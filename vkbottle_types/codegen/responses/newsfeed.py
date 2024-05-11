import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class NewsfeedGenericResponse(BaseModel):

    response: dict = Field()


class NewsfeedGetBannedExtendedResponse(BaseModel):

    response: dict = Field()


class NewsfeedGetBannedResponse(BaseModel):

    response: dict = Field()


class NewsfeedGetCommentsResponse(BaseModel):

    response: dict = Field()


class NewsfeedGetListsExtendedResponse(BaseModel):

    response: dict = Field()


class NewsfeedGetListsResponse(BaseModel):

    response: dict = Field()


class NewsfeedGetMentionsResponse(BaseModel):

    response: dict = Field()


class NewsfeedGetSuggestedSourcesResponse(BaseModel):

    response: dict = Field()


class NewsfeedIgnoreItemResponse(BaseModel):

    response: dict = Field()


class NewsfeedSaveListResponse(BaseModel):

    response: int = Field(
        description="List ID",
    )


class NewsfeedSearchExtendedResponse(BaseModel):

    response: dict = Field()


class NewsfeedSearchExtendedStrictResponse(BaseModel):

    response: dict = Field()


class NewsfeedSearchResponse(BaseModel):

    response: dict = Field()


class NewsfeedSearchStrictResponse(BaseModel):

    response: dict = Field()
