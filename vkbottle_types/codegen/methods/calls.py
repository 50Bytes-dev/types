import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.calls import *
from vkbottle_types.responses.base import *

### OPTIONAL


class CallsCategory(BaseCategory):

    async def force_finish(
        self,
        call_id: str,
        **kwargs,
    ) -> BaseOkResponse:
        """calls.forceFinish method


        :param call_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def start(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> CallsStartResponse:
        """calls.start method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = CallsStartResponse

        return model(**response).response


__all__ = ("CallsCategory",)
