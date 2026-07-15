from datetime import datetime, timezone
from typing import Any
from uuid import UUID

from sqlalchemy import Select, asc, desc, func, select
from sqlalchemy import update as sa_update
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

from src.core.db.session import DB_SESSION_VAR
from src.core.exceptions import CustomException
from src.core.logger import LOGGER
from src.shared.repositories.filters import apply_filters
from src.shared.schemas.base import BaseSchema

from typing import Optional

class BaseRepo:

    resource_model: type
    resource_schema: type[BaseSchema]

    def _get_session(self):
        return DB_SESSION_VAR.get()

    @staticmethod
    def _apply_sort(model: type, stmt: Select, sort_by: str, sort_dir: str) -> Select:
        column = getattr(model, sort_by, None)
        if column is None:
            raise ValueError(f"Model '{model.__name__}' has no field '{sort_by}'")
        return stmt.order_by(desc(column) if sort_dir.lower() == "desc" else asc(column))

    @staticmethod
    def _apply_pagination(stmt: Select, page: int, page_size: int) -> Select:
        page_size = min(max(page_size, 1), MAX_PAGE_SIZE)
        offset = (max(page, 1) - 1) * page_size
        return stmt.limit(page_size).offset(offset)

    async def create_record(self, record_details: BaseSchema) -> BaseSchema:
        try:
            db = self._get_session()
            payload = record_details.model_dump(exclude_none=True, exclude_unset=True)
            if not isinstance(payload, dict):
                raise CustomException.ConflictError(message="Invalid data")
            new_record = self.resource_model(**payload)
            db.add(new_record)
            await db.flush()
            await db.refresh(new_record)
            LOGGER.info(f"Created {self.resource_model.__name__} record.")
            return self.resource_schema.model_validate(new_record)
        except IntegrityError as err:
            await db.rollback()
            raise CustomException.ConflictError(resource=f"{self.resource_model.__name__}" , message="something went wrong")

    async def create_bulk_record(self, record_details: list[BaseSchema]) -> list[BaseSchema]:
        try:
            db = self._get_session()
            instances = []
            for details in record_details:
                payload = details.model_dump(exclude_none=True, exclude_unset=True)
                if not isinstance(payload, dict):
                    raise CustomException.ConflictError(message="Payload was not dumped as dict.")
                instances.append(self.resource_model(**payload))
            db.add_all(instances)
            await db.flush()
            result = []
            for inst in instances:
                await db.refresh(inst)
                result.append(self.resource_schema.model_validate(inst))
            LOGGER.info(f"Bulk created {len(result)} {self.resource_model.__name__} records.")
            return result
        
        except IntegrityError as err:
            await db.rollback()
            if "UNIQUE constraint failed" in str(err):
                raise CustomException.ConflictError(resource=f"{self.resource_model.__name__}" , message=err)
            elif "FOREIGN KEY constraint failed" in str(err):
                raise CustomException.ConflictError(resource=f"{self.resource_model.__name__}" , message="Invalide Mapping of resources")
            else:
                raise CustomException.ConflictError(resource=f"{self.resource_model.__name__}" , message="Something went wrong")

    async def update_record(self, record_id: UUID, record_details: BaseSchema) -> BaseSchema:
        db = self._get_session()
        record = await db.get(self.resource_model, record_id)
        if record is None:
            raise CustomException.NotFoundError(
                resource=self.resource_model.__name__,
                resource_id=record_id,
                error_message=f"No {self.resource_model.__name__} with id {record_id}.",
            )
        payload = record_details.model_dump(exclude_none=True, exclude_unset=True)
        if not payload:
            raise CustomException.ConflictError(error_message="No update data provided.")
        for field, value in payload.items():
            if hasattr(record, field):
                setattr(record, field, value)
        await db.flush()
        await db.refresh(record)
        LOGGER.info(f"Updated {self.resource_model.__name__} id={record_id}.")
        return self.resource_schema.model_validate(record)

    async def soft_delete(self, record_id: UUID) -> bool:
        db = self._get_session()
        stmt = (
            sa_update(self.resource_model)
            .where(
                self.resource_model.id == record_id,
                self.resource_model.deleted_at.is_(None),
            )
            .values(deleted_at=datetime.now(timezone.utc))
        )
        result = await db.execute(stmt)
        deleted = result.rowcount > 0
        if deleted:
            LOGGER.info(f"Soft-deleted {self.resource_model.__name__} id={record_id}.")
        return deleted

    async def remove_record(self, record_id: UUID) -> UUID:
        db = self._get_session()
        record = await db.get(self.resource_model, record_id)
        if record is None:
            raise CustomException.NotFoundError(
                resource=self.resource_model.__name__,
                resource_id=record_id,
                error_message=f"No {self.resource_model.__name__} with id {record_id}.",
            )
        await db.delete(record)
        LOGGER.info(f"Hard-deleted {self.resource_model.__name__} id={record_id}.")
        return record_id

    async def get_record_by_id(self, record_id: UUID, use_joinload: bool = False, conver_to_schema:bool = True, allow_deleted:bool=False) -> BaseSchema:
        db = self._get_session()
        record = await db.get(self.resource_model, record_id)
        if record is None:
            raise CustomException.NotFoundError(
                resource=self.resource_model.__name__,
                resource_id=record_id,
                error_message=f"No {self.resource_model.__name__} with id {record_id}.",
            )
        if not allow_deleted and record.is_deleted:
            raise CustomException.ConflictError(resource=f"{self.resource_model.__name__}" , message="Resource is marked deleted.")
        if conver_to_schema:
            return self.resource_schema.model_validate(record)
        else:
            return record

    async def get_all_records(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: str = "created_at",
        sort_dir: str = "asc",
        include_deleted: bool = False,
        use_joinload: bool = False,
        conver_to_schema:bool = True,
        **filters: Any,
    ) -> list[BaseSchema]:
        db = self._get_session()
        stmt: Select = select(self.resource_model)
        if not include_deleted:
            stmt = stmt.where(self.resource_model.deleted_at.is_(None))

        if filters:
            stmt = apply_filters(self.resource_model, stmt, **filters)

        stmt = self._apply_sort(self.resource_model, stmt, sort_by, sort_dir)

        if page and page_size:
            stmt = self._apply_pagination(stmt, page, page_size)
        if use_joinload:
            stmt = stmt.options(joinedload("*"))
        result = await db.execute(stmt)
        records = result.unique().scalars().all()


        if conver_to_schema:
            return [self.resource_schema.model_validate(r) for r in records]
        else:
            return records

    async def get_record_by_fields(self, use_joinload: bool = False, conver_to_schema:bool = True, allow_deleted:bool=False, **filters: Any) -> BaseSchema:
        data = await self.get_all_records(use_joinload=use_joinload, conver_to_schema=conver_to_schema, **filters)

        if not allow_deleted and data[0].is_deleted:
            raise CustomException.ConflictError(resource=f"{self.resource_model.__name__}" , message="Resource is marked deleted.")
        return data[0]

    async def exists(self, **filters: Any) -> bool:
        db = self._get_session()
        stmt = select(func.count()).select_from(self.resource_model)
        stmt = stmt.where(self.resource_model.deleted_at.is_(None))
        stmt = apply_filters(self.resource_model, stmt, **filters)
        result = await db.execute(stmt)
        return (result.scalar() or 0) > 0

    async def count(self, include_deleted: bool = False, **filters: Any) -> int:
        db = self._get_session()
        stmt = select(func.count()).select_from(self.resource_model)
        if not include_deleted:
            stmt = stmt.where(self.resource_model.deleted_at.is_(None))
        if filters:
            stmt = apply_filters(self.resource_model, stmt, **filters)
        result = await db.execute(stmt)
        return result.scalar() or 0



