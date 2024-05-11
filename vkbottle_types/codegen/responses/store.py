import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class StoreGetFavoriteStickersResponseModel(BaseModel):

    response: dict = Field()


class StoreGetFavoriteStickersResponse(BaseResponse):
    response: "StoreGetFavoriteStickersResponseModel"


class StoreGetProductsResponseModel(BaseModel):

    response: dict = Field()


class StoreGetProductsResponse(BaseResponse):
    response: "StoreGetProductsResponseModel"


class StoreGetStickersKeywordsResponseModel(BaseModel):

    response: dict = Field()


class StoreGetStickersKeywordsResponse(BaseResponse):
    response: "StoreGetStickersKeywordsResponseModel"
