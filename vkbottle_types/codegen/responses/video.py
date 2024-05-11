import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class VideoAddAlbumResponseModel(BaseModel):

    response: dict = Field()


class VideoAddAlbumResponse(BaseResponse):
    response: "VideoAddAlbumResponseModel"


class VideoChangeVideoAlbumsResponseModel(BaseModel):

    response: typing.List[int] = Field()


class VideoChangeVideoAlbumsResponse(BaseResponse):
    response: "VideoChangeVideoAlbumsResponseModel"


class VideoCreateCommentResponseModel(BaseModel):

    response: int = Field(
        description="Created comment ID",
    )


class VideoCreateCommentResponse(BaseResponse):
    response: "VideoCreateCommentResponseModel"


class VideoEditResponseModel(BaseModel):

    response: dict = Field()


class VideoEditResponse(BaseResponse):
    response: "VideoEditResponseModel"


class VideoGetAlbumByIdResponseModel(BaseModel):

    response: "VideoVideoAlbumFull" = Field()


class VideoGetAlbumByIdResponse(BaseResponse):
    response: "VideoGetAlbumByIdResponseModel"


class VideoGetAlbumsByVideoExtendedResponseModel(BaseModel):

    response: dict = Field()


class VideoGetAlbumsByVideoExtendedResponse(BaseResponse):
    response: "VideoGetAlbumsByVideoExtendedResponseModel"


class VideoGetAlbumsByVideoResponseModel(BaseModel):

    response: typing.List[int] = Field()


class VideoGetAlbumsByVideoResponse(BaseResponse):
    response: "VideoGetAlbumsByVideoResponseModel"


class VideoGetAlbumsExtendedResponseModel(BaseModel):

    response: dict = Field()


class VideoGetAlbumsExtendedResponse(BaseResponse):
    response: "VideoGetAlbumsExtendedResponseModel"


class VideoGetAlbumsResponseModel(BaseModel):

    response: dict = Field()


class VideoGetAlbumsResponse(BaseResponse):
    response: "VideoGetAlbumsResponseModel"


class VideoGetCommentsExtendedResponseModel(BaseModel):

    response: dict = Field()


class VideoGetCommentsExtendedResponse(BaseResponse):
    response: "VideoGetCommentsExtendedResponseModel"


class VideoGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class VideoGetCommentsResponse(BaseResponse):
    response: "VideoGetCommentsResponseModel"


class VideoGetLongPollServerResponseModel(BaseModel):

    response: dict = Field()


class VideoGetLongPollServerResponse(BaseResponse):
    response: "VideoGetLongPollServerResponseModel"


class VideoGetResponseModel(BaseModel):

    response: dict = Field()


class VideoGetResponse(BaseResponse):
    response: "VideoGetResponseModel"


class VideoLiveGetCategoriesResponseModel(BaseModel):

    response: typing.List[VideoLiveCategory] = Field()


class VideoLiveGetCategoriesResponse(BaseResponse):
    response: "VideoLiveGetCategoriesResponseModel"


class VideoSaveResponseModel(BaseModel):

    response: "VideoSaveResult" = Field()


class VideoSaveResponse(BaseResponse):
    response: "VideoSaveResponseModel"


class VideoSearchExtendedResponseModel(BaseModel):

    response: dict = Field()


class VideoSearchExtendedResponse(BaseResponse):
    response: "VideoSearchExtendedResponseModel"


class VideoSearchResponseModel(BaseModel):

    response: dict = Field()


class VideoSearchResponse(BaseResponse):
    response: "VideoSearchResponseModel"


class VideoStartStreamingResponseModel(BaseModel):

    response: dict = Field()


class VideoStartStreamingResponse(BaseResponse):
    response: "VideoStartStreamingResponseModel"


class VideoStopStreamingResponseModel(BaseModel):

    response: dict = Field()


class VideoStopStreamingResponse(BaseResponse):
    response: "VideoStopStreamingResponseModel"


class VideoUploadResponseModel(BaseModel):

    response: dict = Field()


class VideoUploadResponse(BaseResponse):
    response: "VideoUploadResponseModel"
