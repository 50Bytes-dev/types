import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class StoriesGetBannedExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesGetBannedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesGetByIdExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesGetPhotoUploadServerResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesGetStatsV5200Response(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesGetStatsResponse(BaseModel):
    
    
    response: 'StoriesStoryStats' = Field(
        
        
        
    )
    
    







class StoriesGetVideoUploadServerResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesGetViewersExtendedV5115Response(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesGetV5113Response(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesSaveResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class StoriesUploadResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



