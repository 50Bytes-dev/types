import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class MessagesAddChatUsersResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesCreateChatWithPeerIdsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesDeleteChatPhotoResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesDeleteConversationResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesDeleteFullResponse(BaseModel):
    
    
    response: typing.List[MessagesDeleteFullResponseItem] = Field(
        
        
        
    )
    
    







class MessagesGetByConversationMessageIdExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetByConversationMessageIdResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetByIdExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetByIdResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetChatPreviewResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetChatChatIdsFieldsResponse(BaseModel):
    
    
    response: typing.List[MessagesChatFull] = Field(
        
        
        
    )
    
    







class MessagesGetChatChatIdsResponse(BaseModel):
    
    
    response: typing.List[MessagesChat] = Field(
        
        
        
    )
    
    







class MessagesGetChatFieldsResponse(BaseModel):
    
    
    response: 'MessagesChatFull' = Field(
        
        
        
    )
    
    







class MessagesGetChatResponse(BaseModel):
    
    
    response: 'MessagesChat' = Field(
        
        
        
    )
    
    







class MessagesGetConversationMembersResponse(BaseModel):
    
    
    response: 'MessagesGetConversationMembers' = Field(
        
        
        
    )
    
    







class MessagesGetConversationsByIdExtendedResponse(BaseModel):
    
    
    response: 'MessagesGetConversationByIdExtended' = Field(
        
        
        
    )
    
    







class MessagesGetConversationsByIdResponse(BaseModel):
    
    
    response: 'MessagesGetConversationById' = Field(
        
        
        
    )
    
    







class MessagesGetConversationsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetHistoryAttachmentsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetHistoryExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetHistoryResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetImportantMessagesExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetImportantMessagesResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetIntentUsersResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetInviteLinkByOwnerResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetInviteLinkResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetLastActivityResponse(BaseModel):
    
    
    response: 'MessagesLastActivity' = Field(
        
        
        
    )
    
    







class MessagesGetLongPollHistoryResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetLongPollServerResponse(BaseModel):
    
    
    response: 'MessagesLongpollParams' = Field(
        
        
        
    )
    
    







class MessagesGetMessagesReactionsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetReactedPeersResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesGetReactionsAssetsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesIsMessagesFromGroupAllowedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesJoinChatByInviteLinkResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesMarkAsImportantDeprecatedResponse(BaseModel):
    
    
    response: typing.List[int] = Field(
        
        
        
    )
    
    







class MessagesPinResponse(BaseModel):
    
    
    response: 'MessagesPinnedMessage' = Field(
        
        
        
    )
    
    







class MessagesSearchConversationsExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesSearchConversationsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesSearchExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesSearchResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class MessagesSendDeprecatedResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Message ID",
        
        
    )
    
    







class MessagesSendUserIdsResponse(BaseModel):
    
    
    response: typing.List[MessagesSendUserIdsResponseItem] = Field(
        
        
        
    )
    
    







class MessagesSetChatPhotoResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



