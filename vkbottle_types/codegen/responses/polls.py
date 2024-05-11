import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PollsCreateResponseModel(BaseModel):

    response: "PollsPoll" = Field()


class PollsCreateResponse(BaseResponse):
    response: "PollsCreateResponseModel"


class PollsGetBackgroundsResponseModel(BaseModel):

    response: typing.List[PollsBackground] = Field()


class PollsGetBackgroundsResponse(BaseResponse):
    response: "PollsGetBackgroundsResponseModel"


class PollsGetByIdResponseModel(BaseModel):

    response: "PollsPollExtended" = Field()


class PollsGetByIdResponse(BaseResponse):
    response: "PollsGetByIdResponseModel"


class PollsGetVotersFieldsResponseModel(BaseModel):

    response: typing.List[PollsFieldsVoters] = Field()


class PollsGetVotersFieldsResponse(BaseResponse):
    response: "PollsGetVotersFieldsResponseModel"


class PollsGetVotersResponseModel(BaseModel):

    response: typing.List[PollsVoters] = Field()


class PollsGetVotersResponse(BaseResponse):
    response: "PollsGetVotersResponseModel"


class PollsSavePhotoResponseModel(BaseModel):

    response: "PollsBackground" = Field()


class PollsSavePhotoResponse(BaseResponse):
    response: "PollsSavePhotoResponseModel"
