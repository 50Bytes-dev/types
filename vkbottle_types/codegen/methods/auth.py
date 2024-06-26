import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.auth import *
from vkbottle_types.responses.base import *

### OPTIONAL


class AuthCategory(BaseCategory):

    async def restore(
        self,
        phone: str,
        last_name: str,
        **kwargs,
    ):
        """auth.restore method


        :param phone: User phone number.
        :param last_name: User last name.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("auth.restore", params)

        model = AuthRestoreResponse

        return model(**response).response


__all__ = ("AuthCategory",)
