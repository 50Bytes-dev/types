import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class MessagesAddChatUsersResponseModel(BaseModel):

    response: dict = Field()


class MessagesAddChatUsersResponse(BaseResponse):
    response: "MessagesAddChatUsersResponseModel"


class MessagesCreateChatWithPeerIdsResponseModel(BaseModel):

    response: dict = Field()


class MessagesCreateChatWithPeerIdsResponse(BaseResponse):
    response: "MessagesCreateChatWithPeerIdsResponseModel"


class MessagesDeleteChatPhotoResponseModel(BaseModel):

    response: dict = Field()


class MessagesDeleteChatPhotoResponse(BaseResponse):
    response: "MessagesDeleteChatPhotoResponseModel"


class MessagesDeleteConversationResponseModel(BaseModel):

    response: dict = Field()


class MessagesDeleteConversationResponse(BaseResponse):
    response: "MessagesDeleteConversationResponseModel"


class MessagesDeleteFullResponseModel(BaseModel):

    response: typing.List[MessagesDeleteFullResponseItem] = Field()


class MessagesDeleteFullResponse(BaseResponse):
    response: "MessagesDeleteFullResponseModel"


class MessagesGetByConversationMessageIdExtendedResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetByConversationMessageIdExtendedResponse(BaseResponse):
    response: "MessagesGetByConversationMessageIdExtendedResponseModel"


class MessagesGetByConversationMessageIdResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetByConversationMessageIdResponse(BaseResponse):
    response: "MessagesGetByConversationMessageIdResponseModel"


class MessagesGetByIdExtendedResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetByIdExtendedResponse(BaseResponse):
    response: "MessagesGetByIdExtendedResponseModel"


class MessagesGetByIdResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetByIdResponse(BaseResponse):
    response: "MessagesGetByIdResponseModel"


class MessagesGetChatPreviewResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetChatPreviewResponse(BaseResponse):
    response: "MessagesGetChatPreviewResponseModel"


class MessagesGetChatChatIdsFieldsResponseModel(BaseModel):

    response: typing.List[MessagesChatFull] = Field()


class MessagesGetChatChatIdsFieldsResponse(BaseResponse):
    response: "MessagesGetChatChatIdsFieldsResponseModel"


class MessagesGetChatChatIdsResponseModel(BaseModel):

    response: typing.List[MessagesChat] = Field()


class MessagesGetChatChatIdsResponse(BaseResponse):
    response: "MessagesGetChatChatIdsResponseModel"


class MessagesGetChatFieldsResponseModel(BaseModel):

    response: "MessagesChatFull" = Field()


class MessagesGetChatFieldsResponse(BaseResponse):
    response: "MessagesGetChatFieldsResponseModel"


class MessagesGetChatResponseModel(BaseModel):

    response: "MessagesChat" = Field()


class MessagesGetChatResponse(BaseResponse):
    response: "MessagesGetChatResponseModel"


class MessagesGetConversationMembersResponseModel(BaseModel):

    response: "MessagesGetConversationMembers" = Field()


class MessagesGetConversationMembersResponse(BaseResponse):
    response: "MessagesGetConversationMembersResponseModel"


class MessagesGetConversationsByIdExtendedResponseModel(BaseModel):

    response: "MessagesGetConversationByIdExtended" = Field()


class MessagesGetConversationsByIdExtendedResponse(BaseResponse):
    response: "MessagesGetConversationsByIdExtendedResponseModel"


class MessagesGetConversationsByIdResponseModel(BaseModel):

    response: "MessagesGetConversationById" = Field()


class MessagesGetConversationsByIdResponse(BaseResponse):
    response: "MessagesGetConversationsByIdResponseModel"


class MessagesGetConversationsResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetConversationsResponse(BaseResponse):
    response: "MessagesGetConversationsResponseModel"


class MessagesGetHistoryAttachmentsResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetHistoryAttachmentsResponse(BaseResponse):
    response: "MessagesGetHistoryAttachmentsResponseModel"


class MessagesGetHistoryExtendedResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetHistoryExtendedResponse(BaseResponse):
    response: "MessagesGetHistoryExtendedResponseModel"


class MessagesGetHistoryResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetHistoryResponse(BaseResponse):
    response: "MessagesGetHistoryResponseModel"


class MessagesGetImportantMessagesExtendedResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetImportantMessagesExtendedResponse(BaseResponse):
    response: "MessagesGetImportantMessagesExtendedResponseModel"


class MessagesGetImportantMessagesResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetImportantMessagesResponse(BaseResponse):
    response: "MessagesGetImportantMessagesResponseModel"


class MessagesGetIntentUsersResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetIntentUsersResponse(BaseResponse):
    response: "MessagesGetIntentUsersResponseModel"


class MessagesGetInviteLinkByOwnerResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetInviteLinkByOwnerResponse(BaseResponse):
    response: "MessagesGetInviteLinkByOwnerResponseModel"


class MessagesGetInviteLinkResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetInviteLinkResponse(BaseResponse):
    response: "MessagesGetInviteLinkResponseModel"


class MessagesGetLastActivityResponseModel(BaseModel):

    response: "MessagesLastActivity" = Field()


class MessagesGetLastActivityResponse(BaseResponse):
    response: "MessagesGetLastActivityResponseModel"


class MessagesGetLongPollHistoryResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetLongPollHistoryResponse(BaseResponse):
    response: "MessagesGetLongPollHistoryResponseModel"


class MessagesGetLongPollServerResponseModel(BaseModel):

    response: "MessagesLongpollParams" = Field()


class MessagesGetLongPollServerResponse(BaseResponse):
    response: "MessagesGetLongPollServerResponseModel"


class MessagesGetMessagesReactionsResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetMessagesReactionsResponse(BaseResponse):
    response: "MessagesGetMessagesReactionsResponseModel"


class MessagesGetReactedPeersResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetReactedPeersResponse(BaseResponse):
    response: "MessagesGetReactedPeersResponseModel"


class MessagesGetReactionsAssetsResponseModel(BaseModel):

    response: dict = Field()


class MessagesGetReactionsAssetsResponse(BaseResponse):
    response: "MessagesGetReactionsAssetsResponseModel"


class MessagesIsMessagesFromGroupAllowedResponseModel(BaseModel):

    response: dict = Field()


class MessagesIsMessagesFromGroupAllowedResponse(BaseResponse):
    response: "MessagesIsMessagesFromGroupAllowedResponseModel"


class MessagesJoinChatByInviteLinkResponseModel(BaseModel):

    response: dict = Field()


class MessagesJoinChatByInviteLinkResponse(BaseResponse):
    response: "MessagesJoinChatByInviteLinkResponseModel"


class MessagesMarkAsImportantDeprecatedResponseModel(BaseModel):

    response: typing.List[int] = Field()


class MessagesMarkAsImportantDeprecatedResponse(BaseResponse):
    response: "MessagesMarkAsImportantDeprecatedResponseModel"


class MessagesPinResponseModel(BaseModel):

    response: "MessagesPinnedMessage" = Field()


class MessagesPinResponse(BaseResponse):
    response: "MessagesPinResponseModel"


class MessagesSearchConversationsExtendedResponseModel(BaseModel):

    response: dict = Field()


class MessagesSearchConversationsExtendedResponse(BaseResponse):
    response: "MessagesSearchConversationsExtendedResponseModel"


class MessagesSearchConversationsResponseModel(BaseModel):

    response: dict = Field()


class MessagesSearchConversationsResponse(BaseResponse):
    response: "MessagesSearchConversationsResponseModel"


class MessagesSearchExtendedResponseModel(BaseModel):

    response: dict = Field()


class MessagesSearchExtendedResponse(BaseResponse):
    response: "MessagesSearchExtendedResponseModel"


class MessagesSearchResponseModel(BaseModel):

    response: dict = Field()


class MessagesSearchResponse(BaseResponse):
    response: "MessagesSearchResponseModel"


class MessagesSendDeprecatedResponseModel(BaseModel):

    response: int = Field(
        description="Message ID",
    )


class MessagesSendDeprecatedResponse(BaseResponse):
    response: "MessagesSendDeprecatedResponseModel"


class MessagesSendUserIdsResponseModel(BaseModel):

    response: typing.List[MessagesSendUserIdsResponseItem] = Field()


class MessagesSendUserIdsResponse(BaseResponse):
    response: "MessagesSendUserIdsResponseModel"


class MessagesSetChatPhotoResponseModel(BaseModel):

    response: dict = Field()


class MessagesSetChatPhotoResponse(BaseResponse):
    response: "MessagesSetChatPhotoResponseModel"
