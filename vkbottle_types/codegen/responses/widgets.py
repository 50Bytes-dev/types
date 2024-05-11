import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class WidgetsGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class WidgetsGetCommentsResponse(BaseResponse):
    response: "WidgetsGetCommentsResponseModel"


class WidgetsGetPagesResponseModel(BaseModel):

    response: dict = Field()


class WidgetsGetPagesResponse(BaseResponse):
    response: "WidgetsGetPagesResponseModel"
