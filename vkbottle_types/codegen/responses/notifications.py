import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class NotificationsGetResponseModel(BaseModel):

    response: dict = Field()


class NotificationsGetResponse(BaseResponse):
    response: "NotificationsGetResponseModel"


class NotificationsSendMessageResponseModel(BaseModel):

    response: typing.List[NotificationsSendMessageItem] = Field()


class NotificationsSendMessageResponse(BaseResponse):
    response: "NotificationsSendMessageResponseModel"
