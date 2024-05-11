import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PollsCreateResponse(BaseModel):

    response: "PollsPoll" = Field()


class PollsGetBackgroundsResponse(BaseModel):

    response: typing.List[PollsBackground] = Field()


class PollsGetByIdResponse(BaseModel):

    response: "PollsPollExtended" = Field()


class PollsGetVotersFieldsResponse(BaseModel):

    response: typing.List[PollsFieldsVoters] = Field()


class PollsGetVotersResponse(BaseModel):

    response: typing.List[PollsVoters] = Field()


class PollsSavePhotoResponse(BaseModel):

    response: "PollsBackground" = Field()
