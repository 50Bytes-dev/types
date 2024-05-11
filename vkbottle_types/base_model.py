import pydantic


class BaseModel(pydantic.BaseModel):
    class Config:
        frozen = True


Field = pydantic.Field

__all__ = ("BaseModel",)
