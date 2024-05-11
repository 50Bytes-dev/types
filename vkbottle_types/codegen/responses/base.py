import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class BaseBoolResponseModel(BaseModel):

    response: bool = Field()


class BaseBoolResponse(BaseResponse):
    response: "BaseBoolResponseModel"


class BaseGetUploadServerResponseModel(BaseModel):

    response: "BaseUploadServer" = Field()


class BaseGetUploadServerResponse(BaseResponse):
    response: "BaseGetUploadServerResponseModel"


class BaseOkResponseModel(BaseModel):

    response: int = Field()


class BaseOkResponse(BaseResponse):
    response: "BaseOkResponseModel"


class BaseUndefinedResponseModel(BaseModel):

    response: dict = Field()


class BaseUndefinedResponse(BaseResponse):
    response: "BaseUndefinedResponseModel"
