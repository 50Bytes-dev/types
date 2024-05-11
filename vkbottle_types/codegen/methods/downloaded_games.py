import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.downloaded_games import *
from vkbottle_types.responses.base import *
### OPTIONAL

class DownloadedGamesCategory(BaseCategory):
    
    

    async def get_paid_status(
        self,
        
        user_id: typing.Optional[int] = None ,
        
        **kwargs,
    ) -> DownloadedGamesPaidStatusResponse:
        """downloadedGames.getPaidStatus method
        
        
        :param user_id: 
        """
        params = self.get_set_params(locals())
        response = await self.api.request("downloadedGames.getPaidStatus", params)
        
        model = DownloadedGamesPaidStatusResponse
        
        return model(**response).response
    


__all__ = (
    "DownloadedGamesCategory",
)