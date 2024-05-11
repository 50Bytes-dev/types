import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class UsersGetFollowersFieldsResponseModel(BaseModel):

    response: dict = Field()


class UsersGetFollowersFieldsResponse(BaseResponse):
    response: "UsersGetFollowersFieldsResponseModel"


class UsersGetFollowersResponseModel(BaseModel):

    response: dict = Field()


class UsersGetFollowersResponse(BaseResponse):
    response: "UsersGetFollowersResponseModel"


class UsersGetSubscriptionsExtendedResponseModel(BaseModel):

    response: dict = Field()


class UsersGetSubscriptionsExtendedResponse(BaseResponse):
    response: "UsersGetSubscriptionsExtendedResponseModel"


class UsersGetSubscriptionsResponseModel(BaseModel):

    response: dict = Field()


class UsersGetSubscriptionsResponse(BaseResponse):
    response: "UsersGetSubscriptionsResponseModel"


class UsersGetResponseModel(BaseModel):

    response: typing.List[UsersUserFull] = Field()


class UsersGetResponse(BaseResponse):
    response: "UsersGetResponseModel"


class UsersSearchResponseModel(BaseModel):

    response: dict = Field()


class UsersSearchResponse(BaseResponse):
    response: "UsersSearchResponseModel"
