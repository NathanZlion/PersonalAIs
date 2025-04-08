from datetime import datetime
from pydantic import BaseModel, Field

from src.utils.helper_functions import get_current_time


class CreatedUpdatedAt(BaseModel):
    """Created and updated at mixin that automatically updates updated_at field."""

    created_at: datetime = Field(default_factory=get_current_time)
    updated_at: datetime = Field(default_factory=get_current_time)

    # model_config = ConfigDict(
    #     validate_assignment=True,
    # )

    # @model_validator(mode="after")  # type: ignore
    # @classmethod
    # def update_updated_at(cls, obj: "CreatedUpdatedAt") -> "CreatedUpdatedAt":
    #     """Update updated_at field."""
    #     # must disable validation to avoid infinite loop
    #     obj.model_config["validate_assignment"] = False

    #     # update updated_at field
    #     obj.updated_at = NOW_FACTORY()

    #     # enable validation again
    #     obj.model_config["validate_assignment"] = True
    #     return obj
