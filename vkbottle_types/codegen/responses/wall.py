import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class WallCreateCommentResponse(BaseModel):

    response: dict = Field()


class WallEditResponse(BaseModel):

    response: dict = Field()


class WallGetByIdExtendedResponse(BaseModel):

    response: dict = Field()


class WallGetByIdResponse(BaseModel):

    response: dict = Field()


class WallGetCommentExtendedResponse(BaseModel):

    response: dict = Field()


class WallGetCommentResponse(BaseModel):

    response: dict = Field()


class WallGetCommentsExtendedResponse(BaseModel):

    response: dict = Field()


class WallGetCommentsResponse(BaseModel):

    response: dict = Field()


class WallGetRepostsResponse(BaseModel):

    response: dict = Field()


class WallGetExtendedResponse(BaseModel):

    response: dict = Field()


class WallGetResponse(BaseModel):

    response: dict = Field()


class WallParseAttachedLinkResponse(BaseModel):

    response: dict = Field()


class WallPostAdsStealthResponse(BaseModel):

    response: dict = Field()


class WallPostResponse(BaseModel):

    response: dict = Field()


class WallRepostResponse(BaseModel):

    response: dict = Field()


class WallSearchExtendedResponse(BaseModel):

    response: dict = Field()


class WallSearchResponse(BaseModel):

    response: dict = Field()
