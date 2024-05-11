import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class NewsfeedGenericResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGenericResponse(BaseResponse):
    response: "NewsfeedGenericResponseModel"


class NewsfeedGetBannedExtendedResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGetBannedExtendedResponse(BaseResponse):
    response: "NewsfeedGetBannedExtendedResponseModel"


class NewsfeedGetBannedResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGetBannedResponse(BaseResponse):
    response: "NewsfeedGetBannedResponseModel"


class NewsfeedGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGetCommentsResponse(BaseResponse):
    response: "NewsfeedGetCommentsResponseModel"


class NewsfeedGetListsExtendedResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGetListsExtendedResponse(BaseResponse):
    response: "NewsfeedGetListsExtendedResponseModel"


class NewsfeedGetListsResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGetListsResponse(BaseResponse):
    response: "NewsfeedGetListsResponseModel"


class NewsfeedGetMentionsResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGetMentionsResponse(BaseResponse):
    response: "NewsfeedGetMentionsResponseModel"


class NewsfeedGetSuggestedSourcesResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedGetSuggestedSourcesResponse(BaseResponse):
    response: "NewsfeedGetSuggestedSourcesResponseModel"


class NewsfeedIgnoreItemResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedIgnoreItemResponse(BaseResponse):
    response: "NewsfeedIgnoreItemResponseModel"


class NewsfeedSaveListResponseModel(BaseModel):

    response: int = Field(
        description="List ID",
    )


class NewsfeedSaveListResponse(BaseResponse):
    response: "NewsfeedSaveListResponseModel"


class NewsfeedSearchExtendedResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedSearchExtendedResponse(BaseResponse):
    response: "NewsfeedSearchExtendedResponseModel"


class NewsfeedSearchExtendedStrictResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedSearchExtendedStrictResponse(BaseResponse):
    response: "NewsfeedSearchExtendedStrictResponseModel"


class NewsfeedSearchResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedSearchResponse(BaseResponse):
    response: "NewsfeedSearchResponseModel"


class NewsfeedSearchStrictResponseModel(BaseModel):

    response: dict = Field()


class NewsfeedSearchStrictResponse(BaseResponse):
    response: "NewsfeedSearchStrictResponseModel"
