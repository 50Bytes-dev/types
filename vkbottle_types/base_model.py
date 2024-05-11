import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(frozen=True)


Field = pydantic.Field

__all__ = ("BaseModel",)
