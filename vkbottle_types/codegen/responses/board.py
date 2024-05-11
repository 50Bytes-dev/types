import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class BoardAddTopicResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Topic ID",
        
        
    )
    
    







class BoardCreateCommentResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Comment ID",
        
        
    )
    
    







class BoardGetCommentsExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class BoardGetCommentsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class BoardGetTopicsExtendedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class BoardGetTopicsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



