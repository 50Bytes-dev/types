import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.polls import *
from vkbottle_types.responses.base import *

### OPTIONAL


class PollsCategory(BaseCategory):

    async def add_vote(
        self,
        poll_id: int,
        answer_ids: typing.List[int],
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        **kwargs,
    ) -> BaseBoolResponse:
        """polls.addVote method


        :param poll_id: Poll ID.
        :param answer_ids:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def create(
        self,
        question: typing.Optional[str] = None,
        is_anonymous: typing.Optional[bool] = None,
        is_multiple: typing.Optional[bool] = None,
        end_date: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        app_id: typing.Optional[int] = None,
        add_answers: typing.Optional[str] = None,
        photo_id: typing.Optional[int] = None,
        background_id: typing.Optional[str] = None,
        disable_unvote: typing.Optional[bool] = None,
        **kwargs,
    ) -> PollsCreateResponse:
        """polls.create method


        :param question: question text
        :param is_anonymous: '1' - anonymous poll, participants list is hidden,, '0' - public poll, participants list is available,, Default value is '0'.
        :param is_multiple:
        :param end_date:
        :param owner_id: If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
        :param app_id:
        :param add_answers: available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
        :param photo_id:
        :param background_id:
        :param disable_unvote:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PollsCreateResponse

        return model(**response).response

    async def delete_vote(
        self,
        poll_id: int,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        **kwargs,
    ) -> BaseBoolResponse:
        """polls.deleteVote method


        :param poll_id: Poll ID.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def edit(
        self,
        poll_id: int,
        owner_id: typing.Optional[int] = None,
        question: typing.Optional[str] = None,
        add_answers: typing.Optional[str] = None,
        edit_answers: typing.Optional[str] = None,
        delete_answers: typing.Optional[str] = None,
        end_date: typing.Optional[int] = None,
        photo_id: typing.Optional[int] = None,
        background_id: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponse:
        """polls.edit method


        :param poll_id: edited poll's id
        :param owner_id: poll owner id
        :param question: new question text
        :param add_answers: answers list, for example: , "["yes","no","maybe"]"
        :param edit_answers: object containing answers that need to be edited,, key - answer id, value - new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
        :param delete_answers: list of answer ids to be deleted. For example: "[382967099, 382967103]"
        :param end_date:
        :param photo_id:
        :param background_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def get_backgrounds(
        self,
        **kwargs,
    ) -> PollsGetBackgroundsResponse:
        """polls.getBackgrounds method"""
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PollsGetBackgroundsResponse

        return model(**response).response

    async def get_by_id(
        self,
        poll_id: int,
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        extended: typing.Optional[bool] = None,
        friends_count: typing.Optional[int] = 3,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> PollsGetByIdResponse:
        """polls.getById method


        :param poll_id: Poll ID.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: '1' - poll is in a board, '0' - poll is on a wall. '0' by default.
        :param extended:
        :param friends_count:
        :param fields:
        :param name_case:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PollsGetByIdResponse

        return model(**response).response

    async def get_photo_upload_server(
        self,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseGetUploadServerResponse:
        """polls.getPhotoUploadServer method


        :param owner_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseGetUploadServerResponse

        return model(**response).response

    @typing.overload
    async def get_voters(
        self,
        poll_id: int,
        answer_ids: typing.List[int],
        fields: typing.List[UsersFields],
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        friends_only: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> PollsGetVotersFieldsResponse: ...

    async def get_voters(
        self,
        poll_id: int,
        answer_ids: typing.List[int],
        owner_id: typing.Optional[int] = None,
        is_board: typing.Optional[bool] = None,
        friends_only: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> PollsGetVotersResponse:
        """polls.getVoters method


        :param poll_id: Poll ID.
        :param answer_ids: Answer IDs.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board:
        :param friends_only: '1' - to return only current user's friends, '0' - to return all users (default),
        :param offset: Offset needed to return a specific subset of voters. '0' - (default)
        :param count: Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' - (default)
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: Case for declension of user name and surname: , 'nom' - nominative (default) , 'gen' - genitive , 'dat' - dative , 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("fields",), PollsGetVotersFieldsResponse),),
            default=PollsGetVotersResponse,
            params=params,
        )

        return model(**response).response

    async def save_photo(
        self,
        photo: typing.Optional[str] = None,
        hash: typing.Optional[str] = None,
        **kwargs,
    ) -> PollsSavePhotoResponse:
        """polls.savePhoto method


        :param photo:
        :param hash:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PollsSavePhotoResponse

        return model(**response).response


__all__ = ("PollsCategory",)
