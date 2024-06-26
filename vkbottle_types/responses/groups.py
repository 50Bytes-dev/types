import inspect
from typing import List, Optional

from vkbottle_types.codegen.responses.groups import *  # noqa: F403,F401
from vkbottle_types.objects import GroupsMemberRole, GroupsUserXtrRole
from vkbottle_types.responses.base_response import BaseResponse


class GetMembersFilterManagersResponse(BaseResponse):
    response: "GetMembersFilterManagersResponseModel"


class GetMembersFieldsFilterManagersResponse(BaseResponse):
    response: "GetMembersFieldsFilterManagersResponseModel"


class GetMembersFilterManagersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsMemberRole"]] = None


class GetMembersFieldsFilterManagersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsUserXtrRole"]] = None


class GroupsGetByIdObject(BaseModel):
    groups: List["GroupsGroupFull"]
    profiles: List["UsersUserFull"]


class GroupsGetByIdObjectResponse(BaseResponse):
    response: GroupsGetByIdObject


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
