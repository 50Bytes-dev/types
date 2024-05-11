import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class SecureCheckTokenResponseModel(BaseModel):

    response: "SecureTokenChecked" = Field()


class SecureCheckTokenResponse(BaseResponse):
    response: "SecureCheckTokenResponseModel"


class SecureGetAppBalanceResponseModel(BaseModel):

    response: int = Field(
        description="App balance",
    )


class SecureGetAppBalanceResponse(BaseResponse):
    response: "SecureGetAppBalanceResponseModel"


class SecureGetSMSHistoryResponseModel(BaseModel):

    response: typing.List[SecureSmsNotification] = Field()


class SecureGetSMSHistoryResponse(BaseResponse):
    response: "SecureGetSMSHistoryResponseModel"


class SecureGetTransactionsHistoryResponseModel(BaseModel):

    response: typing.List[SecureTransaction] = Field()


class SecureGetTransactionsHistoryResponse(BaseResponse):
    response: "SecureGetTransactionsHistoryResponseModel"


class SecureGetUserLevelResponseModel(BaseModel):

    response: typing.List[SecureLevel] = Field()


class SecureGetUserLevelResponse(BaseResponse):
    response: "SecureGetUserLevelResponseModel"


class SecureGiveEventStickerResponseModel(BaseModel):

    response: typing.List[SecureGiveEventStickerItem] = Field()


class SecureGiveEventStickerResponse(BaseResponse):
    response: "SecureGiveEventStickerResponseModel"


class SecureSendNotificationResponseModel(BaseModel):

    response: typing.List[int] = Field()


class SecureSendNotificationResponse(BaseResponse):
    response: "SecureSendNotificationResponseModel"


class SecureSetCounterArrayResponseModel(BaseModel):

    response: typing.List[SecureSetCounterItem] = Field()


class SecureSetCounterArrayResponse(BaseResponse):
    response: "SecureSetCounterArrayResponseModel"
