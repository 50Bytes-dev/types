import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class DocsAddResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Document ID",
        
        
    )
    
    







class DocsDocUploadResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class DocsGetByIdResponse(BaseModel):
    
    
    response: typing.List[DocsDoc] = Field(
        
        
        
    )
    
    







class DocsGetTypesResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class DocsGetUploadServerResponse(BaseModel):
    
    
    response: 'BaseUploadServer' = Field(
        
        
        
    )
    
    







class DocsGetResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class DocsSaveResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class DocsSearchResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



