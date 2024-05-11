import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class FriendsAddListResponseModel(BaseModel):

    response: dict = Field()


class FriendsAddListResponse(BaseResponse):
    response: "FriendsAddListResponseModel"


class FriendsAddResponseModel(BaseModel):

    response: int = Field(
        description="Friend request status",
    )


class FriendsAddResponse(BaseResponse):
    response: "FriendsAddResponseModel"


class FriendsAreFriendsExtendedResponseModel(BaseModel):

    response: typing.List[FriendsFriendExtendedStatus] = Field()


class FriendsAreFriendsExtendedResponse(BaseResponse):
    response: "FriendsAreFriendsExtendedResponseModel"


class FriendsAreFriendsResponseModel(BaseModel):

    response: typing.List[FriendsFriendStatus] = Field()


class FriendsAreFriendsResponse(BaseResponse):
    response: "FriendsAreFriendsResponseModel"


class FriendsDeleteResponseModel(BaseModel):

    response: dict = Field()


class FriendsDeleteResponse(BaseResponse):
    response: "FriendsDeleteResponseModel"


class FriendsGetAppUsersResponseModel(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetAppUsersResponse(BaseResponse):
    response: "FriendsGetAppUsersResponseModel"


class FriendsGetListsResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetListsResponse(BaseResponse):
    response: "FriendsGetListsResponseModel"


class FriendsGetMutualResponseModel(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetMutualResponse(BaseResponse):
    response: "FriendsGetMutualResponseModel"


class FriendsGetMutualTargetUidsResponseModel(BaseModel):

    response: typing.List[FriendsMutualFriend] = Field()


class FriendsGetMutualTargetUidsResponse(BaseResponse):
    response: "FriendsGetMutualTargetUidsResponseModel"


class FriendsGetMutualTotalCountResponseModel(BaseModel):

    response: "FriendsMutualFriend" = Field()


class FriendsGetMutualTotalCountResponse(BaseResponse):
    response: "FriendsGetMutualTotalCountResponseModel"


class FriendsGetOnlineExtendedResponseModel(BaseModel):

    response: "FriendsOnlineUsers" = Field()


class FriendsGetOnlineExtendedResponse(BaseResponse):
    response: "FriendsGetOnlineExtendedResponseModel"


class FriendsGetOnlineOnlineMobileExtendedResponseModel(BaseModel):

    response: "FriendsOnlineUsersWithMobile" = Field()


class FriendsGetOnlineOnlineMobileExtendedResponse(BaseResponse):
    response: "FriendsGetOnlineOnlineMobileExtendedResponseModel"


class FriendsGetOnlineOnlineMobileResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetOnlineOnlineMobileResponse(BaseResponse):
    response: "FriendsGetOnlineOnlineMobileResponseModel"


class FriendsGetOnlineResponseModel(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetOnlineResponse(BaseResponse):
    response: "FriendsGetOnlineResponseModel"


class FriendsGetRecentResponseModel(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetRecentResponse(BaseResponse):
    response: "FriendsGetRecentResponseModel"


class FriendsGetRequestsExtendedResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetRequestsExtendedResponse(BaseResponse):
    response: "FriendsGetRequestsExtendedResponseModel"


class FriendsGetRequestsNeedMutualResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetRequestsNeedMutualResponse(BaseResponse):
    response: "FriendsGetRequestsNeedMutualResponseModel"


class FriendsGetRequestsResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetRequestsResponse(BaseResponse):
    response: "FriendsGetRequestsResponseModel"


class FriendsGetSuggestionsResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetSuggestionsResponse(BaseResponse):
    response: "FriendsGetSuggestionsResponseModel"


class FriendsGetFieldsResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetFieldsResponse(BaseResponse):
    response: "FriendsGetFieldsResponseModel"


class FriendsGetResponseModel(BaseModel):

    response: dict = Field()


class FriendsGetResponse(BaseResponse):
    response: "FriendsGetResponseModel"


class FriendsSearchResponseModel(BaseModel):

    response: dict = Field()


class FriendsSearchResponse(BaseResponse):
    response: "FriendsSearchResponseModel"
