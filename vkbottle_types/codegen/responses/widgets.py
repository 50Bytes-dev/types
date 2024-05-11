import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class WidgetsGetCommentsResponse(BaseModel):

    response: dict = Field()


class WidgetsGetPagesResponse(BaseModel):

    response: dict = Field()
