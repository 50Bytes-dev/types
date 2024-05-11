import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PagesGetHistoryResponseModel(BaseModel):

    response: typing.List[PagesWikipageHistory] = Field()


class PagesGetHistoryResponse(BaseResponse):
    response: "PagesGetHistoryResponseModel"


class PagesGetTitlesResponseModel(BaseModel):

    response: typing.List[PagesWikipage] = Field()


class PagesGetTitlesResponse(BaseResponse):
    response: "PagesGetTitlesResponseModel"


class PagesGetVersionResponseModel(BaseModel):

    response: "PagesWikipageFull" = Field()


class PagesGetVersionResponse(BaseResponse):
    response: "PagesGetVersionResponseModel"


class PagesGetResponseModel(BaseModel):

    response: "PagesWikipageFull" = Field()


class PagesGetResponse(BaseResponse):
    response: "PagesGetResponseModel"


class PagesParseWikiResponseModel(BaseModel):

    response: str = Field(
        description="HTML source",
    )


class PagesParseWikiResponse(BaseResponse):
    response: "PagesParseWikiResponseModel"


class PagesSaveAccessResponseModel(BaseModel):

    response: int = Field(
        description="Page ID",
    )


class PagesSaveAccessResponse(BaseResponse):
    response: "PagesSaveAccessResponseModel"


class PagesSaveResponseModel(BaseModel):

    response: int = Field(
        description="Page ID",
    )


class PagesSaveResponse(BaseResponse):
    response: "PagesSaveResponseModel"
