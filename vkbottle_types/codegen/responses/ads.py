import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class AdsAddOfficeUsersResponseModel(BaseModel):

    response: typing.List[bool] = Field()


class AdsAddOfficeUsersResponse(BaseResponse):
    response: "AdsAddOfficeUsersResponseModel"


class AdsCheckLinkResponseModel(BaseModel):

    response: "AdsLinkStatus" = Field()


class AdsCheckLinkResponse(BaseResponse):
    response: "AdsCheckLinkResponseModel"


class AdsCreateAdsResponseModel(BaseModel):

    response: typing.List[AdsCreateAdStatus] = Field()


class AdsCreateAdsResponse(BaseResponse):
    response: "AdsCreateAdsResponseModel"


class AdsCreateCampaignsResponseModel(BaseModel):

    response: typing.List[AdsCreateCampaignStatus] = Field()


class AdsCreateCampaignsResponse(BaseResponse):
    response: "AdsCreateCampaignsResponseModel"


class AdsCreateClientsResponseModel(BaseModel):

    response: typing.List[AdsCreateClientsStatus] = Field()


class AdsCreateClientsResponse(BaseResponse):
    response: "AdsCreateClientsResponseModel"


class AdsCreateLookalikeRequestResponseModel(BaseModel):

    response: dict = Field()


class AdsCreateLookalikeRequestResponse(BaseResponse):
    response: "AdsCreateLookalikeRequestResponseModel"


class AdsCreateTargetGroupResponseModel(BaseModel):

    response: dict = Field()


class AdsCreateTargetGroupResponse(BaseResponse):
    response: "AdsCreateTargetGroupResponseModel"


class AdsCreateTargetPixelResponseModel(BaseModel):

    response: dict = Field()


class AdsCreateTargetPixelResponse(BaseResponse):
    response: "AdsCreateTargetPixelResponseModel"


class AdsDeleteAdsResponseModel(BaseModel):

    response: typing.List[int] = Field()


class AdsDeleteAdsResponse(BaseResponse):
    response: "AdsDeleteAdsResponseModel"


class AdsDeleteCampaignsResponseModel(BaseModel):

    response: typing.List[int] = Field()


class AdsDeleteCampaignsResponse(BaseResponse):
    response: "AdsDeleteCampaignsResponseModel"


class AdsDeleteClientsResponseModel(BaseModel):

    response: typing.List[int] = Field()


class AdsDeleteClientsResponse(BaseResponse):
    response: "AdsDeleteClientsResponseModel"


class AdsGetAccountsResponseModel(BaseModel):

    response: typing.List[AdsAccount] = Field()


class AdsGetAccountsResponse(BaseResponse):
    response: "AdsGetAccountsResponseModel"


class AdsGetAdsLayoutResponseModel(BaseModel):

    response: typing.List[AdsAdLayout] = Field()


class AdsGetAdsLayoutResponse(BaseResponse):
    response: "AdsGetAdsLayoutResponseModel"


class AdsGetAdsTargetingResponseModel(BaseModel):

    response: typing.List[AdsTargSettings] = Field()


class AdsGetAdsTargetingResponse(BaseResponse):
    response: "AdsGetAdsTargetingResponseModel"


class AdsGetAdsResponseModel(BaseModel):

    response: typing.List[AdsAd] = Field()


class AdsGetAdsResponse(BaseResponse):
    response: "AdsGetAdsResponseModel"


class AdsGetBudgetResponseModel(BaseModel):

    response: str = Field(
        description="Budget",
    )


class AdsGetBudgetResponse(BaseResponse):
    response: "AdsGetBudgetResponseModel"


class AdsGetCampaignsResponseModel(BaseModel):

    response: typing.List[AdsCampaign] = Field()


class AdsGetCampaignsResponse(BaseResponse):
    response: "AdsGetCampaignsResponseModel"


class AdsGetCategoriesResponseModel(BaseModel):

    response: dict = Field()


class AdsGetCategoriesResponse(BaseResponse):
    response: "AdsGetCategoriesResponseModel"


class AdsGetClientsResponseModel(BaseModel):

    response: typing.List[AdsClient] = Field()


class AdsGetClientsResponse(BaseResponse):
    response: "AdsGetClientsResponseModel"


class AdsGetDemographicsResponseModel(BaseModel):

    response: typing.List[AdsDemoStats] = Field()


class AdsGetDemographicsResponse(BaseResponse):
    response: "AdsGetDemographicsResponseModel"


class AdsGetFloodStatsResponseModel(BaseModel):

    response: "AdsFloodStats" = Field()


class AdsGetFloodStatsResponse(BaseResponse):
    response: "AdsGetFloodStatsResponseModel"


class AdsGetLookalikeRequestsResponseModel(BaseModel):

    response: dict = Field()


class AdsGetLookalikeRequestsResponse(BaseResponse):
    response: "AdsGetLookalikeRequestsResponseModel"


class AdsGetMusiciansResponseModel(BaseModel):

    response: dict = Field()


class AdsGetMusiciansResponse(BaseResponse):
    response: "AdsGetMusiciansResponseModel"


class AdsGetOfficeUsersResponseModel(BaseModel):

    response: typing.List[AdsUsers] = Field()


