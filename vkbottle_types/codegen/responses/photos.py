import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *


class PhotosCopyResponseModel(BaseModel):

    response: int = Field(
        description="Photo ID",
    )


class PhotosCopyResponse(BaseResponse):
    response: "PhotosCopyResponseModel"


class PhotosCreateAlbumResponseModel(BaseModel):

    response: "PhotosPhotoAlbumFull" = Field()


class PhotosCreateAlbumResponse(BaseResponse):
    response: "PhotosCreateAlbumResponseModel"


class PhotosCreateCommentResponseModel(BaseModel):

    response: int = Field(
        description="Created comment ID",
    )


class PhotosCreateCommentResponse(BaseResponse):
    response: "PhotosCreateCommentResponseModel"


class PhotosGetAlbumsCountResponseModel(BaseModel):

    response: int = Field(
        description="Albums number",
    )


class PhotosGetAlbumsCountResponse(BaseResponse):
    response: "PhotosGetAlbumsCountResponseModel"


class PhotosGetAlbumsResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetAlbumsResponse(BaseResponse):
    response: "PhotosGetAlbumsResponseModel"


class PhotosGetAllCommentsResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetAllCommentsResponse(BaseResponse):
    response: "PhotosGetAllCommentsResponseModel"


class PhotosGetAllResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetAllResponse(BaseResponse):
    response: "PhotosGetAllResponseModel"


class PhotosGetByIdResponseModel(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosGetByIdResponse(BaseResponse):
    response: "PhotosGetByIdResponseModel"


class PhotosGetCommentsExtendedResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetCommentsExtendedResponse(BaseResponse):
    response: "PhotosGetCommentsExtendedResponseModel"


class PhotosGetCommentsResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetCommentsResponse(BaseResponse):
    response: "PhotosGetCommentsResponseModel"


class PhotosGetMarketUploadServerResponseModel(BaseModel):

    response: "BaseUploadServer" = Field()


class PhotosGetMarketUploadServerResponse(BaseResponse):
    response: "PhotosGetMarketUploadServerResponseModel"


class PhotosGetMessagesUploadServerResponseModel(BaseModel):

    response: "PhotosPhotoUpload" = Field()


class PhotosGetMessagesUploadServerResponse(BaseResponse):
    response: "PhotosGetMessagesUploadServerResponseModel"


class PhotosGetNewTagsResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetNewTagsResponse(BaseResponse):
    response: "PhotosGetNewTagsResponseModel"


class PhotosGetTagsResponseModel(BaseModel):

    response: typing.List[PhotosPhotoTag] = Field()


class PhotosGetTagsResponse(BaseResponse):
    response: "PhotosGetTagsResponseModel"


class PhotosGetUploadServerResponseModel(BaseModel):

    response: "PhotosPhotoUpload" = Field()


class PhotosGetUploadServerResponse(BaseResponse):
    response: "PhotosGetUploadServerResponseModel"


class PhotosGetUserPhotosResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetUserPhotosResponse(BaseResponse):
    response: "PhotosGetUserPhotosResponseModel"


class PhotosGetWallUploadServerResponseModel(BaseModel):

    response: "PhotosPhotoUpload" = Field()


class PhotosGetWallUploadServerResponse(BaseResponse):
    response: "PhotosGetWallUploadServerResponseModel"


class PhotosGetResponseModel(BaseModel):

    response: dict = Field()


class PhotosGetResponse(BaseResponse):
    response: "PhotosGetResponseModel"


class PhotosMarketAlbumUploadResponseModel(BaseModel):

    response: dict = Field()


class PhotosMarketAlbumUploadResponse(BaseResponse):
    response: "PhotosMarketAlbumUploadResponseModel"


class PhotosMarketUploadResponseModel(BaseModel):

    response: dict = Field()


class PhotosMarketUploadResponse(BaseResponse):
    response: "PhotosMarketUploadResponseModel"


class PhotosMessageUploadResponseModel(BaseModel):

    response: dict = Field()


class PhotosMessageUploadResponse(BaseResponse):
    response: "PhotosMessageUploadResponseModel"


class PhotosOwnerCoverUploadResponseModel(BaseModel):

    response: dict = Field()


class PhotosOwnerCoverUploadResponse(BaseResponse):
    response: "PhotosOwnerCoverUploadResponseModel"


class PhotosOwnerUploadResponseModel(BaseModel):

    response: dict = Field()


class PhotosOwnerUploadResponse(BaseResponse):
    response: "PhotosOwnerUploadResponseModel"


class PhotosPhotoUploadResponseModel(BaseModel):

    response: dict = Field()


class PhotosPhotoUploadResponse(BaseResponse):
    response: "PhotosPhotoUploadResponseModel"


class PhotosPutTagResponseModel(BaseModel):

    response: int = Field(
        description="Created tag ID",
    )


class PhotosPutTagResponse(BaseResponse):
    response: "PhotosPutTagResponseModel"


class PhotosSaveMarketAlbumPhotoResponseModel(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveMarketAlbumPhotoResponse(BaseResponse):
    response: "PhotosSaveMarketAlbumPhotoResponseModel"


class PhotosSaveMarketPhotoResponseModel(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveMarketPhotoResponse(BaseResponse):
    response: "PhotosSaveMarketPhotoResponseModel"


class PhotosSaveMessagesPhotoResponseModel(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveMessagesPhotoResponse(BaseResponse):
    response: "PhotosSaveMessagesPhotoResponseModel"


class PhotosSaveOwnerCoverPhotoResponseModel(BaseModel):

    response: dict = Field()


class PhotosSaveOwnerCoverPhotoResponse(BaseResponse):
    response: "PhotosSaveOwnerCoverPhotoResponseModel"


class PhotosSaveOwnerPhotoResponseModel(BaseModel):

    response: dict = Field()


class PhotosSaveOwnerPhotoResponse(BaseResponse):
    response: "PhotosSaveOwnerPhotoResponseModel"


class PhotosSaveWallPhotoResponseModel(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveWallPhotoResponse(BaseResponse):
    response: "PhotosSaveWallPhotoResponseModel"


class PhotosSaveResponseModel(BaseModel):

    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveResponse(BaseResponse):
    response: "PhotosSaveResponseModel"


class PhotosSearchResponseModel(BaseModel):

    response: dict = Field()


class PhotosSearchResponse(BaseResponse):
    response: "PhotosSearchResponseModel"


class PhotosWallUploadResponseModel(BaseModel):

    response: dict = Field()


class PhotosWallUploadResponse(BaseResponse):
    response: "PhotosWallUploadResponseModel"
