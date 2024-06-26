import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.apps import *
from vkbottle_types.responses.base import *

### OPTIONAL


class AppsCategory(BaseCategory):

    async def add_snippet(
        self,
        vk_ref: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[typing.List[int]] = None,
        hash: typing.Optional[typing.List[str]] = None,
        snippet_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        image_url: typing.Optional[str] = None,
        small_image_url: typing.Optional[str] = None,
        button: typing.Optional[str] = None,
        **kwargs,
    ):
        """apps.addSnippet method


        :param vk_ref:
        :param group_id:
        :param hash:
        :param snippet_id:
        :param title:
        :param description:
        :param image_url:
        :param small_image_url:
        :param button:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.addSnippet", params)

        model = AppsAddSnippetResponse

        return model(**response).response

    async def add_users_to_testing_group(
        self,
        user_ids: typing.List[int],
        group_id: int,
        **kwargs,
    ):
        """apps.addUsersToTestingGroup method


        :param user_ids:
        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.addUsersToTestingGroup", params)

        model = BaseBoolResponse

        return model(**response).response

    async def delete_app_requests(
        self,
        **kwargs,
    ):
        """apps.deleteAppRequests method"""
        params = self.get_set_params(locals())
        response = await self.api.request("apps.deleteAppRequests", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_snippet(
        self,
        id: typing.Optional[int] = None,
        **kwargs,
    ):
        """apps.deleteSnippet method


        :param id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.deleteSnippet", params)

        model = BaseOkResponse

        return model(**response).response

    async def get(
        self,
        app_id: typing.Optional[int] = None,
        app_ids: typing.Optional[typing.List[int]] = None,
        platform: typing.Optional[str] = "web",
        extended: typing.Optional[bool] = 0,
        return_friends: typing.Optional[bool] = 0,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        app_fields: typing.Optional[typing.List[AppsAppFields]] = None,
        **kwargs,
    ):
        """apps.get method


        :param app_id: Application ID
        :param app_ids: List of application ID
        :param platform: platform. Possible values: *'ios' - iOS,, *'android' - Android,, *'winphone' - Windows Phone,, *'web' - приложения на vk.com. By default: 'web'.
        :param extended:
        :param return_friends:
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default),, 'gen' - genitive,, 'dat' - dative,, 'acc' - accusative,, 'ins' - instrumental,, 'abl' - prepositional. (only if 'return_friends' = '1')
        :param app_fields: List of app fields to return. Fields 'id', 'type' and 'title' will always be in response. Leave this field empty to get all fields
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.get", params)

        model = AppsGetResponse

        return model(**response).response

    async def get_catalog(
        self,
        sort: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        platform: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        return_friends: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        genre_id: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        **kwargs,
    ):
        """apps.getCatalog method


        :param sort: Sort order: 'popular_today' - popular for one day (default), 'visitors' - by visitors number , 'create_date' - by creation date, 'growth_rate' - by growth rate, 'popular_week' - popular for one week
        :param offset: Offset required to return a specific subset of apps.
        :param count: Number of apps to return.
        :param platform:
        :param extended: '1' - to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' - not to return additional fields (default).
        :param return_friends:
        :param fields:
        :param name_case:
        :param q: Search query string.
        :param genre_id:
        :param filter: 'installed' - to return list of installed apps (only for mobile platform).
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getCatalog", params)

        model = AppsGetCatalogResponse

        return model(**response).response

    @typing.overload
    async def get_friends_list(
        self,
        extended: typing.Literal[True] = True,
        count: typing.Optional[int] = 20,
        offset: typing.Optional[int] = 0,
        type: typing.Optional[str] = "invite",
        fields: typing.Optional[typing.List[UsersFields]] = 1,
        query: typing.Optional[str] = None,
        **kwargs,
    ): ...

    async def get_friends_list(
        self,
        extended: typing.Optional[bool] = 0,
        count: typing.Optional[int] = 20,
        offset: typing.Optional[int] = 0,
        type: typing.Optional[str] = "invite",
        fields: typing.Optional[typing.List[UsersFields]] = 1,
        query: typing.Optional[str] = None,
        **kwargs,
    ):
        """apps.getFriendsList method


        :param extended:
        :param count: List size.
        :param offset:
        :param type: List type. Possible values: * 'invite' - available for invites (don't play the game),, * 'request' - available for request (play the game). By default: 'invite'.
        :param fields: Additional profile fields, see [vk.com/dev/fields|description].
        :param query: Search query string (e.g., 'Vasya Babich').
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getFriendsList", params)

        model = self.get_model(
            ((("extended",), AppsGetFriendsListExtendedResponse),),
            default=AppsGetFriendsListResponse,
            params=params,
        )

        return model(**response).response

    @typing.overload
    async def get_leaderboard(
        self,
        type: str,
        extended: typing.Literal[True] = True,
        value_global: typing.Optional[bool] = 1,
        **kwargs,
    ): ...

    async def get_leaderboard(
        self,
        type: str,
        value_global: typing.Optional[bool] = 1,
        extended: typing.Optional[bool] = 0,
        **kwargs,
    ):
        """apps.getLeaderboard method


        :param type: Leaderboard type. Possible values: *'level' - by level,, *'points' - by mission points,, *'score' - by score ().
        :param global: Rating type. Possible values: *'1' - global rating among all players,, *'0' - rating among user friends.
        :param extended: 1 - to return additional info about users
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getLeaderboard", params)

        model = self.get_model(
            ((("extended",), AppsGetLeaderboardExtendedResponse),),
            default=AppsGetLeaderboardResponse,
            params=params,
        )

        return model(**response).response

    async def get_mini_app_policies(
        self,
        app_id: int,
        **kwargs,
    ):
        """apps.getMiniAppPolicies method


        :param app_id: Mini App ID
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getMiniAppPolicies", params)

        model = AppsGetMiniAppPoliciesResponse

        return model(**response).response

    async def get_scopes(
        self,
        type: typing.Optional[str] = "user",
        **kwargs,
    ):
        """apps.getScopes method


        :param type:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScopes", params)

        model = AppsGetScopesResponse

        return model(**response).response

    async def get_score(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """apps.getScore method


        :param user_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScore", params)

        model = AppsGetScoreResponse

        return model(**response).response

    async def get_snippets(
        self,
        **kwargs,
    ):
        """apps.getSnippets method"""
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getSnippets", params)

        model = AppsGetSnippetsResponse

        return model(**response).response

    async def get_testing_groups(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """apps.getTestingGroups method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.getTestingGroups", params)

        model = AppsGetTestingGroupsResponse

        return model(**response).response

    async def is_notifications_allowed(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """apps.isNotificationsAllowed method


        :param user_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.isNotificationsAllowed", params)

        model = AppsIsNotificationsAllowedResponse

        return model(**response).response

    async def promo_has_active_gift(
        self,
        promo_id: int,
        user_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """apps.promoHasActiveGift method


        :param promo_id: Id of game promo action
        :param user_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoHasActiveGift", params)

        model = BaseBoolResponse

        return model(**response).response

    async def promo_use_gift(
        self,
        promo_id: int,
        user_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """apps.promoUseGift method


        :param promo_id: Id of game promo action
        :param user_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoUseGift", params)

        model = BaseBoolResponse

        return model(**response).response

    async def remove_testing_group(
        self,
        group_id: int,
        **kwargs,
    ):
        """apps.removeTestingGroup method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.removeTestingGroup", params)

        model = BaseBoolResponse

        return model(**response).response

    async def remove_users_from_testing_groups(
        self,
        user_ids: typing.List[int],
        **kwargs,
    ):
        """apps.removeUsersFromTestingGroups method


        :param user_ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.removeUsersFromTestingGroups", params)

        model = BaseBoolResponse

        return model(**response).response

    async def send_request(
        self,
        user_id: int,
        text: typing.Optional[str] = None,
        type: typing.Optional[str] = "request",
        name: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        separate: typing.Optional[bool] = None,
        **kwargs,
    ):
        """apps.sendRequest method


        :param user_id: id of the user to send a request
        :param text: request text
        :param type: request type. Values: 'invite' - if the request is sent to a user who does not have the app installed,, 'request' - if a user has already installed the app
        :param name:
        :param key: special string key to be sent with the request
        :param separate:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.sendRequest", params)

        model = AppsSendRequestResponse

        return model(**response).response

    async def update_meta_for_testing_group(
        self,
        webview: str,
        name: str,
        platforms: typing.List[str],
        group_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ):
        """apps.updateMetaForTestingGroup method


        :param webview:
        :param name:
        :param platforms:
        :param group_id:
        :param user_ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("apps.updateMetaForTestingGroup", params)

        model = AppsCreatedGroupResponse

        return model(**response).response


__all__ = ("AppsCategory",)
