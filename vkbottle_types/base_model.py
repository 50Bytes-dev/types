import pydantic


class RootModel(pydantic.RootModel):
    model_config = pydantic.ConfigDict(frozen=True)


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(frozen=True)


Field = pydantic.Field

__all__ = ("BaseModel",)
