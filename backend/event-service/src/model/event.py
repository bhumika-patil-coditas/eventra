from __future__ import annotations

from datetime import date

from sqlalchemy import Date, Enum as SQLEnum, Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column, validates

from src.core import Base, IdTimeStampMixin
from src.utils.constants import EventStatus

class Event(Base, IdTimeStampMixin):
    __tablename__ = "events"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    event_date: Mapped[date] = mapped_column(Date, nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    requirements: Mapped[str] = mapped_column(Text, nullable=False)

    budget_min: Mapped[float] = mapped_column(Float, nullable=False)
    budget_max: Mapped[float] = mapped_column(Float, nullable=False)

    status: Mapped[EventStatus] = mapped_column(
        SQLEnum(EventStatus, name="event_status"),
        default=EventStatus.DRAFT,
        nullable=False,
    )

    @validates("event_date")
    def validate_event_date(self, key: str, value: date) -> date:
        if value <= date.today():
            raise ValueError("Event date must be in the future.")
        return value

    @validates("budget_min")
    def validate_budget_min(self, key: str, value: float) -> float:
        if value < 0:
            raise ValueError("Minimum budget cannot be negative.")

        if hasattr(self, "budget_max") and self.budget_max is not None:
            if value > self.budget_max:
                raise ValueError("Minimum budget cannot exceed maximum budget.")

        return value

    @validates("budget_max")
    def validate_budget_max(self, key: str, value: float) -> float:
        if value < 0:
            raise ValueError("Maximum budget cannot be negative.")

        if hasattr(self, "budget_min") and self.budget_min is not None:
            if value < self.budget_min:
                raise ValueError("Maximum budget cannot be less than minimum budget.")

        return value