import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.adsweb import *
from vkbottle_types.responses.base import *

### OPTIONAL


class AdswebCategory(BaseCategory):

    async def get_ad_categories(
        self,
        office_id: int,
        **kwargs,
    ):
        """adsweb.getAdCategories method


        :param office_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdCategories", params)

        model = AdswebGetAdCategoriesResponse

        return model(**response).response

    async def get_ad_unit_code(
        self,
        **kwargs,
    ):
        """adsweb.getAdUnitCode method"""
        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdUnitCode", params)

        model = AdswebGetAdUnitCodeResponse

        return model(**response).response

    async def get_ad_units(
        self,
        office_id: int,
        sites_ids: typing.Optional[str] = None,
        ad_units_ids: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        **kwargs,
    ):
        """adsweb.getAdUnits method


        :param office_id:
        :param sites_ids:
        :param ad_units_ids:
        :param fields:
        :param limit:
        :param offset:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdUnits", params)

        model = AdswebGetAdUnitsResponse

        return model(**response).response

    async def get_fraud_history(
        self,
        office_id: int,
        sites_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        **kwargs,
    ):
        """adsweb.getFraudHistory method


        :param office_id:
        :param sites_ids:
        :param limit:
        :param offset:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getFraudHistory", params)

        model = AdswebGetFraudHistoryResponse

        return model(**response).response

    async def get_sites(
        self,
        office_id: int,
        sites_ids: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        **kwargs,
    ):
        """adsweb.getSites method


        :param office_id:
        :param sites_ids:
        :param fields:
        :param limit:
        :param offset:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getSites", params)

        model = AdswebGetSitesResponse

        return model(**response).response

    async def get_statistics(
        self,
        office_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
        **kwargs,
    ):
        """adsweb.getStatistics method


        :param office_id:
        :param ids_type:
        :param ids:
        :param period:
        :param date_from:
        :param date_to:
        :param fields:
        :param limit:
        :param page_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getStatistics", params)

        model = AdswebGetStatisticsResponse

        return model(**response).response


__all__ = ("AdswebCategory",)
