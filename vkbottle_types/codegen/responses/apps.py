import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class AppsAddSnippetResponseModel(BaseModel):

    response: dict = Field()


class AppsAddSnippetResponse(BaseResponse):
    response: "AppsAddSnippetResponseModel"


class AppsCreatedGroupResponseModel(BaseModel):

    response: dict = Field()


class AppsCreatedGroupResponse(BaseResponse):
    response: "AppsCreatedGroupResponseModel"


class AppsGetCatalogResponseModel(BaseModel):

    response: "AppsCatalogList" = Field()


class AppsGetCatalogResponse(BaseResponse):
    response: "AppsGetCatalogResponseModel"


class AppsGetFriendsListExtendedResponseModel(BaseModel):

    response: dict = Field()


class AppsGetFriendsListExtendedResponse(BaseResponse):
    response: "AppsGetFriendsListExtendedResponseModel"


class AppsGetFriendsListResponseModel(BaseModel):

    response: dict = Field()


class AppsGetFriendsListResponse(BaseResponse):
    response: "AppsGetFriendsListResponseModel"


class AppsGetLeaderboardExtendedResponseModel(BaseModel):

    response: dict = Field()


class AppsGetLeaderboardExtendedResponse(BaseResponse):
    response: "AppsGetLeaderboardExtendedResponseModel"


class AppsGetLeaderboardResponseModel(BaseModel):

    response: dict = Field()


class AppsGetLeaderboardResponse(BaseResponse):
    response: "AppsGetLeaderboardResponseModel"


class AppsGetMiniAppPoliciesResponseModel(BaseModel):

    response: dict = Field()


class AppsGetMiniAppPoliciesResponse(BaseResponse):
    response: "AppsGetMiniAppPoliciesResponseModel"


class AppsGetScopesResponseModel(BaseModel):

    response: dict = Field()


class AppsGetScopesResponse(BaseResponse):
    response: "AppsGetScopesResponseModel"


class AppsGetScoreResponseModel(BaseModel):

    response: int = Field(
        description="Score number",
    )


class AppsGetScoreResponse(BaseResponse):
    response: "AppsGetScoreResponseModel"


class AppsGetSnippetsResponseModel(BaseModel):

    response: dict = Field()


class AppsGetSnippetsResponse(BaseResponse):
    response: "AppsGetSnippetsResponseModel"


class AppsGetTestingGroupsResponseModel(BaseModel):

    response: typing.List[AppsTestingGroup] = Field()


class AppsGetTestingGroupsResponse(BaseResponse):
    response: "AppsGetTestingGroupsResponseModel"


class AppsGetResponseModel(BaseModel):

    response: dict = Field()


class AppsGetResponse(BaseResponse):
    response: "AppsGetResponseModel"


class AppsImageUploadResponseModel(BaseModel):

    response: dict = Field()


class AppsImageUploadResponse(BaseResponse):
    response: "AppsImageUploadResponseModel"


class AppsIsNotificationsAllowedResponseModel(BaseModel):

    response: dict = Field()


class AppsIsNotificationsAllowedResponse(BaseResponse):
    response: "AppsIsNotificationsAllowedResponseModel"


class AppsSendRequestResponseModel(BaseModel):

    response: int = Field(
        description="Request ID",
    )


class AppsSendRequestResponse(BaseResponse):
    response: "AppsSendRequestResponseModel"
