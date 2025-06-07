import enum
import typing
import pydantic
import sys

from typing import Any, Dict, Type, TypeVar

T = TypeVar("T", bound="BaseModel")

# Определяем версию pydantic
PYDANTIC_V2 = pydantic.VERSION.startswith("2.")
PYDANTIC_V1 = pydantic.VERSION.startswith("1.")

# Унифицированный Field
Field = pydantic.Field

# ---- BaseModel ----

if PYDANTIC_V2:

    class BaseModel(pydantic.BaseModel):
        model_config = pydantic.ConfigDict(frozen=True, arbitrary_types_allowed=True)

        @classmethod
        def from_raw(cls: Type[T], data: bytes, /, *, strict: bool = False) -> T:
            return cls.model_validate_json(data, strict=strict)

        @classmethod
        def from_dict(cls: Type[T], data: Dict[str, Any], /) -> T:
            return cls.model_validate(data)

        def to_dict(self) -> Dict[str, Any]:
            return self.model_dump()

elif PYDANTIC_V1:

    class BaseModel(pydantic.BaseModel):
        class Config:
            frozen = True
            arbitrary_types_allowed = True

        @classmethod
        def from_raw(cls: Type[T], data: bytes, /, *, strict: bool = False) -> T:
            return cls.parse_raw(data)

        @classmethod
        def from_dict(cls: Type[T], data: Dict[str, Any], /) -> T:
            return cls.parse_obj(data)

        def to_dict(self) -> Dict[str, Any]:
            return self.dict()
else:
    raise ImportError(f"Unsupported Pydantic version: {pydantic.VERSION}")


# ---- BaseEnumMeta ----


class BaseEnumMeta(enum.EnumMeta):
    def __new__(metacls, cls, bases, classdict, **kwds):
        classdict["NOT_SUPPORTED_MEMBER"] = "NOT_SUPPORTED"
        classdict["_missing_"] = classmethod(lambda cls, _: cls._member_map_["NOT_SUPPORTED_MEMBER"])
        return super().__new__(metacls, cls, bases, classdict, **kwds)


__all__ = ("BaseModel", "BaseEnumMeta", "Field")
