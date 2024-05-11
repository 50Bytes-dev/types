import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class AppWidgetsGetAppImageUploadServerResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppWidgetsGetAppImagesResponse(BaseModel):
    
    
    response: 'AppWidgetsPhotos' = Field(
        
        
        
    )
    
    







class AppWidgetsGetGroupImageUploadServerResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AppWidgetsGetGroupImagesResponse(BaseModel):
    
    
    response: 'AppWidgetsPhotos' = Field(
        
        
        
    )
    
    







class AppWidgetsGetImagesByIdResponse(BaseModel):
    
    
    response: typing.List[AppWidgetsPhoto] = Field(
        
        
        
    )
    
    







class AppWidgetsSaveAppImageResponse(BaseModel):
    
    
    response: 'AppWidgetsPhoto' = Field(
        
        
        
    )
    
    







class AppWidgetsSaveGroupImageResponse(BaseModel):
    
    
    response: 'AppWidgetsPhoto' = Field(
        
        
        
    )
    
    



