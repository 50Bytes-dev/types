import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class DatabaseGetChairsResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetChairsResponse(BaseResponse):
    response: "DatabaseGetChairsResponseModel"


class DatabaseGetCitiesByIdResponseModel(BaseModel):

    response: typing.List[DatabaseCityById] = Field()


class DatabaseGetCitiesByIdResponse(BaseResponse):
    response: "DatabaseGetCitiesByIdResponseModel"


class DatabaseGetCitiesResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetCitiesResponse(BaseResponse):
    response: "DatabaseGetCitiesResponseModel"


class DatabaseGetCountriesByIdResponseModel(BaseModel):

    response: typing.List[BaseCountry] = Field()


class DatabaseGetCountriesByIdResponse(BaseResponse):
    response: "DatabaseGetCountriesByIdResponseModel"


class DatabaseGetCountriesResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetCountriesResponse(BaseResponse):
    response: "DatabaseGetCountriesResponseModel"


class DatabaseGetFacultiesResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetFacultiesResponse(BaseResponse):
    response: "DatabaseGetFacultiesResponseModel"


class DatabaseGetMetroStationsByIdResponseModel(BaseModel):

    response: typing.List[DatabaseStation] = Field()


class DatabaseGetMetroStationsByIdResponse(BaseResponse):
    response: "DatabaseGetMetroStationsByIdResponseModel"


class DatabaseGetMetroStationsResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetMetroStationsResponse(BaseResponse):
    response: "DatabaseGetMetroStationsResponseModel"


class DatabaseGetRegionsResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetRegionsResponse(BaseResponse):
    response: "DatabaseGetRegionsResponseModel"


class DatabaseGetSchoolClassesNewResponseModel(BaseModel):

    response: typing.List[DatabaseSchoolClass] = Field()


class DatabaseGetSchoolClassesNewResponse(BaseResponse):
    response: "DatabaseGetSchoolClassesNewResponseModel"


class DatabaseGetSchoolsResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetSchoolsResponse(BaseResponse):
    response: "DatabaseGetSchoolsResponseModel"


class DatabaseGetUniversitiesResponseModel(BaseModel):

    response: dict = Field()


class DatabaseGetUniversitiesResponse(BaseResponse):
    response: "DatabaseGetUniversitiesResponseModel"
