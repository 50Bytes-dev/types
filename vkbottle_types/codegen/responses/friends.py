import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class FriendsAddListResponse(BaseModel):

    response: dict = Field()


class FriendsAddResponse(BaseModel):

    response: int = Field(
        description="Friend request status",
    )


class FriendsAreFriendsExtendedResponse(BaseModel):

    response: typing.List[FriendsFriendExtendedStatus] = Field()


class FriendsAreFriendsResponse(BaseModel):

    response: typing.List[FriendsFriendStatus] = Field()


class FriendsDeleteResponse(BaseModel):

    response: dict = Field()


class FriendsGetAppUsersResponse(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetListsResponse(BaseModel):

    response: dict = Field()


class FriendsGetMutualResponse(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetMutualTargetUidsResponse(BaseModel):

    response: typing.List[FriendsMutualFriend] = Field()


class FriendsGetMutualTotalCountResponse(BaseModel):

    response: "FriendsMutualFriend" = Field()


class FriendsGetOnlineExtendedResponse(BaseModel):

    response: "FriendsOnlineUsers" = Field()


class FriendsGetOnlineOnlineMobileExtendedResponse(BaseModel):

    response: "FriendsOnlineUsersWithMobile" = Field()


class FriendsGetOnlineOnlineMobileResponse(BaseModel):

    response: dict = Field()


class FriendsGetOnlineResponse(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetRecentResponse(BaseModel):

    response: typing.List[int] = Field()


class FriendsGetRequestsExtendedResponse(BaseModel):

    response: dict = Field()


class FriendsGetRequestsNeedMutualResponse(BaseModel):

    response: dict = Field()


class FriendsGetRequestsResponse(BaseModel):

    response: dict = Field()


class FriendsGetSuggestionsResponse(BaseModel):

    response: dict = Field()


class FriendsGetFieldsResponse(BaseModel):

    response: dict = Field()


class FriendsGetResponse(BaseModel):

    response: dict = Field()


class FriendsSearchResponse(BaseModel):

    response: dict = Field()
