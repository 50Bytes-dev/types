import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class FaveAddTagResponse(BaseModel):
    
    
    response: 'FaveTag' = Field(
        
        
        
    )
    
    







class FaveGetPagesResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class FaveGetTagsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class FaveGetExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class FaveGetResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



