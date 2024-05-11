import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class PrettyCardsCreateResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class PrettyCardsDeleteResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class PrettyCardsEditResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class PrettyCardsGetByIdResponse(BaseModel):
    
    
    response: typing.List[PrettyCardsPrettyCardOrError] = Field(
        
        
        
    )
    
    







class PrettyCardsGetUploadURLResponse(BaseModel):
    
    
    response: str = Field(
        
        
        description="Upload URL",
        
        
    )
    
    







class PrettyCardsGetResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



