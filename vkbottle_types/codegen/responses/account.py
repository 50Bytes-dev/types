import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class AccountChangePasswordResponseModel(BaseModel):

    response: dict = Field()


class AccountChangePasswordResponse(BaseResponse):
    response: "AccountChangePasswordResponseModel"


class AccountGetActiveOffersResponseModel(BaseModel):

    response: dict = Field()


class AccountGetActiveOffersResponse(BaseResponse):
    response: "AccountGetActiveOffersResponseModel"


class AccountGetAppPermissionsResponseModel(BaseModel):

    response: int = Field(
        description="Permissions mask",
    )


class AccountGetAppPermissionsResponse(BaseResponse):
    response: "AccountGetAppPermissionsResponseModel"


class AccountGetBannedResponseModel(BaseModel):

    response: dict = Field()


class AccountGetBannedResponse(BaseResponse):
    response: "AccountGetBannedResponseModel"


class AccountGetCountersResponseModel(BaseModel):

    response: "AccountAccountCounters" = Field()


class AccountGetCountersResponse(BaseResponse):
    response: "AccountGetCountersResponseModel"


class AccountGetInfoResponseModel(BaseModel):

    response: "AccountInfo" = Field()


class AccountGetInfoResponse(BaseResponse):
    response: "AccountGetInfoResponseModel"


class AccountGetProfileInfoResponseModel(BaseModel):

    response: "AccountUserSettings" = Field()


class AccountGetProfileInfoResponse(BaseResponse):
    response: "AccountGetProfileInfoResponseModel"


class AccountGetPushSettingsResponseModel(BaseModel):

    response: "AccountPushSettings" = Field()


class AccountGetPushSettingsResponse(BaseResponse):
    response: "AccountGetPushSettingsResponseModel"


class AccountSaveProfileInfoResponseModel(BaseModel):

    response: dict = Field()


class AccountSaveProfileInfoResponse(BaseResponse):
    response: "AccountSaveProfileInfoResponseModel"
