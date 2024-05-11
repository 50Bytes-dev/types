import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class OrdersChangeStateResponseModel(BaseModel):

    response: str = Field(
        description="New state",
    )


class OrdersChangeStateResponse(BaseResponse):
    response: "OrdersChangeStateResponseModel"


class OrdersGetAmountResponseModel(BaseModel):

    response: typing.List[OrdersAmount] = Field()


class OrdersGetAmountResponse(BaseResponse):
    response: "OrdersGetAmountResponseModel"


class OrdersGetByIdResponseModel(BaseModel):

    response: typing.List[OrdersOrder] = Field()


class OrdersGetByIdResponse(BaseResponse):
    response: "OrdersGetByIdResponseModel"


class OrdersGetUserSubscriptionByIdResponseModel(BaseModel):

    response: "OrdersSubscription" = Field()


class OrdersGetUserSubscriptionByIdResponse(BaseResponse):
    response: "OrdersGetUserSubscriptionByIdResponseModel"


class OrdersGetUserSubscriptionsResponseModel(BaseModel):

    response: dict = Field()


class OrdersGetUserSubscriptionsResponse(BaseResponse):
    response: "OrdersGetUserSubscriptionsResponseModel"


class OrdersGetResponseModel(BaseModel):

    response: typing.List[OrdersOrder] = Field()


class OrdersGetResponse(BaseResponse):
    response: "OrdersGetResponseModel"
