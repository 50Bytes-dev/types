import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class GroupsAddAddressResponse(BaseModel):

    response: "GroupsAddress" = Field()


class GroupsAddCallbackServerResponse(BaseModel):

    response: dict = Field()


class GroupsAddLinkResponse(BaseModel):

    response: "GroupsLinksItem" = Field()


class GroupsCreateResponse(BaseModel):

    response: "GroupsGroupFull" = Field()


class GroupsEditAddressResponse(BaseModel):

    response: "GroupsAddress" = Field(
        description="Result",
    )


class GroupsGetAddressesResponse(BaseModel):

    response: dict = Field()


class GroupsGetBannedResponse(BaseModel):

    response: dict = Field()


class GroupsGetByIdObjectResponse(BaseModel):

    response: dict = Field()


class GroupsGetCallbackConfirmationCodeResponse(BaseModel):

    response: dict = Field()


class GroupsGetCallbackServersResponse(BaseModel):

    response: dict = Field()


class GroupsGetCallbackSettingsResponse(BaseModel):

    response: "GroupsCallbackSettings" = Field()


class GroupsGetCatalogInfoExtendedResponse(BaseModel):

    response: dict = Field()


class GroupsGetCatalogInfoResponse(BaseModel):

    response: dict = Field()


class GroupsGetInvitedUsersResponse(BaseModel):

    response: dict = Field()


class GroupsGetInvitesExtendedResponse(BaseModel):

    response: dict = Field()


class GroupsGetInvitesResponse(BaseModel):

    response: dict = Field()


class GroupsGetLongPollServerResponse(BaseModel):

    response: "GroupsLongPollServer" = Field()


class GroupsGetLongPollSettingsResponse(BaseModel):

    response: "GroupsLongPollSettings" = Field()


class GroupsGetMembersFieldsResponse(BaseModel):

    response: dict = Field()


class GroupsGetMembersFilterResponse(BaseModel):

    response: dict = Field()


class GroupsGetMembersResponse(BaseModel):

    response: dict = Field()


class GroupsGetOnlineStatusResponse(BaseModel):

    response: dict = Field()


class GroupsGetRequestsFieldsResponse(BaseModel):

    response: dict = Field()


class GroupsGetRequestsResponse(BaseModel):

    response: dict = Field()


class GroupsGetSettingsResponse(BaseModel):

    response: dict = Field()


class GroupsGetTagListResponse(BaseModel):

    response: typing.List[GroupsGroupTag] = Field()


class GroupsGetTokenPermissionsResponse(BaseModel):

    response: dict = Field()


class GroupsGetObjectExtendedResponse(BaseModel):

    response: dict = Field()


class GroupsGetResponse(BaseModel):

    response: dict = Field()


class GroupsInviteUserIdsListResponse(BaseModel):

    response: dict = Field()


class GroupsIsMemberExtendedResponse(BaseModel):

    response: dict = Field()


class GroupsIsMemberUserIdsExtendedResponse(BaseModel):

    response: typing.List[GroupsMemberStatusFull] = Field()


class GroupsIsMemberUserIdsResponse(BaseModel):

    response: typing.List[GroupsMemberStatus] = Field()


class GroupsSearchResponse(BaseModel):

    response: dict = Field()
