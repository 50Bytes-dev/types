import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class StorageGetKeysResponseModel(BaseModel):

    response: typing.List[str] = Field()


class StorageGetKeysResponse(BaseResponse):
    response: "StorageGetKeysResponseModel"


class StorageGetResponseModel(BaseModel):

    response: typing.List[StorageValue] = Field()


class StorageGetResponse(BaseResponse):
    response: "StorageGetResponseModel"
