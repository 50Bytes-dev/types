import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class UtilsCheckLinkResponseModel(BaseModel):

    response: "UtilsLinkChecked" = Field()


class UtilsCheckLinkResponse(BaseResponse):
    response: "UtilsCheckLinkResponseModel"


class UtilsGetLastShortenedLinksResponseModel(BaseModel):

    response: dict = Field()


class UtilsGetLastShortenedLinksResponse(BaseResponse):
    response: "UtilsGetLastShortenedLinksResponseModel"


class UtilsGetLinkStatsExtendedResponseModel(BaseModel):

    response: "UtilsLinkStatsExtended" = Field()


class UtilsGetLinkStatsExtendedResponse(BaseResponse):
    response: "UtilsGetLinkStatsExtendedResponseModel"


class UtilsGetLinkStatsResponseModel(BaseModel):

    response: "UtilsLinkStats" = Field()


class UtilsGetLinkStatsResponse(BaseResponse):
    response: "UtilsGetLinkStatsResponseModel"


class UtilsGetServerTimeResponseModel(BaseModel):

    response: int = Field(
        description="Time as Unixtime",
    )


class UtilsGetServerTimeResponse(BaseResponse):
    response: "UtilsGetServerTimeResponseModel"


class UtilsGetShortLinkResponseModel(BaseModel):

    response: "UtilsShortLink" = Field()


class UtilsGetShortLinkResponse(BaseResponse):
    response: "UtilsGetShortLinkResponseModel"


class UtilsResolveScreenNameResponseModel(BaseModel):

    response: "UtilsDomainResolved" = Field()


class UtilsResolveScreenNameResponse(BaseResponse):
    response: "UtilsResolveScreenNameResponseModel"
