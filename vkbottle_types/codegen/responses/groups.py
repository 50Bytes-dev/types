import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class GroupsAddAddressResponseModel(BaseModel):

    response: "GroupsAddress" = Field()


class GroupsAddAddressResponse(BaseResponse):
    response: "GroupsAddAddressResponseModel"


class GroupsAddCallbackServerResponseModel(BaseModel):

    response: dict = Field()


class GroupsAddCallbackServerResponse(BaseResponse):
    response: "GroupsAddCallbackServerResponseModel"


class GroupsAddLinkResponseModel(BaseModel):

    response: "GroupsLinksItem" = Field()


class GroupsAddLinkResponse(BaseResponse):
    response: "GroupsAddLinkResponseModel"


class GroupsCreateResponseModel(BaseModel):

    response: "GroupsGroupFull" = Field()


class GroupsCreateResponse(BaseResponse):
    response: "GroupsCreateResponseModel"


class GroupsEditAddressResponseModel(BaseModel):

    response: "GroupsAddress" = Field(
        description="Result",
    )


class GroupsEditAddressResponse(BaseResponse):
    response: "GroupsEditAddressResponseModel"


class GroupsGetAddressesResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetAddressesResponse(BaseResponse):
    response: "GroupsGetAddressesResponseModel"


class GroupsGetBannedResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetBannedResponse(BaseResponse):
    response: "GroupsGetBannedResponseModel"


class GroupsGetByIdObjectResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetByIdObjectResponse(BaseResponse):
    response: "GroupsGetByIdObjectResponseModel"


class GroupsGetCallbackConfirmationCodeResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetCallbackConfirmationCodeResponse(BaseResponse):
    response: "GroupsGetCallbackConfirmationCodeResponseModel"


class GroupsGetCallbackServersResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetCallbackServersResponse(BaseResponse):
    response: "GroupsGetCallbackServersResponseModel"


class GroupsGetCallbackSettingsResponseModel(BaseModel):

    response: "GroupsCallbackSettings" = Field()


class GroupsGetCallbackSettingsResponse(BaseResponse):
    response: "GroupsGetCallbackSettingsResponseModel"


class GroupsGetCatalogInfoExtendedResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetCatalogInfoExtendedResponse(BaseResponse):
    response: "GroupsGetCatalogInfoExtendedResponseModel"


class GroupsGetCatalogInfoResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetCatalogInfoResponse(BaseResponse):
    response: "GroupsGetCatalogInfoResponseModel"


class GroupsGetInvitedUsersResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetInvitedUsersResponse(BaseResponse):
    response: "GroupsGetInvitedUsersResponseModel"


class GroupsGetInvitesExtendedResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetInvitesExtendedResponse(BaseResponse):
    response: "GroupsGetInvitesExtendedResponseModel"


class GroupsGetInvitesResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetInvitesResponse(BaseResponse):
    response: "GroupsGetInvitesResponseModel"


class GroupsGetLongPollServerResponseModel(BaseModel):

    response: "GroupsLongPollServer" = Field()


class GroupsGetLongPollServerResponse(BaseResponse):
    response: "GroupsGetLongPollServerResponseModel"


class GroupsGetLongPollSettingsResponseModel(BaseModel):

    response: "GroupsLongPollSettings" = Field()


class GroupsGetLongPollSettingsResponse(BaseResponse):
    response: "GroupsGetLongPollSettingsResponseModel"


class GroupsGetMembersFieldsResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetMembersFieldsResponse(BaseResponse):
    response: "GroupsGetMembersFieldsResponseModel"


class GroupsGetMembersFilterResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetMembersFilterResponse(BaseResponse):
    response: "GroupsGetMembersFilterResponseModel"


class GroupsGetMembersResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetMembersResponse(BaseResponse):
    response: "GroupsGetMembersResponseModel"


class GroupsGetOnlineStatusResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetOnlineStatusResponse(BaseResponse):
    response: "GroupsGetOnlineStatusResponseModel"


class GroupsGetRequestsFieldsResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetRequestsFieldsResponse(BaseResponse):
    response: "GroupsGetRequestsFieldsResponseModel"


class GroupsGetRequestsResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetRequestsResponse(BaseResponse):
    response: "GroupsGetRequestsResponseModel"


class GroupsGetSettingsResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetSettingsResponse(BaseResponse):
    response: "GroupsGetSettingsResponseModel"


class GroupsGetTagListResponseModel(BaseModel):

    response: typing.List[GroupsGroupTag] = Field()


class GroupsGetTagListResponse(BaseResponse):
    response: "GroupsGetTagListResponseModel"


class GroupsGetTokenPermissionsResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetTokenPermissionsResponse(BaseResponse):
    response: "GroupsGetTokenPermissionsResponseModel"


class GroupsGetObjectExtendedResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetObjectExtendedResponse(BaseResponse):
    response: "GroupsGetObjectExtendedResponseModel"


class GroupsGetResponseModel(BaseModel):

    response: dict = Field()


class GroupsGetResponse(BaseResponse):
    response: "GroupsGetResponseModel"


class GroupsInviteUserIdsListResponseModel(BaseModel):

    response: dict = Field()


class GroupsInviteUserIdsListResponse(BaseResponse):
    response: "GroupsInviteUserIdsListResponseModel"


class GroupsIsMemberExtendedResponseModel(BaseModel):

    response: dict = Field()


class GroupsIsMemberExtendedResponse(BaseResponse):
    response: "GroupsIsMemberExtendedResponseModel"


class GroupsIsMemberUserIdsExtendedResponseModel(BaseModel):

    response: typing.List[GroupsMemberStatusFull] = Field()


class GroupsIsMemberUserIdsExtendedResponse(BaseResponse):
    response: "GroupsIsMemberUserIdsExtendedResponseModel"


class GroupsIsMemberUserIdsResponseModel(BaseModel):

    response: typing.List[GroupsMemberStatus] = Field()


class GroupsIsMemberUserIdsResponse(BaseResponse):
    response: "GroupsIsMemberUserIdsResponseModel"


class GroupsSearchResponseModel(BaseModel):

    response: dict = Field()


class GroupsSearchResponse(BaseResponse):
    response: "GroupsSearchResponseModel"
