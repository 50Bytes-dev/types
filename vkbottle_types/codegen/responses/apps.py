import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class AppsAddSnippetResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsCreatedGroupResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetCatalogResponse(BaseModel):
    
    
    response: 'AppsCatalogList' = Field(
        
        
        
    )
    
    







class AppsGetFriendsListExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetFriendsListResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetLeaderboardExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetLeaderboardResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetMiniAppPoliciesResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetScopesResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetScoreResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Score number",
        
        
    )
    
    







class AppsGetSnippetsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsGetTestingGroupsResponse(BaseModel):
    
    
    response: typing.List[AppsTestingGroup] = Field(
        
        
        
    )
    
    







class AppsGetResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsImageUploadResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsIsNotificationsAllowedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppsSendRequestResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Request ID",
        
        
    )
    
    



