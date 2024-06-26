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
    ):
        """calls.forceFinish method


        :param call_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("calls.forceFinish", params)

        model = BaseOkResponse

        return model(**response).response

    async def start(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """calls.start method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("calls.start", params)

        model = CallsStartResponse

        return model(**response).response


__all__ = ("CallsCategory",)
