import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class StoriesGetBannedExtendedResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetBannedExtendedResponse(BaseResponse):
    response: "StoriesGetBannedExtendedResponseModel"


class StoriesGetBannedResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetBannedResponse(BaseResponse):
    response: "StoriesGetBannedResponseModel"


class StoriesGetByIdExtendedResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetByIdExtendedResponse(BaseResponse):
    response: "StoriesGetByIdExtendedResponseModel"


class StoriesGetPhotoUploadServerResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetPhotoUploadServerResponse(BaseResponse):
    response: "StoriesGetPhotoUploadServerResponseModel"


class StoriesGetStatsV5200ResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetStatsV5200Response(BaseResponse):
    response: "StoriesGetStatsV5200ResponseModel"


class StoriesGetStatsResponseModel(BaseModel):

    response: "StoriesStoryStats" = Field()


class StoriesGetStatsResponse(BaseResponse):
    response: "StoriesGetStatsResponseModel"


class StoriesGetVideoUploadServerResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetVideoUploadServerResponse(BaseResponse):
    response: "StoriesGetVideoUploadServerResponseModel"


class StoriesGetViewersExtendedV5115ResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetViewersExtendedV5115Response(BaseResponse):
    response: "StoriesGetViewersExtendedV5115ResponseModel"


class StoriesGetV5113ResponseModel(BaseModel):

    response: dict = Field()


class StoriesGetV5113Response(BaseResponse):
    response: "StoriesGetV5113ResponseModel"


class StoriesSaveResponseModel(BaseModel):

    response: dict = Field()


class StoriesSaveResponse(BaseResponse):
    response: "StoriesSaveResponseModel"


class StoriesUploadResponseModel(BaseModel):

    response: dict = Field()


class StoriesUploadResponse(BaseResponse):
    response: "StoriesUploadResponseModel"
