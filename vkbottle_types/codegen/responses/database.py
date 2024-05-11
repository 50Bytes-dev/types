import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class DatabaseGetChairsResponse(BaseModel):

    response: dict = Field()


class DatabaseGetCitiesByIdResponse(BaseModel):

    response: typing.List[DatabaseCityById] = Field()


class DatabaseGetCitiesResponse(BaseModel):

    response: dict = Field()


class DatabaseGetCountriesByIdResponse(BaseModel):

    response: typing.List[BaseCountry] = Field()


class DatabaseGetCountriesResponse(BaseModel):

    response: dict = Field()


class DatabaseGetFacultiesResponse(BaseModel):

    response: dict = Field()


class DatabaseGetMetroStationsByIdResponse(BaseModel):

    response: typing.List[DatabaseStation] = Field()


class DatabaseGetMetroStationsResponse(BaseModel):

    response: dict = Field()


class DatabaseGetRegionsResponse(BaseModel):

    response: dict = Field()


class DatabaseGetSchoolClassesNewResponse(BaseModel):

    response: typing.List[DatabaseSchoolClass] = Field()


class DatabaseGetSchoolsResponse(BaseModel):

    response: dict = Field()


class DatabaseGetUniversitiesResponse(BaseModel):

    response: dict = Field()
