import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import *





class OrdersChangeStateResponse(BaseModel):
    
    
    response: str = Field(
        
        
        description="New state",
        
        
    )
    
    







class OrdersGetAmountResponse(BaseModel):
    
    
    response: typing.List[OrdersAmount] = Field(
        
        
        
    )
    
    







class OrdersGetByIdResponse(BaseModel):
    
    
    response: typing.List[OrdersOrder] = Field(
        
        
        
    )
    
    







class OrdersGetUserSubscriptionByIdResponse(BaseModel):
    
    
    response: 'OrdersSubscription' = Field(
        
        
        
    )
    
    







class OrdersGetUserSubscriptionsResponse(BaseModel):
    
    
    response: dict = Field(
        
        
        
    )
    
    







class OrdersGetResponse(BaseModel):
    
    
    response: typing.List[OrdersOrder] = Field(
        
        
        
    )
    
    



