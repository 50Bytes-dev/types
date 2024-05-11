import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class StreamingGetServerUrlResponseModel(BaseModel):

    response: dict = Field()


class StreamingGetServerUrlResponse(BaseResponse):
    response: "StreamingGetServerUrlResponseModel"


class StreamingGetStatsResponseModel(BaseModel):

    response: typing.List[StreamingStats] = Field()


class StreamingGetStatsResponse(BaseResponse):
    response: "StreamingGetStatsResponseModel"


class StreamingGetStemResponseModel(BaseModel):

    response: dict = Field()


class StreamingGetStemResponse(BaseResponse):
    response: "StreamingGetStemResponseModel"
