import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.notes import *
from vkbottle_types.responses.base import *

### OPTIONAL


class NotesCategory(BaseCategory):

    async def add(
        self,
        title: str,
        text: str,
        privacy_view: typing.Optional[typing.List[str]] = "all",
        privacy_comment: typing.Optional[typing.List[str]] = "all",
        **kwargs,
    ):
        """notes.add method


        :param title: Note title.
        :param text: Note text.
        :param privacy_view:
        :param privacy_comment:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.add", params)

        model = NotesAddResponse

        return model(**response).response

    async def create_comment(
        self,
        note_id: int,
        message: str,
        owner_id: typing.Optional[int] = None,
        reply_to: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        **kwargs,
    ):
        """notes.createComment method


        :param note_id: Note ID.
        :param message: Comment text.
        :param owner_id: Note owner ID.
        :param reply_to: ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param guid:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.createComment", params)

        model = NotesCreateCommentResponse

        return model(**response).response

    async def delete(
        self,
        note_id: int,
        **kwargs,
    ):
        """notes.delete method


        :param note_id: Note ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.delete", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """notes.deleteComment method


        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.deleteComment", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit(
        self,
        note_id: int,
        title: str,
        text: str,
        privacy_view: typing.Optional[typing.List[str]] = "all",
        privacy_comment: typing.Optional[typing.List[str]] = "all",
        **kwargs,
    ):
        """notes.edit method


        :param note_id: Note ID.
        :param title: Note title.
        :param text: Note text.
        :param privacy_view:
        :param privacy_comment:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.edit", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        message: str,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """notes.editComment method


        :param comment_id: Comment ID.
        :param message: New comment text.
        :param owner_id: Note owner ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.editComment", params)

        model = BaseOkResponse

        return model(**response).response

    async def get(
        self,
        note_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        sort: typing.Optional[int] = 0,
        **kwargs,
    ):
        """notes.get method


        :param note_ids: Note IDs.
        :param user_id: Note owner ID.
        :param offset:
        :param count: Number of notes to return.
        :param sort:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.get", params)

        model = NotesGetResponse

        return model(**response).response

    async def get_by_id(
        self,
        note_id: int,
        owner_id: typing.Optional[int] = None,
        need_wiki: typing.Optional[bool] = 0,
        **kwargs,
    ):
        """notes.getById method


        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param need_wiki:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.getById", params)

        model = NotesGetByIdResponse

        return model(**response).response

    async def get_comments(
        self,
        note_id: int,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[int] = 0,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        **kwargs,
    ):
        """notes.getComments method


        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param sort:
        :param offset:
        :param count: Number of comments to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.getComments", params)

        model = NotesGetCommentsResponse

        return model(**response).response

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """notes.restoreComment method


        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("notes.restoreComment", params)

        model = BaseOkResponse

        return model(**response).response


__all__ = ("NotesCategory",)
