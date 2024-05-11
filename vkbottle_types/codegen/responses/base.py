import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class BaseBoolResponse(BaseModel):

    response: bool = Field()


class BaseGetUploadServerResponse(BaseModel):

    response: "BaseUploadServer" = Field()


class BaseOkResponse(BaseModel):

    response: int = Field()


class BaseUndefinedResponse(BaseModel):

    response: dict = Field()
