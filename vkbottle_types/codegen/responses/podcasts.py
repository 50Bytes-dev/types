import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PodcastsSearchPodcastResponseModel(BaseModel):

    response: dict = Field()


class PodcastsSearchPodcastResponse(BaseResponse):
    response: "PodcastsSearchPodcastResponseModel"
