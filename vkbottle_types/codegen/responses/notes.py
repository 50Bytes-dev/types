import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class NotesAddResponse(BaseModel):

    response: int = Field(
        description="Note ID",
    )


class NotesCreateCommentResponse(BaseModel):

    response: int = Field(
        description="Comment ID",
    )


class NotesGetByIdResponse(BaseModel):

    response: "NotesNote" = Field()


class NotesGetCommentsResponse(BaseModel):

    response: dict = Field()


class NotesGetResponse(BaseModel):

    response: dict = Field()
