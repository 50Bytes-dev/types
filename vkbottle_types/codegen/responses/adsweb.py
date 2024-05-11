import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class AdswebGetAdCategoriesResponseModel(BaseModel):

    response: dict = Field()


class AdswebGetAdCategoriesResponse(BaseResponse):
    response: "AdswebGetAdCategoriesResponseModel"


class AdswebGetAdUnitCodeResponseModel(BaseModel):

    response: dict = Field()


class AdswebGetAdUnitCodeResponse(BaseResponse):
    response: "AdswebGetAdUnitCodeResponseModel"


class AdswebGetAdUnitsResponseModel(BaseModel):

    response: dict = Field()


class AdswebGetAdUnitsResponse(BaseResponse):
    response: "AdswebGetAdUnitsResponseModel"


class AdswebGetFraudHistoryResponseModel(BaseModel):

    response: dict = Field()


class AdswebGetFraudHistoryResponse(BaseResponse):
    response: "AdswebGetFraudHistoryResponseModel"


class AdswebGetSitesResponseModel(BaseModel):

    response: dict = Field()


class AdswebGetSitesResponse(BaseResponse):
    response: "AdswebGetSitesResponseModel"


class AdswebGetStatisticsResponseModel(BaseModel):

    response: dict = Field()


class AdswebGetStatisticsResponse(BaseResponse):
    response: "AdswebGetStatisticsResponseModel"
