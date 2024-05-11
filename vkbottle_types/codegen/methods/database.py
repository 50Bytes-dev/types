import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.database import *
from vkbottle_types.responses.base import *

### OPTIONAL


class DatabaseCategory(BaseCategory):

    async def get_chairs(
        self,
        faculty_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        **kwargs,
    ) -> DatabaseGetChairsResponse:
        """database.getChairs method


        :param faculty_id: id of the faculty to get chairs from
        :param offset: offset required to get a certain subset of chairs
        :param count: amount of chairs to get
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getChairs", params)

        model = DatabaseGetChairsResponse

        return model(**response).response

    async def get_cities(
        self,
        region_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        need_all: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        **kwargs,
    ) -> DatabaseGetCitiesResponse:
        """database.getCities method


        :param region_id: Region ID.
        :param q: Search query.
        :param need_all: '1' - to return all cities in the country, '0' - to return major cities in the country (default),
        :param offset: Offset needed to return a specific subset of cities.
        :param count: Number of cities to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getCities", params)

        model = DatabaseGetCitiesResponse

        return model(**response).response

    async def get_cities_by_id(
        self,
        city_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> DatabaseGetCitiesByIdResponse:
        """database.getCitiesById method


        :param city_ids: City IDs.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getCitiesById", params)

        model = DatabaseGetCitiesByIdResponse

        return model(**response).response

    async def get_countries(
        self,
        need_all: typing.Optional[bool] = None,
        code: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        **kwargs,
    ) -> DatabaseGetCountriesResponse:
        """database.getCountries method


        :param need_all: '1' - to return a full list of all countries, '0' - to return a list of countries near the current user's country (default).
        :param code: Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param offset: Offset needed to return a specific subset of countries.
        :param count: Number of countries to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getCountries", params)

        model = DatabaseGetCountriesResponse

        return model(**response).response

    async def get_countries_by_id(
        self,
        country_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> DatabaseGetCountriesByIdResponse:
        """database.getCountriesById method


        :param country_ids: Country IDs.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getCountriesById", params)

        model = DatabaseGetCountriesByIdResponse

        return model(**response).response

    async def get_faculties(
        self,
        university_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        **kwargs,
    ) -> DatabaseGetFacultiesResponse:
        """database.getFaculties method


        :param university_id: University ID.
        :param offset: Offset needed to return a specific subset of faculties.
        :param count: Number of faculties to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getFaculties", params)

        model = DatabaseGetFacultiesResponse

        return model(**response).response

    async def get_metro_stations(
        self,
        city_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        extended: typing.Optional[bool] = 0,
        **kwargs,
    ) -> DatabaseGetMetroStationsResponse:
        """database.getMetroStations method


        :param city_id:
        :param offset:
        :param count:
        :param extended:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getMetroStations", params)

        model = DatabaseGetMetroStationsResponse

        return model(**response).response

    async def get_metro_stations_by_id(
        self,
        station_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> DatabaseGetMetroStationsByIdResponse:
        """database.getMetroStationsById method


        :param station_ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getMetroStationsById", params)

        model = DatabaseGetMetroStationsByIdResponse

        return model(**response).response

    async def get_regions(
        self,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        **kwargs,
    ) -> DatabaseGetRegionsResponse:
        """database.getRegions method


        :param q: Search query.
        :param offset: Offset needed to return specific subset of regions.
        :param count: Number of regions to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getRegions", params)

        model = DatabaseGetRegionsResponse

        return model(**response).response

    async def get_school_classes(
        self,
        country_id: typing.Optional[int] = None,
        **kwargs,
    ) -> DatabaseGetSchoolClassesNewResponse:
        """database.getSchoolClasses method


        :param country_id: Country ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getSchoolClasses", params)

        model = DatabaseGetSchoolClassesNewResponse

        return model(**response).response

    async def get_schools(
        self,
        city_id: int,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        **kwargs,
    ) -> DatabaseGetSchoolsResponse:
        """database.getSchools method


        :param city_id: City ID.
        :param q: Search query.
        :param offset: Offset needed to return a specific subset of schools.
        :param count: Number of schools to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getSchools", params)

        model = DatabaseGetSchoolsResponse

        return model(**response).response

    async def get_universities(
        self,
        q: typing.Optional[str] = None,
        city_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 100,
        **kwargs,
    ) -> DatabaseGetUniversitiesResponse:
        """database.getUniversities method


        :param q: Search query.
        :param city_id: City ID.
        :param offset: Offset needed to return a specific subset of universities.
        :param count: Number of universities to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("database.getUniversities", params)

        model = DatabaseGetUniversitiesResponse

        return model(**response).response


__all__ = ("DatabaseCategory",)
