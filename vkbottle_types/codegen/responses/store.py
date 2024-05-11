import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class StoreGetFavoriteStickersResponse(BaseModel):

    response: dict = Field()


class StoreGetProductsResponse(BaseModel):

    response: dict = Field()


class StoreGetStickersKeywordsResponse(BaseModel):

    response: dict = Field()
