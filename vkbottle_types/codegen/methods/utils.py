import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.utils import *
from vkbottle_types.responses.base import *

### OPTIONAL


class UtilsCategory(BaseCategory):

    async def check_link(
        self,
        url: str,
        **kwargs,
    ):
        """utils.checkLink method


        :param url: Link to check (e.g., 'http://google.com').
        """
        params = self.get_set_params(locals())
        response = await self.api.request("utils.checkLink", params)

        model = UtilsCheckLinkResponse

        return model(**response).response

    async def delete_from_last_shortened(
        self,
        key: str,
        **kwargs,
    ):
        """utils.deleteFromLastShortened method


        :param key: Link key (characters after vk.cc/).
        """
        params = self.get_set_params(locals())
        response = await self.api.request("utils.deleteFromLastShortened", params)

        model = BaseOkResponse

        return model(**response).response

    async def get_last_shortened_links(
        self,
        count: typing.Optional[int] = 10,
        offset: typing.Optional[int] = 0,
        **kwargs,
    ):
        """utils.getLastShortenedLinks method


        :param count: Number of links to return.
        :param offset: Offset needed to return a specific subset of links.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("utils.getLastShortenedLinks", params)

        model = UtilsGetLastShortenedLinksResponse

        return model(**response).response

    @typing.overload
    async def get_link_stats(
        self,
        key: str,
        extended: typing.Literal[True] = True,
        source: typing.Optional[str] = "vk_cc",
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[str] = "day",
        intervals_count: typing.Optional[int] = 1,
        **kwargs,
    ): ...

    async def get_link_stats(
        self,
        key: str,
        source: typing.Optional[str] = "vk_cc",
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[str] = "day",
        intervals_count: typing.Optional[int] = 1,
        extended: typing.Optional[bool] = 0,
        **kwargs,
    ):
        """utils.getLinkStats method


        :param key: Link key (characters after vk.cc/).
        :param source: Source of scope
        :param access_key: Access key for private link stats.
        :param interval: Interval.
        :param intervals_count: Number of intervals to return.
        :param extended: 1 - to return extended stats data (sex, age, geo). 0 - to return views number only.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("utils.getLinkStats", params)

        model = self.get_model(
            ((("extended",), UtilsGetLinkStatsExtendedResponse),),
            default=UtilsGetLinkStatsResponse,
            params=params,
        )

        return model(**response).response

    async def get_server_time(
        self,
        **kwargs,
    ):
        """utils.getServerTime method"""
        params = self.get_set_params(locals())
        response = await self.api.request("utils.getServerTime", params)

        model = UtilsGetServerTimeResponse

        return model(**response).response

    async def get_short_link(
        self,
        url: str,
        private: typing.Optional[bool] = 0,
        **kwargs,
    ):
        """utils.getShortLink method


        :param url: URL to be shortened.
        :param private: 1 - private stats, 0 - public stats.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("utils.getShortLink", params)

        model = UtilsGetShortLinkResponse

        return model(**response).response

    async def resolve_screen_name(
        self,
        screen_name: str,
        **kwargs,
    ):
        """utils.resolveScreenName method


        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("utils.resolveScreenName", params)

        model = UtilsResolveScreenNameResponse

        return model(**response).response


__all__ = ("UtilsCategory",)
