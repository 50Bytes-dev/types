import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.streaming import *
from vkbottle_types.responses.base import *

### OPTIONAL


class StreamingCategory(BaseCategory):

    async def get_server_url(
        self,
        **kwargs,
    ) -> StreamingGetServerUrlResponse:
        """streaming.getServerUrl method"""
        params = self.get_set_params(locals())
        response = await self.api.request("streaming.getServerUrl", params)

        model = StreamingGetServerUrlResponse

        return model(**response).response

    async def get_stats(
        self,
        type: typing.Optional[str] = None,
        interval: typing.Optional[str] = "5m",
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        **kwargs,
    ) -> StreamingGetStatsResponse:
        """streaming.getStats method


        :param type:
        :param interval:
        :param start_time:
        :param end_time:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("streaming.getStats", params)

        model = StreamingGetStatsResponse

        return model(**response).response

    async def get_stem(
        self,
        word: str,
        **kwargs,
    ) -> StreamingGetStemResponse:
        """streaming.getStem method


        :param word:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("streaming.getStem", params)

        model = StreamingGetStemResponse

        return model(**response).response


__all__ = ("StreamingCategory",)
