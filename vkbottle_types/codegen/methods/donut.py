import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.donut import *
from vkbottle_types.responses.base import *
from vkbottle_types.responses.groups import *


class DonutCategory(BaseCategory):

    async def get_friends(
        self,
        owner_id: int,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 10,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ):
        """donut.getFriends method


        :param owner_id:
        :param offset:
        :param count:
        :param fields:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("donut.getFriends", params)

        model = GroupsGetMembersFieldsResponse

        return model(**response).response

    async def get_subscription(
        self,
        owner_id: int,
        **kwargs,
    ):
        """donut.getSubscription method


        :param owner_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscription", params)

        model = DonutGetSubscriptionResponse

        return model(**response).response

    async def get_subscriptions(
        self,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 10,
        **kwargs,
    ):
        """donut.getSubscriptions method


        :param fields:
        :param offset:
        :param count:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscriptions", params)

        model = DonutGetSubscriptionsResponse

        return model(**response).response

    async def is_don(
        self,
        owner_id: int,
        **kwargs,
    ):
        """donut.isDon method


        :param owner_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("donut.isDon", params)

        model = BaseBoolResponse

        return model(**response).response


__all__ = ("DonutCategory",)
