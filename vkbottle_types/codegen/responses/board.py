import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class BoardAddTopicResponseModel(BaseModel):

    response: int = Field(
        description="Topic ID",
    )


class BoardAddTopicResponse(BaseResponse):
    response: "BoardAddTopicResponseModel"


class BoardCreateCommentResponseModel(BaseModel):

    response: int = Field(
        description="Comment ID",
    )


class BoardCreateCommentResponse(BaseResponse):
    response: "BoardCreateCommentResponseModel"


class BoardGetCommentsExtendedResponseModel(BaseModel):

    response: dict = Field()


class BoardGetCommentsExtendedResponse(BaseResponse):
    response: "BoardGetCommentsExtendedResponseModel"


class BoardGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class BoardGetCommentsResponse(BaseResponse):
    response: "BoardGetCommentsResponseModel"


class BoardGetTopicsExtendedResponseModel(BaseModel):

    response: dict = Field()


class BoardGetTopicsExtendedResponse(BaseResponse):
    response: "BoardGetTopicsExtendedResponseModel"


class BoardGetTopicsResponseModel(BaseModel):

    response: dict = Field()


class BoardGetTopicsResponse(BaseResponse):
    response: "BoardGetTopicsResponseModel"
