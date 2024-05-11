import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class FaveAddTagResponseModel(BaseModel):

    response: "FaveTag" = Field()


class FaveAddTagResponse(BaseResponse):
    response: "FaveAddTagResponseModel"


class FaveGetPagesResponseModel(BaseModel):

    response: dict = Field()


class FaveGetPagesResponse(BaseResponse):
    response: "FaveGetPagesResponseModel"


class FaveGetTagsResponseModel(BaseModel):

    response: dict = Field()


class FaveGetTagsResponse(BaseResponse):
    response: "FaveGetTagsResponseModel"


class FaveGetExtendedResponseModel(BaseModel):

    response: dict = Field()


class FaveGetExtendedResponse(BaseResponse):
    response: "FaveGetExtendedResponseModel"


class FaveGetResponseModel(BaseModel):

    response: dict = Field()


class FaveGetResponse(BaseResponse):
    response: "FaveGetResponseModel"
