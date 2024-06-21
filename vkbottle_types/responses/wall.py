import inspect

from vkbottle_types.codegen.responses.wall import *  # noqa: F403,F401

from .base_response import BaseResponse


class WallGetObject(BaseModel):
    items: List["WallWallItem"]
    count: int


class WallGetResponse(BaseResponse):
    response: WallGetObject = None


class WallGetExtendedObject(BaseModel):
    items: List["WallWallItem"]
    profiles: List["UsersUserFull"]
    groups: List["GroupsGroupFull"]
    count: int


class WallGetExtendedResponse(BaseResponse):
    response: WallGetExtendedObject


class WallGetCommentsObject(BaseModel):
    items: List["WallWallComment"]
    count: int


class WallGetCommentsResponse(BaseResponse):
    response: WallGetCommentsObject


class WallGetCommentsExtendedObject(BaseModel):
    items: List["WallWallComment"]
    profiles: List["UsersUserFull"]
    groups: List["GroupsGroupFull"]
    current_level_count: int
    can_post: bool
    show_reply_button: bool
    groups_can_post: bool
    post_author_id: int
    count: int


class WallGetCommentsExtendedResponse(BaseResponse):
    response: WallGetCommentsExtendedObject


_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if not (inspect.isclass(item) and issubclass(item, BaseResponse)):
        continue
    if item.__name__ == "BaseModel":
        continue
    item.model_rebuild()
    for parent in item.__bases__:
        if parent.__name__ == item.__name__:
            parent.model_fields.update(item.model_fields)
            parent.model_rebuild()
