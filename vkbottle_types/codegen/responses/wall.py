import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class WallCreateCommentResponseModel(BaseModel):

    response: dict = Field()


class WallCreateCommentResponse(BaseResponse):
    response: "WallCreateCommentResponseModel"


class WallEditResponseModel(BaseModel):

    response: dict = Field()


class WallEditResponse(BaseResponse):
    response: "WallEditResponseModel"


class WallGetByIdExtendedResponseModel(BaseModel):

    response: dict = Field()


class WallGetByIdExtendedResponse(BaseResponse):
    response: "WallGetByIdExtendedResponseModel"


class WallGetByIdResponseModel(BaseModel):

    response: dict = Field()


class WallGetByIdResponse(BaseResponse):
    response: "WallGetByIdResponseModel"


class WallGetCommentExtendedResponseModel(BaseModel):

    response: dict = Field()


class WallGetCommentExtendedResponse(BaseResponse):
    response: "WallGetCommentExtendedResponseModel"


class WallGetCommentResponseModel(BaseModel):

    response: dict = Field()


class WallGetCommentResponse(BaseResponse):
    response: "WallGetCommentResponseModel"


class WallGetCommentsExtendedResponseModel(BaseModel):

    response: dict = Field()


class WallGetCommentsExtendedResponse(BaseResponse):
    response: "WallGetCommentsExtendedResponseModel"


class WallGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class WallGetCommentsResponse(BaseResponse):
    response: "WallGetCommentsResponseModel"


class WallGetRepostsResponseModel(BaseModel):

    response: dict = Field()


class WallGetRepostsResponse(BaseResponse):
    response: "WallGetRepostsResponseModel"


class WallGetExtendedResponseModel(BaseModel):

    response: dict = Field()


class WallGetExtendedResponse(BaseResponse):
    response: "WallGetExtendedResponseModel"


class WallGetResponseModel(BaseModel):

    response: dict = Field()


class WallGetResponse(BaseResponse):
    response: "WallGetResponseModel"


class WallParseAttachedLinkResponseModel(BaseModel):

    response: dict = Field()


class WallParseAttachedLinkResponse(BaseResponse):
    response: "WallParseAttachedLinkResponseModel"


class WallPostAdsStealthResponseModel(BaseModel):

    response: dict = Field()


class WallPostAdsStealthResponse(BaseResponse):
    response: "WallPostAdsStealthResponseModel"


class WallPostResponseModel(BaseModel):

    response: dict = Field()


class WallPostResponse(BaseResponse):
    response: "WallPostResponseModel"


class WallRepostResponseModel(BaseModel):

    response: dict = Field()


class WallRepostResponse(BaseResponse):
    response: "WallRepostResponseModel"


class WallSearchExtendedResponseModel(BaseModel):

    response: dict = Field()


class WallSearchExtendedResponse(BaseResponse):
    response: "WallSearchExtendedResponseModel"


class WallSearchResponseModel(BaseModel):

    response: dict = Field()


class WallSearchResponse(BaseResponse):
    response: "WallSearchResponseModel"
