import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.likes import *
from vkbottle_types.responses.base import *

### OPTIONAL


class LikesCategory(BaseCategory):

    async def add(
        self,
        type: str,
        item_id: int,
        owner_id: typing.Optional[int] = None,
        access_key: typing.Optional[str] = None,
        from_group: typing.Optional[bool] = None,
        **kwargs,
    ) -> LikesAddResponseModel:
        """likes.add method


        :param type: Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion, 'sitepage' - page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param item_id: Object ID.
        :param owner_id: ID of the user or community that owns the object.
        :param access_key: Access key required for an object owned by a private entity.
        :param from_group: Impersonate group
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LikesAddResponse

        return model(**response).response

    async def delete(
        self,
        type: str,
        item_id: int,
        owner_id: typing.Optional[int] = None,
        access_key: typing.Optional[str] = None,
        from_group: typing.Optional[bool] = None,
        **kwargs,
    ) -> LikesDeleteResponseModel:
        """likes.delete method


        :param type: Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion, 'sitepage' - page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param item_id: Object ID.
        :param owner_id: ID of the user or community that owns the object.
        :param access_key: Access key required for an object owned by a private entity.
        :param from_group: Impersonate group
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LikesDeleteResponse

        return model(**response).response

    @typing.overload
    async def get_list(
        self,
        type: str,
        extended: typing.Literal[True] = True,
        owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        page_url: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        friends_only: typing.Optional[int] = 0,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        skip_own: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> LikesGetListExtendedResponseModel: ...

    async def get_list(
        self,
        type: str,
        owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        page_url: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        friends_only: typing.Optional[int] = 0,
        extended: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        skip_own: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> LikesGetListResponseModel:
        """likes.getList method


        :param type: , Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion, 'sitepage' - page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param owner_id: ID of the user, community, or application that owns the object. If the 'type' parameter is set as 'sitepage', the application ID is passed as 'owner_id'. Use negative value for a community id. If the 'type' parameter is not set, the 'owner_id' is assumed to be either the current user or the same application ID as if the 'type' parameter was set to 'sitepage'.
        :param item_id: Object ID. If 'type' is set as 'sitepage', 'item_id' can include the 'page_id' parameter value used during initialization of the [vk.com/dev/Like|Like widget].
        :param page_url: URL of the page where the [vk.com/dev/Like|Like widget] is installed. Used instead of the 'item_id' parameter.
        :param filter: Filters to apply: 'likes' - returns information about all users who liked the object (default), 'copies' - returns information only about users who told their friends about the object
        :param friends_only: Specifies which users are returned: '1' - to return only the current user's friends, '0' - to return all users (default)
        :param extended: Specifies whether extended information will be returned. '1' - to return extended information about users and communities from the 'Likes' list, '0' - to return no additional information (default)
        :param offset: Offset needed to select a specific subset of users.
        :param count: Number of user IDs to return (maximum '1000'). Default is '100' if 'friends_only' is set to '0', otherwise, the default is '10' if 'friends_only' is set to '1'.
        :param skip_own:
        :param fields:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), LikesGetListExtendedResponse),),
            default=LikesGetListResponse,
            params=params,
        )

        return model(**response).response

    async def is_liked(
        self,
        type: str,
        item_id: int,
        user_id: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ) -> LikesIsLikedResponseModel:
        """likes.isLiked method


        :param type: Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion
        :param item_id: Object ID.
        :param user_id: User ID.
        :param owner_id: ID of the user or community that owns the object.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LikesIsLikedResponse

        return model(**response).response


__all__ = ("LikesCategory",)
