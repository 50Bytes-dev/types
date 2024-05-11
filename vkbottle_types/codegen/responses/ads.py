import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class AdsAddOfficeUsersResponse(BaseModel):
    
    
    response: typing.List[bool] = Field(
        
        
        
    )
    
    







class AdsCheckLinkResponse(BaseModel):
    
    
    response: 'AdsLinkStatus' = Field(
        
        
        
    )
    
    







class AdsCreateAdsResponse(BaseModel):
    
    
    response: typing.List[AdsCreateAdStatus] = Field(
        
        
        
    )
    
    







class AdsCreateCampaignsResponse(BaseModel):
    
    
    response: typing.List[AdsCreateCampaignStatus] = Field(
        
        
        
    )
    
    







class AdsCreateClientsResponse(BaseModel):
    
    
    response: typing.List[AdsCreateClientsStatus] = Field(
        
        
        
    )
    
    







class AdsCreateLookalikeRequestResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsCreateTargetGroupResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsCreateTargetPixelResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsDeleteAdsResponse(BaseModel):
    
    
    response: typing.List[int] = Field(
        
        
        
    )
    
    







class AdsDeleteCampaignsResponse(BaseModel):
    
    
    response: typing.List[int] = Field(
        
        
        
    )
    
    







class AdsDeleteClientsResponse(BaseModel):
    
    
    response: typing.List[int] = Field(
        
        
        
    )
    
    







class AdsGetAccountsResponse(BaseModel):
    
    
    response: typing.List[AdsAccount] = Field(
        
        
        
    )
    
    







class AdsGetAdsLayoutResponse(BaseModel):
    
    
    response: typing.List[AdsAdLayout] = Field(
        
        
        
    )
    
    







class AdsGetAdsTargetingResponse(BaseModel):
    
    
    response: typing.List[AdsTargSettings] = Field(
        
        
        
    )
    
    







class AdsGetAdsResponse(BaseModel):
    
    
    response: typing.List[AdsAd] = Field(
        
        
        
    )
    
    







class AdsGetBudgetResponse(BaseModel):
    
    
    response: str = Field(
        
        
        description="Budget",
        
        
    )
    
    







class AdsGetCampaignsResponse(BaseModel):
    
    
    response: typing.List[AdsCampaign] = Field(
        
        
        
    )
    
    







class AdsGetCategoriesResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsGetClientsResponse(BaseModel):
    
    
    response: typing.List[AdsClient] = Field(
        
        
        
    )
    
    







class AdsGetDemographicsResponse(BaseModel):
    
    
    response: typing.List[AdsDemoStats] = Field(
        
        
        
    )
    
    







class AdsGetFloodStatsResponse(BaseModel):
    
    
    response: 'AdsFloodStats' = Field(
        
        
        
    )
    
    







class AdsGetLookalikeRequestsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsGetMusiciansResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsGetOfficeUsersResponse(BaseModel):
    
    
    response: typing.List[AdsUsers] = Field(
        
        
        
    )
    
    







class AdsGetPostsReachResponse(BaseModel):
    
    
    response: typing.List[AdsPromotedPostReach] = Field(
        
        
        
    )
    
    







class AdsGetRejectionReasonResponse(BaseModel):
    
    
    response: 'AdsRejectReason' = Field(
        
        
        
    )
    
    







class AdsGetStatisticsResponse(BaseModel):
    
    
    response: typing.List[AdsStats] = Field(
        
        
        
    )
    
    







class AdsGetSuggestionsCitiesResponse(BaseModel):
    
    
    response: typing.List[AdsTargSuggestionsCities] = Field(
        
        
        
    )
    
    







class AdsGetSuggestionsRegionsResponse(BaseModel):
    
    
    response: typing.List[AdsTargSuggestionsRegions] = Field(
        
        
        
    )
    
    







class AdsGetSuggestionsResponse(BaseModel):
    
    
    response: typing.List[AdsTargSuggestions] = Field(
        
        
        
    )
    
    







class AdsGetSuggestionsSchoolsResponse(BaseModel):
    
    
    response: typing.List[AdsTargSuggestionsSchools] = Field(
        
        
        
    )
    
    







class AdsGetTargetGroupsResponse(BaseModel):
    
    
    response: typing.List[AdsTargetGroup] = Field(
        
        
        
    )
    
    







class AdsGetTargetPixelsResponse(BaseModel):
    
    
    response: typing.List[AdsTargetPixelInfo] = Field(
        
        
        
    )
    
    







class AdsGetTargetingStatsResponse(BaseModel):
    
    
    response: 'AdsTargStats' = Field(
        
        
        
    )
    
    







class AdsGetUploadURLResponse(BaseModel):
    
    
    response: str = Field(
        
        
        description="Photo upload URL",
        
        
    )
    
    







class AdsGetVideoUploadURLResponse(BaseModel):
    
    
    response: str = Field(
        
        
        description="Video upload URL",
        
        
    )
    
    







class AdsImportTargetContactsResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Imported contacts number",
        
        
    )
    
    







class AdsRemoveOfficeUsersResponse(BaseModel):
    
    
    response: typing.List[bool] = Field(
        
        
        
    )
    
    







class AdsRemoveTargetContactsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsSaveLookalikeRequestResultResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsShareTargetGroupResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AdsUpdateAdsResponse(BaseModel):
    
    
    response: typing.List[AdsUpdateAdsStatus] = Field(
        
        
        
    )
    
    







class AdsUpdateCampaignsResponse(BaseModel):
    
    
    response: typing.List[AdsCreateCampaignStatus] = Field(
        
        
        
    )
    
    







class AdsUpdateClientsResponse(BaseModel):
    
    
    response: typing.List[AdsUpdateClientsStatus] = Field(
        
        
        
    )
    
    







class AdsUpdateOfficeUsersResponse(BaseModel):
    
    
    response: typing.List[AdsUpdateOfficeUsersResult] = Field(
        
        
        
    )
    
    



