import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class MarketAddAlbumResponseModel(BaseModel):

    response: dict = Field()


class MarketAddAlbumResponse(BaseResponse):
    response: "MarketAddAlbumResponseModel"


class MarketAddPropertyVariantResponseModel(BaseModel):

    response: dict = Field()


class MarketAddPropertyVariantResponse(BaseResponse):
    response: "MarketAddPropertyVariantResponseModel"


class MarketAddPropertyResponseModel(BaseModel):

    response: dict = Field()


class MarketAddPropertyResponse(BaseResponse):
    response: "MarketAddPropertyResponseModel"


class MarketAddResponseModel(BaseModel):

    response: dict = Field()


class MarketAddResponse(BaseResponse):
    response: "MarketAddResponseModel"


class MarketCreateCommentResponseModel(BaseModel):

    response: int = Field(
        description="Comment ID",
    )


class MarketCreateCommentResponse(BaseResponse):
    response: "MarketCreateCommentResponseModel"


class MarketGetAlbumByIdResponseModel(BaseModel):

    response: dict = Field()


class MarketGetAlbumByIdResponse(BaseResponse):
    response: "MarketGetAlbumByIdResponseModel"


class MarketGetAlbumsResponseModel(BaseModel):

    response: dict = Field()


class MarketGetAlbumsResponse(BaseResponse):
    response: "MarketGetAlbumsResponseModel"


class MarketGetByIdExtendedResponseModel(BaseModel):

    response: dict = Field()


class MarketGetByIdExtendedResponse(BaseResponse):
    response: "MarketGetByIdExtendedResponseModel"


class MarketGetByIdResponseModel(BaseModel):

    response: dict = Field()


class MarketGetByIdResponse(BaseResponse):
    response: "MarketGetByIdResponseModel"


class MarketGetCategoriesNewResponseModel(BaseModel):

    response: dict = Field()


class MarketGetCategoriesNewResponse(BaseResponse):
    response: "MarketGetCategoriesNewResponseModel"


class MarketGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class MarketGetCommentsResponse(BaseResponse):
    response: "MarketGetCommentsResponseModel"


class MarketGetGroupOrdersResponseModel(BaseModel):

    response: dict = Field()


class MarketGetGroupOrdersResponse(BaseResponse):
    response: "MarketGetGroupOrdersResponseModel"


class MarketGetOrderByIdResponseModel(BaseModel):

    response: dict = Field()


class MarketGetOrderByIdResponse(BaseResponse):
    response: "MarketGetOrderByIdResponseModel"


class MarketGetOrderItemsResponseModel(BaseModel):

    response: dict = Field()


class MarketGetOrderItemsResponse(BaseResponse):
    response: "MarketGetOrderItemsResponseModel"


class MarketGetOrdersExtendedResponseModel(BaseModel):

    response: dict = Field()


class MarketGetOrdersExtendedResponse(BaseResponse):
    response: "MarketGetOrdersExtendedResponseModel"


class MarketGetOrdersResponseModel(BaseModel):

    response: dict = Field()


class MarketGetOrdersResponse(BaseResponse):
    response: "MarketGetOrdersResponseModel"


class MarketGetPropertiesResponseModel(BaseModel):

    response: dict = Field()


class MarketGetPropertiesResponse(BaseResponse):
    response: "MarketGetPropertiesResponseModel"


class MarketGetExtendedResponseModel(BaseModel):

    response: dict = Field()


class MarketGetExtendedResponse(BaseResponse):
    response: "MarketGetExtendedResponseModel"


class MarketGetResponseModel(BaseModel):

    response: dict = Field()


class MarketGetResponse(BaseResponse):
    response: "MarketGetResponseModel"


class MarketGroupItemsResponseModel(BaseModel):

    response: dict = Field()


class MarketGroupItemsResponse(BaseResponse):
    response: "MarketGroupItemsResponseModel"


class MarketPhotoIdResponseModel(BaseModel):

    response: dict = Field()


class MarketPhotoIdResponse(BaseResponse):
    response: "MarketPhotoIdResponseModel"


class MarketSearchBasicResponseModel(BaseModel):

    response: dict = Field()


class MarketSearchBasicResponse(BaseResponse):
    response: "MarketSearchBasicResponseModel"


class MarketSearchExtendedResponseModel(BaseModel):

    response: dict = Field()


class MarketSearchExtendedResponse(BaseResponse):
    response: "MarketSearchExtendedResponseModel"


class MarketSearchResponseModel(BaseModel):

    response: dict = Field()


class MarketSearchResponse(BaseResponse):
    response: "MarketSearchResponseModel"
