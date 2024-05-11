import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class AccountChangePasswordResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AccountGetActiveOffersResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AccountGetAppPermissionsResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="Permissions mask",
        
        
    )
    
    







class AccountGetBannedResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class AccountGetCountersResponse(BaseModel):
    
    
    response: 'AccountAccountCounters' = Field(
        
        
        
    )
    
    







class AccountGetInfoResponse(BaseModel):
    
    
    response: 'AccountInfo' = Field(
        
        
        
    )
    
    







class AccountGetProfileInfoResponse(BaseModel):
    
    
    response: 'AccountUserSettings' = Field(
        
        
        
    )
    
    







class AccountGetPushSettingsResponse(BaseModel):
    
    
    response: 'AccountPushSettings' = Field(
        
        
        
    )
    
    







class AccountSaveProfileInfoResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    



