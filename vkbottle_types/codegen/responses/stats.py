import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class StatsGetPostReachResponseModel(BaseModel):

    response: typing.List[StatsWallpostStat] = Field()


class StatsGetPostReachResponse(BaseResponse):
    response: "StatsGetPostReachResponseModel"


class StatsGetResponseModel(BaseModel):

    response: typing.List[StatsPeriod] = Field()


class StatsGetResponse(BaseResponse):
    response: "StatsGetResponseModel"
