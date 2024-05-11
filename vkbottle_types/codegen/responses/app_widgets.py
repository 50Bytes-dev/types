import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class AppWidgetsGetAppImageUploadServerResponseModel(BaseModel):

    response: dict = Field()


class AppWidgetsGetAppImageUploadServerResponse(BaseResponse):
    response: "AppWidgetsGetAppImageUploadServerResponseModel"


class AppWidgetsGetAppImagesResponseModel(BaseModel):

    response: "AppWidgetsPhotos" = Field()


class AppWidgetsGetAppImagesResponse(BaseResponse):
    response: "AppWidgetsGetAppImagesResponseModel"


class AppWidgetsGetGroupImageUploadServerResponseModel(BaseModel):

    response: dict = Field()


class AppWidgetsGetGroupImageUploadServerResponse(BaseResponse):
    response: "AppWidgetsGetGroupImageUploadServerResponseModel"


class AppWidgetsGetGroupImagesResponseModel(BaseModel):

    response: "AppWidgetsPhotos" = Field()


class AppWidgetsGetGroupImagesResponse(BaseResponse):
    response: "AppWidgetsGetGroupImagesResponseModel"


class AppWidgetsGetImagesByIdResponseModel(BaseModel):

    response: typing.List[AppWidgetsPhoto] = Field()


class AppWidgetsGetImagesByIdResponse(BaseResponse):
    response: "AppWidgetsGetImagesByIdResponseModel"


class AppWidgetsSaveAppImageResponseModel(BaseModel):

    response: "AppWidgetsPhoto" = Field()


class AppWidgetsSaveAppImageResponse(BaseResponse):
    response: "AppWidgetsSaveAppImageResponseModel"


class AppWidgetsSaveGroupImageResponseModel(BaseModel):

    response: "AppWidgetsPhoto" = Field()


class AppWidgetsSaveGroupImageResponse(BaseResponse):
    response: "AppWidgetsSaveGroupImageResponseModel"
