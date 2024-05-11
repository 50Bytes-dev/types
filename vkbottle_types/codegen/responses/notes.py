import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class NotesAddResponseModel(BaseModel):

    response: int = Field(
        description="Note ID",
    )


class NotesAddResponse(BaseResponse):
    response: "NotesAddResponseModel"


class NotesCreateCommentResponseModel(BaseModel):

    response: int = Field(
        description="Comment ID",
    )


class NotesCreateCommentResponse(BaseResponse):
    response: "NotesCreateCommentResponseModel"


class NotesGetByIdResponseModel(BaseModel):

    response: "NotesNote" = Field()


class NotesGetByIdResponse(BaseResponse):
    response: "NotesGetByIdResponseModel"


class NotesGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class NotesGetCommentsResponse(BaseResponse):
    response: "NotesGetCommentsResponseModel"


class NotesGetResponseModel(BaseModel):

    response: dict = Field()


class NotesGetResponse(BaseResponse):
    response: "NotesGetResponseModel"
