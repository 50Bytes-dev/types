import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.ads import *
from vkbottle_types.responses.base import *

### OPTIONAL


class AdsCategory(BaseCategory):

    async def add_office_users(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.addOfficeUsers method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.addOfficeUsers", params)

        model = AdsAddOfficeUsersResponse

        return model(**response).response

    async def check_link(
        self,
        account_id: int,
        link_type: str,
        link_url: str,
        campaign_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.checkLink method


        :param account_id: Advertising account ID.
        :param link_type: Object type: *'community' - community,, *'post' - community post,, *'application' - VK application,, *'video' - video,, *'site' - external site.
        :param link_url: Object URL.
        :param campaign_id: Campaign ID
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.checkLink", params)

        model = AdsCheckLinkResponse

        return model(**response).response

    async def create_ads(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.createAds method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.createAds", params)

        model = AdsCreateAdsResponse

        return model(**response).response

    async def create_campaigns(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.createCampaigns method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.createCampaigns", params)

        model = AdsCreateCampaignsResponse

        return model(**response).response

    async def create_clients(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.createClients method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.createClients", params)

        model = AdsCreateClientsResponse

        return model(**response).response

    async def create_lookalike_request(
        self,
        account_id: int,
        source_type: str,
        client_id: typing.Optional[int] = None,
        retargeting_group_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.createLookalikeRequest method


        :param account_id:
        :param source_type:
        :param client_id:
        :param retargeting_group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.createLookalikeRequest", params)

        model = AdsCreateLookalikeRequestResponse

        return model(**response).response

    async def create_target_group(
        self,
        account_id: int,
        name: str,
        lifetime: int,
        client_id: typing.Optional[int] = None,
        target_pixel_id: typing.Optional[int] = None,
        target_pixel_rules: typing.Optional[str] = None,
        **kwargs,
    ):
        """ads.createTargetGroup method


        :param account_id: Advertising account ID.
        :param name: Name of the target group - a string up to 64 characters long.
        :param lifetime: 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param target_pixel_id:
        :param target_pixel_rules:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.createTargetGroup", params)

        model = AdsCreateTargetGroupResponse

        return model(**response).response

    async def create_target_pixel(
        self,
        account_id: int,
        name: str,
        category_id: int,
        client_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        **kwargs,
    ):
        """ads.createTargetPixel method


        :param account_id:
        :param name:
        :param category_id:
        :param client_id:
        :param domain:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.createTargetPixel", params)

        model = AdsCreateTargetPixelResponse

        return model(**response).response

    async def delete_ads(
        self,
        account_id: int,
        ids: str,
        **kwargs,
    ):
        """ads.deleteAds method


        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with ad IDs.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteAds", params)

        model = AdsDeleteAdsResponse

        return model(**response).response

    async def delete_campaigns(
        self,
        account_id: int,
        ids: str,
        **kwargs,
    ):
        """ads.deleteCampaigns method


        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted campaigns.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteCampaigns", params)

        model = AdsDeleteCampaignsResponse

        return model(**response).response

    async def delete_clients(
        self,
        account_id: int,
        ids: str,
        **kwargs,
    ):
        """ads.deleteClients method


        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted clients.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteClients", params)

        model = AdsDeleteClientsResponse

        return model(**response).response

    async def delete_target_group(
        self,
        account_id: int,
        target_group_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.deleteTargetGroup method


        :param account_id: Advertising account ID.
        :param target_group_id: Group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteTargetGroup", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_target_pixel(
        self,
        account_id: int,
        target_pixel_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.deleteTargetPixel method


        :param account_id:
        :param target_pixel_id:
        :param client_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteTargetPixel", params)

        model = BaseUndefinedResponse

        return model(**response).response

    async def get_accounts(
        self,
        **kwargs,
    ):
        """ads.getAccounts method"""
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAccounts", params)

        model = AdsGetAccountsResponse

        return model(**response).response

    async def get_ads(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        only_deleted: typing.Optional[bool] = None,
        campaign_ids: typing.Optional[str] = None,
        ad_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.getAds method


        :param account_id: Advertising account ID.
        :param client_id: 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown: *0 - show only active ads,, *1 - show all ads.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 - show all ads,, *1 - show only archived ads. Available when include_deleted flag is *1
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param limit: Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAds", params)

        model = AdsGetAdsResponse

        return model(**response).response

    async def get_ads_layout(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        only_deleted: typing.Optional[bool] = None,
        campaign_ids: typing.Optional[str] = None,
        ad_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.getAdsLayout method


        :param account_id: Advertising account ID.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 - show only active ads,, *1 - show all ads.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 - show all ads,, *1 - show only archived ads. Available when include_deleted flag is *1
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAdsLayout", params)

        model = AdsGetAdsLayoutResponse

        return model(**response).response

    async def get_ads_targeting(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        only_deleted: typing.Optional[bool] = None,
        campaign_ids: typing.Optional[str] = None,
        ad_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.getAdsTargeting method


        :param account_id: Advertising account ID.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: flag that specifies whether archived ads shall be shown: *0 - show only active ads,, *1 - show all ads.
        :param only_deleted:
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset needed to return a specific subset of results.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAdsTargeting", params)

        model = AdsGetAdsTargetingResponse

        return model(**response).response

    async def get_budget(
        self,
        account_id: int,
        **kwargs,
    ):
        """ads.getBudget method


        :param account_id: Advertising account ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getBudget", params)

        model = AdsGetBudgetResponse

        return model(**response).response

    async def get_campaigns(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        campaign_ids: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ):
        """ads.getCampaigns method


        :param account_id: Advertising account ID.
        :param client_id: 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 - show only active campaigns,, *1 - show all campaigns.
        :param campaign_ids: Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        :param fields:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getCampaigns", params)

        model = AdsGetCampaignsResponse

        return model(**response).response

    async def get_categories(
        self,
        lang: typing.Optional[str] = None,
        **kwargs,
    ):
        """ads.getCategories method


        :param lang: Language. The full list of supported languages is [vk.com/dev/api_requests|here].
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getCategories", params)

        model = AdsGetCategoriesResponse

        return model(**response).response

    async def get_clients(
        self,
        account_id: int,
        **kwargs,
    ):
        """ads.getClients method


        :param account_id: Advertising account ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getClients", params)

        model = AdsGetClientsResponse

        return model(**response).response

    async def get_demographics(
        self,
        account_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
        **kwargs,
    ):
        """ads.getDemographics method


        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day - statistics by days,, *month - statistics by months,, *overall - overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - day it was created on,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - current day,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - current month,, *overall: 0.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getDemographics", params)

        model = AdsGetDemographicsResponse

        return model(**response).response

    async def get_flood_stats(
        self,
        account_id: int,
        **kwargs,
    ):
        """ads.getFloodStats method


        :param account_id: Advertising account ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getFloodStats", params)

        model = AdsGetFloodStatsResponse

        return model(**response).response

    async def get_lookalike_requests(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        requests_ids: typing.Optional[str] = None,
        offset: typing.Optional[int] = 0,
        limit: typing.Optional[int] = 10,
        sort_by: typing.Optional[str] = "id",
        **kwargs,
    ):
        """ads.getLookalikeRequests method


        :param account_id:
        :param client_id:
        :param requests_ids:
        :param offset:
        :param limit:
        :param sort_by:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getLookalikeRequests", params)

        model = AdsGetLookalikeRequestsResponse

        return model(**response).response

    async def get_musicians(
        self,
        artist_name: str,
        **kwargs,
    ):
        """ads.getMusicians method


        :param artist_name:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getMusicians", params)

        model = AdsGetMusiciansResponse

        return model(**response).response

    async def get_musicians_by_ids(
        self,
        ids: typing.List[int],
        **kwargs,
    ):
        """ads.getMusiciansByIds method


        :param ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getMusiciansByIds", params)

        model = AdsGetMusiciansResponse

        return model(**response).response

    async def get_office_users(
        self,
        account_id: int,
        **kwargs,
    ):
        """ads.getOfficeUsers method


        :param account_id: Advertising account ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getOfficeUsers", params)

        model = AdsGetOfficeUsersResponse

        return model(**response).response

    async def get_posts_reach(
        self,
        account_id: int,
        ids_type: str,
        ids: str,
        **kwargs,
    ):
        """ads.getPostsReach method


        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getPostsReach", params)

        model = AdsGetPostsReachResponse

        return model(**response).response

    async def get_rejection_reason(
        self,
        account_id: int,
        ad_id: int,
        **kwargs,
    ):
        """ads.getRejectionReason method


        :param account_id: Advertising account ID.
        :param ad_id: Ad ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getRejectionReason", params)

        model = AdsGetRejectionReasonResponse

        return model(**response).response

    async def get_statistics(
        self,
        account_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
        stats_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ):
        """ads.getStatistics method


        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns,, *client - clients,, *office - account.
        :param ids: IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day - statistics by days,, *month - statistics by months,, *overall - overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - day it was created on,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - current day,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - current month,, *overall: 0.
        :param stats_fields: Additional fields to add to statistics
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getStatistics", params)

        model = AdsGetStatisticsResponse

        return model(**response).response

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        ids: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        cities: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        **kwargs,
    ): ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        cities: str,
        ids: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
        **kwargs,
    ): ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        ids: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        cities: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        **kwargs,
    ): ...

    async def get_suggestions(
        self,
        section: str,
        ids: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        cities: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        **kwargs,
    ):
        """ads.getSuggestions method


        :param section: Section, suggestions are retrieved in. Available values: *countries - request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions - requested list of regions. 'country' parameter is required. *cities - requested list of cities. 'country' parameter is required. *districts - requested list of districts. 'cities' parameter is required. *stations - requested list of subway stations. 'cities' parameter is required. *streets - requested list of streets. 'cities' parameter is required. *schools - requested list of educational organizations. 'cities' parameter is required. *interests - requested list of interests. *positions - requested list of positions (professions). *group_types - requested list of group types. *religions - requested list of religious commitments. *browsers - requested list of browsers and mobile devices.
        :param ids: Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param q: Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        :param country: ID of the country objects are searched in.
        :param cities: IDs of cities where objects are searched in, separated with a comma.
        :param lang: Language of the returned string values. Supported languages: *ru - Russian,, *ua - Ukrainian,, *en - English.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getSuggestions", params)

        model = self.get_model(
            (
                (("regions",), AdsGetSuggestionsRegionsResponse),
                (("cities",), AdsGetSuggestionsCitiesResponse),
                (("schools",), AdsGetSuggestionsSchoolsResponse),
            ),
            default=AdsGetSuggestionsResponse,
            params=params,
        )

        return model(**response).response

    async def get_target_groups(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        **kwargs,
    ):
        """ads.getTargetGroups method


        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: '1' - to return pixel code.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getTargetGroups", params)

        model = AdsGetTargetGroupsResponse

        return model(**response).response

    async def get_target_pixels(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.getTargetPixels method


        :param account_id:
        :param client_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getTargetPixels", params)

        model = AdsGetTargetPixelsResponse

        return model(**response).response

    async def get_targeting_stats(
        self,
        account_id: int,
        link_url: str,
        client_id: typing.Optional[int] = None,
        criteria: typing.Optional[str] = None,
        ad_id: typing.Optional[int] = None,
        ad_format: typing.Optional[int] = None,
        ad_platform: typing.Optional[str] = None,
        ad_platform_no_wall: typing.Optional[str] = None,
        ad_platform_no_ad_network: typing.Optional[str] = None,
        publisher_platforms: typing.Optional[str] = None,
        link_domain: typing.Optional[str] = None,
        need_precise: typing.Optional[bool] = None,
        impressions_limit_period: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.getTargetingStats method


        :param account_id: Advertising account ID.
        :param link_url: URL for the advertised object.
        :param client_id:
        :param criteria: Serialized JSON object that describes targeting parameters. Description of 'criteria' object see below.
        :param ad_id: ID of an ad which targeting parameters shall be analyzed.
        :param ad_format: Ad format. Possible values: *'1' - image and text,, *'2' - big image,, *'3' - exclusive format,, *'4' - community, square image,, *'7' - special app format,, *'8' - special community format,, *'9' - post in community,, *'10' - app board.
        :param ad_platform: Platforms to use for ad showing. Possible values: (for 'ad_format' = '1'), *'0' - VK and partner sites,, *'1' - VK only. (for 'ad_format' = '9'), *'all' - all platforms,, *'desktop' - desktop version,, *'mobile' - mobile version and apps.
        :param ad_platform_no_wall:
        :param ad_platform_no_ad_network:
        :param publisher_platforms:
        :param link_domain: Domain of the advertised object.
        :param need_precise: Additionally return recommended cpc and cpm to reach 5,10..95 percents of audience.
        :param impressions_limit_period: Impressions limit period in seconds, must be a multiple of 86400(day)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getTargetingStats", params)

        model = AdsGetTargetingStatsResponse

        return model(**response).response

    async def get_upload_u_r_l(
        self,
        ad_format: int,
        icon: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.getUploadURL method


        :param ad_format: Ad format: *1 - image and text,, *2 - big image,, *3 - exclusive format,, *4 - community, square image,, *7 - special app format.
        :param icon:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getUploadURL", params)

        model = AdsGetUploadURLResponse

        return model(**response).response

    async def get_video_upload_u_r_l(
        self,
        **kwargs,
    ):
        """ads.getVideoUploadURL method"""
        params = self.get_set_params(locals())
        response = await self.api.request("ads.getVideoUploadURL", params)

        model = AdsGetVideoUploadURLResponse

        return model(**response).response

    async def import_target_contacts(
        self,
        account_id: int,
        target_group_id: int,
        contacts: str,
        client_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.importTargetContacts method


        :param account_id: Advertising account ID.
        :param target_group_id: Target group ID.
        :param contacts: List of phone numbers, emails or user IDs separated with a comma.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.importTargetContacts", params)

        model = AdsImportTargetContactsResponse

        return model(**response).response

    async def remove_office_users(
        self,
        account_id: int,
        ids: str,
        **kwargs,
    ):
        """ads.removeOfficeUsers method


        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted managers.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.removeOfficeUsers", params)

        model = AdsRemoveOfficeUsersResponse

        return model(**response).response

    async def remove_target_contacts(
        self,
        account_id: int,
        target_group_id: int,
        contacts: str,
        client_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.removeTargetContacts method


        :param account_id:
        :param target_group_id:
        :param contacts:
        :param client_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.removeTargetContacts", params)

        model = AdsRemoveTargetContactsResponse

        return model(**response).response

    async def save_lookalike_request_result(
        self,
        account_id: int,
        request_id: int,
        level: int,
        client_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.saveLookalikeRequestResult method


        :param account_id:
        :param request_id:
        :param level:
        :param client_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.saveLookalikeRequestResult", params)

        model = AdsSaveLookalikeRequestResultResponse

        return model(**response).response

    async def share_target_group(
        self,
        account_id: int,
        target_group_id: int,
        client_id: typing.Optional[int] = None,
        share_with_client_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """ads.shareTargetGroup method


        :param account_id:
        :param target_group_id:
        :param client_id:
        :param share_with_client_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.shareTargetGroup", params)

        model = AdsShareTargetGroupResponse

        return model(**response).response

    async def update_ads(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.updateAds method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateAds", params)

        model = AdsUpdateAdsResponse

        return model(**response).response

    async def update_campaigns(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.updateCampaigns method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateCampaigns", params)

        model = AdsUpdateCampaignsResponse

        return model(**response).response

    async def update_clients(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.updateClients method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateClients", params)

        model = AdsUpdateClientsResponse

        return model(**response).response

    async def update_office_users(
        self,
        account_id: int,
        data: str,
        **kwargs,
    ):
        """ads.updateOfficeUsers method


        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateOfficeUsers", params)

        model = AdsUpdateOfficeUsersResponse

        return model(**response).response

    async def update_target_group(
        self,
        account_id: int,
        target_group_id: int,
        name: str,
        lifetime: int,
        client_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        target_pixel_id: typing.Optional[int] = None,
        target_pixel_rules: typing.Optional[str] = None,
        **kwargs,
    ):
        """ads.updateTargetGroup method


        :param account_id: Advertising account ID.
        :param target_group_id: Group ID.
        :param name: New name of the target group - a string up to 64 characters long.
        :param lifetime: 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' - automatic exclusion is off.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param domain: Domain of the site where user accounting code will be placed.
        :param target_pixel_id:
        :param target_pixel_rules:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateTargetGroup", params)

        model = BaseOkResponse

        return model(**response).response

    async def update_target_pixel(
        self,
        account_id: int,
        target_pixel_id: int,
        name: str,
        category_id: int,
        client_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        **kwargs,
    ):
        """ads.updateTargetPixel method


        :param account_id:
        :param target_pixel_id:
        :param name:
        :param category_id:
        :param client_id:
        :param domain:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateTargetPixel", params)

        model = BaseUndefinedResponse

        return model(**response).response


__all__ = ("AdsCategory",)
