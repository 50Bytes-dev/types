import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class SecureCheckTokenResponse(BaseModel):
    
    
    response: 'SecureTokenChecked' = Field(
        
        
        
    )
    
    







class SecureGetAppBalanceResponse(BaseModel):
    
    
    response: int = Field(
        
        
        description="App balance",
        
        
    )
    
    







class SecureGetSMSHistoryResponse(BaseModel):
    
    
    response: typing.List[SecureSmsNotification] = Field(
        
        
        
    )
    
    







class SecureGetTransactionsHistoryResponse(BaseModel):
    
    
    response: typing.List[SecureTransaction] = Field(
        
        
        
    )
    
    







class SecureGetUserLevelResponse(BaseModel):
    
    
    response: typing.List[SecureLevel] = Field(
        
        
        
    )
    
    







class SecureGiveEventStickerResponse(BaseModel):
    
    
    response: typing.List[SecureGiveEventStickerItem] = Field(
        
        
        
    )
    
    







class SecureSendNotificationResponse(BaseModel):
    
    
    response: typing.List[int] = Field(
        
        
        
    )
    
    







class SecureSetCounterArrayResponse(BaseModel):
    
    
    response: typing.List[SecureSetCounterItem] = Field(
        
        
        
    )
    
    



