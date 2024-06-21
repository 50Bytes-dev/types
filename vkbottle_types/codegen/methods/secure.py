import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.secure import *
from vkbottle_types.responses.base import *

### OPTIONAL


class SecureCategory(BaseCategory):

    async def add_app_event(
        self,
        activity_id: int,
        user_id: typing.Optional[int] = None,
        value: typing.Optional[int] = None,
        **kwargs,
    ):
        """secure.addAppEvent method


        :param activity_id: there are 2 default activities: , * 1 - level. Works similar to ,, * 2 - points, saves points amount, Any other value is for saving completed missions
        :param user_id: ID of a user to save the data
        :param value: depends on activity_id: * 1 - number, current level number,, * 2 - number, current user's points amount, , Any other value is ignored
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.addAppEvent", params)

        model = BaseOkResponse

        return model(**response).response

    async def check_token(
        self,
        token: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        **kwargs,
    ):
        """secure.checkToken method


        :param token: client 'access_token'
        :param ip: user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.checkToken", params)

        model = SecureCheckTokenResponse

        return model(**response).response

    async def get_app_balance(
        self,
        **kwargs,
    ):
        """secure.getAppBalance method"""
        params = self.get_set_params(locals())
        response = await self.api.request("secure.getAppBalance", params)

        model = SecureGetAppBalanceResponse

        return model(**response).response

    async def get_s_m_s_history(
        self,
        user_id: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = 1000,
        **kwargs,
    ):
        """secure.getSMSHistory method


        :param user_id:
        :param date_from: filter by start date. It is set as UNIX-time.
        :param date_to: filter by end date. It is set as UNIX-time.
        :param limit: number of returned posts. By default - 1000.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.getSMSHistory", params)

        model = SecureGetSMSHistoryResponse

        return model(**response).response

    async def get_transactions_history(
        self,
        type: typing.Optional[int] = None,
        uid_from: typing.Optional[int] = None,
        uid_to: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = 1000,
        **kwargs,
    ):
        """secure.getTransactionsHistory method


        :param type:
        :param uid_from:
        :param uid_to:
        :param date_from:
        :param date_to:
        :param limit:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.getTransactionsHistory", params)

        model = SecureGetTransactionsHistoryResponse

        return model(**response).response

    async def get_user_level(
        self,
        user_ids: typing.List[int],
        **kwargs,
    ):
        """secure.getUserLevel method


        :param user_ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.getUserLevel", params)

        model = SecureGetUserLevelResponse

        return model(**response).response

    async def give_event_sticker(
        self,
        user_ids: typing.List[int],
        achievement_id: int,
        **kwargs,
    ):
        """secure.giveEventSticker method


        :param user_ids:
        :param achievement_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.giveEventSticker", params)

        model = SecureGiveEventStickerResponse

        return model(**response).response

    async def send_notification(
        self,
        message: str,
        user_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
        notification_id: typing.Optional[int] = 0,
        promo_id: typing.Optional[int] = 0,
        **kwargs,
    ):
        """secure.sendNotification method


        :param message: notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :param user_ids:
        :param user_id:
        :param notification_id:
        :param promo_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendNotification", params)

        model = SecureSendNotificationResponse

        return model(**response).response

    async def send_s_m_s_notification(
        self,
        user_id: int,
        message: str,
        **kwargs,
    ):
        """secure.sendSMSNotification method


        :param user_id: ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        :param message: 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendSMSNotification", params)

        model = BaseOkResponse

        return model(**response).response

    @typing.overload
    async def set_counter(
        self,
        counters: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        counter: typing.Optional[int] = None,
        increment: typing.Optional[bool] = None,
        **kwargs,
    ): ...

    @typing.overload
    async def set_counter(
        self,
        counters: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        counter: typing.Optional[int] = None,
        increment: typing.Optional[bool] = None,
        **kwargs,
    ): ...

    async def set_counter(
        self,
        counters: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        counter: typing.Optional[int] = None,
        increment: typing.Optional[bool] = None,
        **kwargs,
    ):
        """secure.setCounter method


        :param counters:
        :param user_id:
        :param counter: counter value.
        :param increment:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("secure.setCounter", params)

        model = self.get_model(
            (
                (("response_integer",), BaseBoolResponse),
                (("response_array",), SecureSetCounterArrayResponse),
            ),
            default=None,
            params=params,
        )

        return model(**response).response


__all__ = ("SecureCategory",)
