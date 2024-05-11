import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PagesGetHistoryResponse(BaseModel):

    response: typing.List[PagesWikipageHistory] = Field()


class PagesGetTitlesResponse(BaseModel):

    response: typing.List[PagesWikipage] = Field()


class PagesGetVersionResponse(BaseModel):

    response: "PagesWikipageFull" = Field()


class PagesGetResponse(BaseModel):

    response: "PagesWikipageFull" = Field()


class PagesParseWikiResponse(BaseModel):

    response: str = Field(
        description="HTML source",
    )


class PagesSaveAccessResponse(BaseModel):

    response: int = Field(
        description="Page ID",
    )


class PagesSaveResponse(BaseModel):

    response: int = Field(
        description="Page ID",
    )
