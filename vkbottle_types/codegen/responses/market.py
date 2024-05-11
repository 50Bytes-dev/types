import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class MarketAddAlbumResponse(BaseModel):

    response: dict = Field()


class MarketAddPropertyVariantResponse(BaseModel):

    response: dict = Field()


class MarketAddPropertyResponse(BaseModel):

    response: dict = Field()


class MarketAddResponse(BaseModel):

    response: dict = Field()


class MarketCreateCommentResponse(BaseModel):

    response: int = Field(
        description="Comment ID",
    )


class MarketGetAlbumByIdResponse(BaseModel):

    response: dict = Field()


class MarketGetAlbumsResponse(BaseModel):

    response: dict = Field()


class MarketGetByIdExtendedResponse(BaseModel):

    response: dict = Field()


class MarketGetByIdResponse(BaseModel):

    response: dict = Field()


class MarketGetCategoriesNewResponse(BaseModel):

    response: dict = Field()


class MarketGetCommentsResponse(BaseModel):

    response: dict = Field()


class MarketGetGroupOrdersResponse(BaseModel):

    response: dict = Field()


class MarketGetOrderByIdResponse(BaseModel):

    response: dict = Field()


class MarketGetOrderItemsResponse(BaseModel):

    response: dict = Field()


class MarketGetOrdersExtendedResponse(BaseModel):

    response: dict = Field()


class MarketGetOrdersResponse(BaseModel):

    response: dict = Field()


class MarketGetPropertiesResponse(BaseModel):

    response: dict = Field()


class MarketGetExtendedResponse(BaseModel):

    response: dict = Field()


class MarketGetResponse(BaseModel):

    response: dict = Field()


class MarketGroupItemsResponse(BaseModel):

    response: dict = Field()


class MarketPhotoIdResponse(BaseModel):

    response: dict = Field()


class MarketSearchBasicResponse(BaseModel):

    response: dict = Field()


class MarketSearchExtendedResponse(BaseModel):

    response: dict = Field()


class MarketSearchResponse(BaseModel):

    response: dict = Field()