class AdsGetOfficeUsersResponse(BaseResponse):
    response: "AdsGetOfficeUsersResponseModel"


class AdsGetPostsReachResponseModel(BaseModel):

    response: typing.List[AdsPromotedPostReach] = Field()


class AdsGetPostsReachResponse(BaseResponse):
    response: "AdsGetPostsReachResponseModel"


class AdsGetRejectionReasonResponseModel(BaseModel):

    response: "AdsRejectReason" = Field()


class AdsGetRejectionReasonResponse(BaseResponse):
    response: "AdsGetRejectionReasonResponseModel"


class AdsGetStatisticsResponseModel(BaseModel):

    response: typing.List[AdsStats] = Field()


class AdsGetStatisticsResponse(BaseResponse):
    response: "AdsGetStatisticsResponseModel"


class AdsGetSuggestionsCitiesResponseModel(BaseModel):

    response: typing.List[AdsTargSuggestionsCities] = Field()


class AdsGetSuggestionsCitiesResponse(BaseResponse):
    response: "AdsGetSuggestionsCitiesResponseModel"


class AdsGetSuggestionsRegionsResponseModel(BaseModel):

    response: typing.List[AdsTargSuggestionsRegions] = Field()


class AdsGetSuggestionsRegionsResponse(BaseResponse):
    response: "AdsGetSuggestionsRegionsResponseModel"


class AdsGetSuggestionsResponseModel(BaseModel):

    response: typing.List[AdsTargSuggestions] = Field()


class AdsGetSuggestionsResponse(BaseResponse):
    response: "AdsGetSuggestionsResponseModel"


class AdsGetSuggestionsSchoolsResponseModel(BaseModel):

    response: typing.List[AdsTargSuggestionsSchools] = Field()


class AdsGetSuggestionsSchoolsResponse(BaseResponse):
    response: "AdsGetSuggestionsSchoolsResponseModel"


class AdsGetTargetGroupsResponseModel(BaseModel):

    response: typing.List[AdsTargetGroup] = Field()


class AdsGetTargetGroupsResponse(BaseResponse):
    response: "AdsGetTargetGroupsResponseModel"


class AdsGetTargetPixelsResponseModel(BaseModel):

    response: typing.List[AdsTargetPixelInfo] = Field()


class AdsGetTargetPixelsResponse(BaseResponse):
    response: "AdsGetTargetPixelsResponseModel"


class AdsGetTargetingStatsResponseModel(BaseModel):

    response: "AdsTargStats" = Field()


class AdsGetTargetingStatsResponse(BaseResponse):
    response: "AdsGetTargetingStatsResponseModel"


class AdsGetUploadURLResponseModel(BaseModel):

    response: str = Field(
        description="Photo upload URL",
    )


class AdsGetUploadURLResponse(BaseResponse):
    response: "AdsGetUploadURLResponseModel"


class AdsGetVideoUploadURLResponseModel(BaseModel):

    response: str = Field(
        description="Video upload URL",
    )


class AdsGetVideoUploadURLResponse(BaseResponse):
    response: "AdsGetVideoUploadURLResponseModel"


class AdsImportTargetContactsResponseModel(BaseModel):

    response: int = Field(
        description="Imported contacts number",
    )


class AdsImportTargetContactsResponse(BaseResponse):
    response: "AdsImportTargetContactsResponseModel"


class AdsRemoveOfficeUsersResponseModel(BaseModel):

    response: typing.List[bool] = Field()


class AdsRemoveOfficeUsersResponse(BaseResponse):
    response: "AdsRemoveOfficeUsersResponseModel"


class AdsRemoveTargetContactsResponseModel(BaseModel):

    response: dict = Field()


class AdsRemoveTargetContactsResponse(BaseResponse):
    response: "AdsRemoveTargetContactsResponseModel"


class AdsSaveLookalikeRequestResultResponseModel(BaseModel):

    response: dict = Field()


class AdsSaveLookalikeRequestResultResponse(BaseResponse):
    response: "AdsSaveLookalikeRequestResultResponseModel"


class AdsShareTargetGroupResponseModel(BaseModel):

    response: dict = Field()


class AdsShareTargetGroupResponse(BaseResponse):
    response: "AdsShareTargetGroupResponseModel"


class AdsUpdateAdsResponseModel(BaseModel):

    response: typing.List[AdsUpdateAdsStatus] = Field()


class AdsUpdateAdsResponse(BaseResponse):
    response: "AdsUpdateAdsResponseModel"


class AdsUpdateCampaignsResponseModel(BaseModel):

    response: typing.List[AdsCreateCampaignStatus] = Field()


class AdsUpdateCampaignsResponse(BaseResponse):
    response: "AdsUpdateCampaignsResponseModel"


class AdsUpdateClientsResponseModel(BaseModel):

    response: typing.List[AdsUpdateClientsStatus] = Field()


class AdsUpdateClientsResponse(BaseResponse):
    response: "AdsUpdateClientsResponseModel"


class AdsUpdateOfficeUsersResponseModel(BaseModel):

    response: typing.List[AdsUpdateOfficeUsersResult] = Field()


class AdsUpdateOfficeUsersResponse(BaseResponse):
    response: "AdsUpdateOfficeUsersResponseModel"
