import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class LeadFormsCreateResponseModel(BaseModel):

    response: dict = Field()


class LeadFormsCreateResponse(BaseResponse):
    response: "LeadFormsCreateResponseModel"


class LeadFormsDeleteResponseModel(BaseModel):

    response: dict = Field()


class LeadFormsDeleteResponse(BaseResponse):
    response: "LeadFormsDeleteResponseModel"


class LeadFormsGetLeadsResponseModel(BaseModel):

    response: dict = Field()


class LeadFormsGetLeadsResponse(BaseResponse):
    response: "LeadFormsGetLeadsResponseModel"


class LeadFormsGetResponseModel(BaseModel):

    response: "LeadFormsForm" = Field()


class LeadFormsGetResponse(BaseResponse):
    response: "LeadFormsGetResponseModel"


class LeadFormsListResponseModel(BaseModel):

    response: typing.List[LeadFormsForm] = Field()


class LeadFormsListResponse(BaseResponse):
    response: "LeadFormsListResponseModel"


class LeadFormsUploadUrlResponseModel(BaseModel):

    response: str = Field()


class LeadFormsUploadUrlResponse(BaseResponse):
    response: "LeadFormsUploadUrlResponseModel"
