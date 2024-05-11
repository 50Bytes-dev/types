import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PhotosCopyResponse(BaseModel):

    response: int = Field(
        description="Photo ID",
    )


class PhotosCreateAlbumResponse(BaseModel):

    response: "PhotosPhotoAlbumFull" = Field()


class PhotosCreateCommentResponse(BaseModel):

    response: int = Field(
        description="Created comment ID",
    )


class PhotosGetAlbumsCountResponse(BaseModel):

    response: int = Field(
        description="Albums number",
    )


class PhotosGetAlbumsResponse(BaseModel):

    response: dict = Field()


class PhotosGetAllCommentsResponse(BaseModel):

    response: dict = Field()


class PhotosGetAllResponse(BaseModel):

    response: dict = Field()


class PhotosGetByIdResponse(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosGetCommentsExtendedResponse(BaseModel):

    response: dict = Field()


class PhotosGetCommentsResponse(BaseModel):

    response: dict = Field()


class PhotosGetMarketUploadServerResponse(BaseModel):

    response: "BaseUploadServer" = Field()


class PhotosGetMessagesUploadServerResponse(BaseModel):

    response: "PhotosPhotoUpload" = Field()


class PhotosGetNewTagsResponse(BaseModel):

    response: dict = Field()


class PhotosGetTagsResponse(BaseModel):

    response: typing.List[PhotosPhotoTag] = Field()


class PhotosGetUploadServerResponse(BaseModel):

    response: "PhotosPhotoUpload" = Field()


class PhotosGetUserPhotosResponse(BaseModel):

    response: dict = Field()


class PhotosGetWallUploadServerResponse(BaseModel):

    response: "PhotosPhotoUpload" = Field()


class PhotosGetResponse(BaseModel):

    response: dict = Field()


class PhotosMarketAlbumUploadResponse(BaseModel):

    response: dict = Field()


class PhotosMarketUploadResponse(BaseModel):

    response: dict = Field()


class PhotosMessageUploadResponse(BaseModel):

    response: dict = Field()


class PhotosOwnerCoverUploadResponse(BaseModel):

    response: dict = Field()


class PhotosOwnerUploadResponse(BaseModel):

    response: dict = Field()


class PhotosPhotoUploadResponse(BaseModel):

    response: dict = Field()


class PhotosPutTagResponse(BaseModel):

    response: int = Field(
        description="Created tag ID",
    )


class PhotosSaveMarketAlbumPhotoResponse(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveMarketPhotoResponse(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveMessagesPhotoResponse(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveOwnerCoverPhotoResponse(BaseModel):

    response: dict = Field()


class PhotosSaveOwnerPhotoResponse(BaseModel):

    response: dict = Field()


class PhotosSaveWallPhotoResponse(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveResponse(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSearchResponse(BaseModel):

    response: dict = Field()


class PhotosWallUploadResponse(BaseModel):

    response: dict = Field()
