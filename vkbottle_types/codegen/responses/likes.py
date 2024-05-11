import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class LikesAddResponseModel(BaseModel):

    response: dict = Field()


class LikesAddResponse(BaseResponse):
    response: "LikesAddResponseModel"


class LikesDeleteResponseModel(BaseModel):

    response: dict = Field()


class LikesDeleteResponse(BaseResponse):
    response: "LikesDeleteResponseModel"


class LikesGetListExtendedResponseModel(BaseModel):

    response: dict = Field()


class LikesGetListExtendedResponse(BaseResponse):
    response: "LikesGetListExtendedResponseModel"


class LikesGetListResponseModel(BaseModel):

    response: dict = Field()


class LikesGetListResponse(BaseResponse):
    response: "LikesGetListResponseModel"


class LikesIsLikedResponseModel(BaseModel):

    response: dict = Field()


class LikesIsLikedResponse(BaseResponse):
    response: "LikesIsLikedResponseModel"
