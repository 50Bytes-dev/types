import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class UtilsCheckLinkResponse(BaseModel):
    
    
    response: 'UtilsLinkChecked' = Field(
        
        
        
    )
    
    







class UtilsGetLastShortenedLinksResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class UtilsGetLinkStatsExtendedResponse(BaseModel):
    
    
    response: 'UtilsLinkStatsExtended' = Field(
        
        
        
    )
    
    







class UtilsGetLinkStatsResponse(BaseModel):
    
    
    response: 'UtilsLinkStats' = Field(
        
        
        
    )
    
    







class UtilsGetServerTimeResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Time as Unixtime",
        
        
    )
    
    







class UtilsGetShortLinkResponse(BaseModel):
    
    
    response: 'UtilsShortLink' = Field(
        
        
        
    )
    
    







class UtilsResolveScreenNameResponse(BaseModel):
    
    
    response: 'UtilsDomainResolved' = Field(
        
        
        
    )
    
    



