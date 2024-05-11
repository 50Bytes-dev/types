import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PrettyCardsCreateResponseModel(BaseModel):

    response: dict = Field()


class PrettyCardsCreateResponse(BaseResponse):
    response: "PrettyCardsCreateResponseModel"


class PrettyCardsDeleteResponseModel(BaseModel):

    response: dict = Field()


class PrettyCardsDeleteResponse(BaseResponse):
    response: "PrettyCardsDeleteResponseModel"


class PrettyCardsEditResponseModel(BaseModel):

    response: dict = Field()


class PrettyCardsEditResponse(BaseResponse):
    response: "PrettyCardsEditResponseModel"


class PrettyCardsGetByIdResponseModel(BaseModel):

    response: typing.List[PrettyCardsPrettyCardOrError] = Field()


class PrettyCardsGetByIdResponse(BaseResponse):
    response: "PrettyCardsGetByIdResponseModel"


class PrettyCardsGetUploadURLResponseModel(BaseModel):

    response: str = Field(
        description="Upload URL",
    )


class PrettyCardsGetUploadURLResponse(BaseResponse):
    response: "PrettyCardsGetUploadURLResponseModel"


class PrettyCardsGetResponseModel(BaseModel):

    response: dict = Field()


class PrettyCardsGetResponse(BaseResponse):
    response: "PrettyCardsGetResponseModel"
