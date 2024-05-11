import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class DonutGetSubscriptionResponseModel(BaseModel):

    response: "DonutDonatorSubscriptionInfo" = Field()


class DonutGetSubscriptionResponse(BaseResponse):
    response: "DonutGetSubscriptionResponseModel"


class DonutGetSubscriptionsResponseModel(BaseModel):

    response: dict = Field()


class DonutGetSubscriptionsResponse(BaseResponse):
    response: "DonutGetSubscriptionsResponseModel"
