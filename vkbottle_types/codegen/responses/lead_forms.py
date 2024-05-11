import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class LeadFormsCreateResponse(BaseModel):

    response: dict = Field()


class LeadFormsDeleteResponse(BaseModel):

    response: dict = Field()


class LeadFormsGetLeadsResponse(BaseModel):

    response: dict = Field()


class LeadFormsGetResponse(BaseModel):

    response: "LeadFormsForm" = Field()


class LeadFormsListResponse(BaseModel):

    response: typing.List[LeadFormsForm] = Field()


class LeadFormsUploadUrlResponse(BaseModel):

    response: str = Field()
