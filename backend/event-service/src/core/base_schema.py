from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema for all Pydantic models."""

    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        validate_assignment=True,
        extra="forbid",
        use_enum_values=True,
        populate_by_name=True,
        validate_default=True,
        arbitrary_types_allowed=True,
    )