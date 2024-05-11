import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class DocsAddResponseModel(BaseModel):

    response: int = Field(
        description="Document ID",
    )


class DocsAddResponse(BaseResponse):
    response: "DocsAddResponseModel"


class DocsDocUploadResponseModel(BaseModel):

    response: dict = Field()


class DocsDocUploadResponse(BaseResponse):
    response: "DocsDocUploadResponseModel"


class DocsGetByIdResponseModel(BaseModel):

    response: typing.List[DocsDoc] = Field()


class DocsGetByIdResponse(BaseResponse):
    response: "DocsGetByIdResponseModel"


class DocsGetTypesResponseModel(BaseModel):

    response: dict = Field()


class DocsGetTypesResponse(BaseResponse):
    response: "DocsGetTypesResponseModel"


class DocsGetUploadServerResponseModel(BaseModel):

    response: "BaseUploadServer" = Field()


class DocsGetUploadServerResponse(BaseResponse):
    response: "DocsGetUploadServerResponseModel"


class DocsGetResponseModel(BaseModel):

    response: dict = Field()


class DocsGetResponse(BaseResponse):
    response: "DocsGetResponseModel"


class DocsSaveResponseModel(BaseModel):

    response: dict = Field()


class DocsSaveResponse(BaseResponse):
    response: "DocsSaveResponseModel"


class DocsSearchResponseModel(BaseModel):

    response: dict = Field()


class DocsSearchResponse(BaseResponse):
    response: "DocsSearchResponseModel"
