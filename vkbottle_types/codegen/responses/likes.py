import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class LikesAddResponse(BaseModel):

    response: dict = Field()


class LikesDeleteResponse(BaseModel):

    response: dict = Field()


class LikesGetListExtendedResponse(BaseModel):

    response: dict = Field()


class LikesGetListResponse(BaseModel):

    response: dict = Field()


class LikesIsLikedResponse(BaseModel):

    response: dict = Field()
