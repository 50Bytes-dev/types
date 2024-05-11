import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class VideoAddAlbumResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoChangeVideoAlbumsResponse(BaseModel):
    
    
    response: typing.List[int] = Field(
        
        
        
    )
    
    







class VideoCreateCommentResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Created comment ID",
        
        
    )
    
    







class VideoEditResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoGetAlbumByIdResponse(BaseModel):
    
    
    response: 'VideoVideoAlbumFull' = Field(
        
        
        
    )
    
    







class VideoGetAlbumsByVideoExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoGetAlbumsByVideoResponse(BaseModel):
    
    
    response: typing.List[int] = Field(
        
        
        
    )
    
    







class VideoGetAlbumsExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoGetAlbumsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoGetCommentsExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoGetCommentsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoGetLongPollServerResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoGetResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoLiveGetCategoriesResponse(BaseModel):
    
    
    response: typing.List[VideoLiveCategory] = Field(
        
        
        
    )
    
    







class VideoSaveResponse(BaseModel):
    
    
    response: 'VideoSaveResult' = Field(
        
        
        
    )
    
    







class VideoSearchExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoSearchResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoStartStreamingResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoStopStreamingResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class VideoUploadResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



