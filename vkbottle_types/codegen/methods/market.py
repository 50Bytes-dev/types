import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.market import *
from vkbottle_types.responses.base import *

### OPTIONAL


class MarketCategory(BaseCategory):

    async def add(
        self,
        owner_id: int,
        name: str,
        description: str,
        category_id: int,
        price: typing.Optional[float] = None,
        old_price: typing.Optional[float] = None,
        deleted: typing.Optional[bool] = None,
        main_photo_id: typing.Optional[int] = None,
        photo_ids: typing.Optional[typing.List[int]] = None,
        video_ids: typing.Optional[typing.List[int]] = None,
        url: typing.Optional[str] = None,
        variant_ids: typing.Optional[typing.List[int]] = None,
        is_main_variant: typing.Optional[bool] = None,
        dimension_width: typing.Optional[int] = None,
        dimension_height: typing.Optional[int] = None,
        dimension_length: typing.Optional[int] = None,
        weight: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        stock_amount: typing.Optional[int] = None,
        **kwargs,
    ):
        """market.add method


        :param owner_id: ID of an item owner community.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param old_price:
        :param deleted: Item status ('1' - deleted, '0' - not deleted).
        :param main_photo_id: Cover photo ID.
        :param photo_ids: IDs of additional photos.
        :param video_ids: IDs of additional videos.
        :param url: Url for button in market item.
        :param variant_ids: IDs of properties variants.
        :param is_main_variant: Is main in their group.
        :param dimension_width:
        :param dimension_height:
        :param dimension_length:
        :param weight:
        :param sku:
        :param stock_amount:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.add", params)

        model = MarketAddResponse

        return model(**response).response

    async def add_album(
        self,
        owner_id: int,
        title: str,
        photo_id: typing.Optional[int] = None,
        main_album: typing.Optional[bool] = None,
        is_hidden: typing.Optional[bool] = None,
        **kwargs,
    ):
        """market.addAlbum method


        :param owner_id: ID of an item owner community.
        :param title: Collection title.
        :param photo_id: Cover photo ID.
        :param main_album: Set as main ('1' - set, '0' - no).
        :param is_hidden: Set as hidden
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.addAlbum", params)

        model = MarketAddAlbumResponse

        return model(**response).response

    async def add_property(
        self,
        group_id: int,
        title: str,
        **kwargs,
    ):
        """market.addProperty method


        :param group_id: Group id.
        :param title: Property name.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.addProperty", params)

        model = MarketAddPropertyResponse

        return model(**response).response

    async def add_property_variant(
        self,
        group_id: int,
        property_id: int,
        title: str,
        **kwargs,
    ):
        """market.addPropertyVariant method


        :param group_id: Group id.
        :param property_id: Property id.
        :param title: Variant name.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.addPropertyVariant", params)

        model = MarketAddPropertyVariantResponse

        return model(**response).response

    async def add_to_album(
        self,
        owner_id: int,
        item_ids: typing.List[int],
        album_ids: typing.List[int],
        **kwargs,
    ):
        """market.addToAlbum method


        :param owner_id: ID of an item owner community.
        :param item_ids:
        :param album_ids: Collections IDs to add item to.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.addToAlbum", params)

        model = BaseOkResponse

        return model(**response).response

    async def create_comment(
        self,
        owner_id: int,
        item_id: int,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        reply_to_comment: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        **kwargs,
    ):
        """market.createComment method


        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param message: Comment text (required if 'attachments' parameter is not specified)
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param reply_to_comment: ID of a comment to reply with current comment to.
        :param sticker_id: Sticker ID.
        :param guid: Random value to avoid resending one comment.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.createComment", params)

        model = MarketCreateCommentResponse

        return model(**response).response

    async def delete(
        self,
        owner_id: int,
        item_id: int,
        **kwargs,
    ):
        """market.delete method


        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.delete", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_album(
        self,
        owner_id: int,
        album_id: int,
        **kwargs,
    ):
        """market.deleteAlbum method


        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.deleteAlbum", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_comment(
        self,
        owner_id: int,
        comment_id: int,
        **kwargs,
    ):
        """market.deleteComment method


        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: comment id
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.deleteComment", params)

        model = BaseBoolResponse

        return model(**response).response

    async def delete_property(
        self,
        group_id: int,
        property_id: int,
        **kwargs,
    ):
        """market.deleteProperty method


        :param group_id: Group id.
        :param property_id: Property id.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.deleteProperty", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_property_variant(
        self,
        group_id: int,
        variant_id: int,
        **kwargs,
    ):
        """market.deletePropertyVariant method


        :param group_id: Group id.
        :param variant_id: Variant id.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.deletePropertyVariant", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit(
        self,
        owner_id: int,
        item_id: int,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        category_id: typing.Optional[int] = None,
        price: typing.Optional[float] = None,
        old_price: typing.Optional[float] = None,
        deleted: typing.Optional[bool] = None,
        main_photo_id: typing.Optional[int] = None,
        photo_ids: typing.Optional[typing.List[int]] = None,
        video_ids: typing.Optional[typing.List[int]] = None,
        url: typing.Optional[str] = None,
        variant_ids: typing.Optional[typing.List[int]] = None,
        is_main_variant: typing.Optional[bool] = None,
        dimension_width: typing.Optional[int] = None,
        dimension_height: typing.Optional[int] = None,
        dimension_length: typing.Optional[int] = None,
        weight: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        stock_amount: typing.Optional[int] = None,
        **kwargs,
    ):
        """market.edit method


        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param old_price:
        :param deleted: Item status ('1' - deleted, '0' - not deleted).
        :param main_photo_id: Cover photo ID.
        :param photo_ids: IDs of additional photos.
        :param video_ids: IDs of additional videos.
        :param url: Url for button in market item.
        :param variant_ids: IDs of properties variants.
        :param is_main_variant: Is main in their group.
        :param dimension_width:
        :param dimension_height:
        :param dimension_length:
        :param weight:
        :param sku:
        :param stock_amount:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.edit", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_album(
        self,
        owner_id: int,
        album_id: int,
        title: str,
        photo_id: typing.Optional[int] = None,
        main_album: typing.Optional[bool] = None,
        is_hidden: typing.Optional[bool] = None,
        **kwargs,
    ):
        """market.editAlbum method


        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        :param title: Collection title.
        :param photo_id: Cover photo id
        :param main_album: Set as main ('1' - set, '0' - no).
        :param is_hidden: Set as hidden
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.editAlbum", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_comment(
        self,
        owner_id: int,
        comment_id: int,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ):
        """market.editComment method


        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param message: New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.editComment", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_order(
        self,
        user_id: int,
        order_id: int,
        merchant_comment: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        track_number: typing.Optional[str] = None,
        payment_status: typing.Optional[str] = None,
        delivery_price: typing.Optional[int] = None,
        width: typing.Optional[int] = None,
        length: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        weight: typing.Optional[int] = None,
        comment_for_user: typing.Optional[str] = None,
        receipt_link: typing.Optional[str] = None,
        **kwargs,
    ):
        """market.editOrder method


        :param user_id:
        :param order_id:
        :param merchant_comment:
        :param status:
        :param track_number:
        :param payment_status:
        :param delivery_price:
        :param width:
        :param length:
        :param height:
        :param weight:
        :param comment_for_user:
        :param receipt_link:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.editOrder", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_property(
        self,
        group_id: int,
        property_id: int,
        title: str,
        **kwargs,
    ):
        """market.editProperty method


        :param group_id: Group id.
        :param property_id: Property id.
        :param title: Property name
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.editProperty", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_property_variant(
        self,
        group_id: int,
        variant_id: int,
        title: str,
        **kwargs,
    ):
        """market.editPropertyVariant method


        :param group_id: Group id.
        :param variant_id: Variant id.
        :param title: Variant name.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.editPropertyVariant", params)

        model = BaseOkResponse

        return model(**response).response

    async def filter_categories(
        self,
        category_id: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        count: typing.Optional[int] = 20,
        **kwargs,
    ):
        """market.filterCategories method


        :param category_id: Category_id filter categories
        :param query: Query filter categories
        :param count: Number of results to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.filterCategories", params)

        model = MarketGetCategoriesNewResponse

        return model(**response).response

    @typing.overload
    async def get(
        self,
        owner_id: int,
        extended: typing.Literal[True] = True,
        album_id: typing.Optional[int] = 0,
        count: typing.Optional[int] = 100,
        offset: typing.Optional[int] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        need_variants: typing.Optional[bool] = None,
        with_disabled: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ): ...

    async def get(
        self,
        owner_id: int,
        album_id: typing.Optional[int] = 0,
        count: typing.Optional[int] = 100,
        offset: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        need_variants: typing.Optional[bool] = None,
        with_disabled: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ):
        """market.get method


        :param owner_id: ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_id:
        :param count: Number of items to return.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' - method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        :param date_from: Items update date from (format: yyyy-mm-dd)
        :param date_to: Items update date to (format: yyyy-mm-dd)
        :param need_variants: Add variants to response if exist
        :param with_disabled: Add disabled items to response
        :param fields:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.get", params)

        model = self.get_model(
            ((("extended",), MarketGetExtendedResponse),),
            default=MarketGetResponse,
            params=params,
        )

        return model(**response).response

    async def get_album_by_id(
        self,
        owner_id: int,
        album_ids: typing.List[int],
        **kwargs,
    ):
        """market.getAlbumById method


        :param owner_id: identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_ids: collections identifiers to obtain data from
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getAlbumById", params)

        model = MarketGetAlbumByIdResponse

        return model(**response).response

    async def get_albums(
        self,
        owner_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 50,
        **kwargs,
    ):
        """market.getAlbums method


        :param owner_id: ID of an items owner community.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getAlbums", params)

        model = MarketGetAlbumsResponse

        return model(**response).response

    @typing.overload
    async def get_by_id(
        self,
        item_ids: typing.List[str],
        extended: typing.Literal[True] = True,
        **kwargs,
    ): ...

    async def get_by_id(
        self,
        item_ids: typing.List[str],
        extended: typing.Optional[bool] = None,
        **kwargs,
    ):
        """market.getById method


        :param item_ids: Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: '1' - to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getById", params)

        model = self.get_model(
            ((("extended",), MarketGetByIdExtendedResponse),),
            default=MarketGetByIdResponse,
            params=params,
        )

        return model(**response).response

    async def get_categories(
        self,
        group_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """market.getCategories method


        :param group_id: Group Id.
        :param album_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getCategories", params)

        model = MarketGetCategoriesNewResponse

        return model(**response).response

    async def get_comments(
        self,
        owner_id: int,
        item_id: int,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        sort: typing.Optional[str] = "asc",
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        **kwargs,
    ):
        """market.getComments method


        :param owner_id: ID of an item owner community
        :param item_id: Item ID.
        :param need_likes: '1' - to return likes info.
        :param start_comment_id: ID of a comment to start a list from (details below).
        :param offset:
        :param count: Number of results to return.
        :param sort: Sort order ('asc' - from old to new, 'desc' - from new to old)
        :param extended: '1' - comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
        :param fields: List of additional profile fields to return. See the [vk.com/dev/fields|details]
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getComments", params)

        model = MarketGetCommentsResponse

        return model(**response).response

    async def get_group_orders(
        self,
        group_id: typing.Optional[typing.Union["int", "str"]] = None,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 10,
        **kwargs,
    ):
        """market.getGroupOrders method


        :param group_id: ID or groups domain
        :param offset:
        :param count:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getGroupOrders", params)

        model = MarketGetGroupOrdersResponse

        return model(**response).response

    async def get_order_by_id(
        self,
        order_id: int,
        user_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        **kwargs,
    ):
        """market.getOrderById method


        :param order_id:
        :param user_id:
        :param extended:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getOrderById", params)

        model = MarketGetOrderByIdResponse

        return model(**response).response

    async def get_order_items(
        self,
        order_id: int,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 50,
        **kwargs,
    ):
        """market.getOrderItems method


        :param order_id:
        :param user_id:
        :param offset:
        :param count:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getOrderItems", params)

        model = MarketGetOrderItemsResponse

        return model(**response).response

    @typing.overload
    async def get_orders(
        self,
        extended: typing.Literal[True] = True,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 10,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        **kwargs,
    ): ...

    async def get_orders(
        self,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 10,
        extended: typing.Optional[bool] = None,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        **kwargs,
    ):
        """market.getOrders method


        :param offset:
        :param count:
        :param extended:
        :param date_from: Orders status updated date from (format: yyyy-mm-dd)
        :param date_to: Orders status updated date to (format: yyyy-mm-dd)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getOrders", params)

        model = self.get_model(
            ((("extended",), MarketGetOrdersExtendedResponse),),
            default=MarketGetOrdersResponse,
            params=params,
        )

        return model(**response).response

    async def get_product_photo_upload_server(
        self,
        group_id: int,
        **kwargs,
    ):
        """market.getProductPhotoUploadServer method


        :param group_id: Community ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getProductPhotoUploadServer", params)

        model = BaseGetUploadServerResponse

        return model(**response).response

    async def get_properties(
        self,
        group_id: int,
        **kwargs,
    ):
        """market.getProperties method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.getProperties", params)

        model = MarketGetPropertiesResponse

        return model(**response).response

    async def group_items(
        self,
        group_id: int,
        item_ids: typing.List[int],
        item_group_id: typing.Optional[int] = None,
        **kwargs,
    ):
        """market.groupItems method


        :param group_id: Group id.
        :param item_ids: Item ids.
        :param item_group_id: Items group id.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.groupItems", params)

        model = MarketGroupItemsResponse

        return model(**response).response

    async def remove_from_album(
        self,
        owner_id: int,
        item_id: int,
        album_ids: typing.List[int],
        **kwargs,
    ):
        """market.removeFromAlbum method


        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to remove item from.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.removeFromAlbum", params)

        model = BaseOkResponse

        return model(**response).response

    async def reorder_albums(
        self,
        owner_id: int,
        album_id: int,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
        **kwargs,
    ):
        """market.reorderAlbums method


        :param owner_id: ID of an item owner community.
        :param album_id: Collection ID.
        :param before: ID of a collection to place current collection before it.
        :param after: ID of a collection to place current collection after it.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.reorderAlbums", params)

        model = BaseOkResponse

        return model(**response).response

    async def reorder_items(
        self,
        owner_id: int,
        item_id: int,
        album_id: typing.Optional[int] = None,
        before: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
        **kwargs,
    ):
        """market.reorderItems method


        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_id: ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param before: ID of an item to place current item before it.
        :param after: ID of an item to place current item after it.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.reorderItems", params)

        model = BaseOkResponse

        return model(**response).response

    async def report(
        self,
        owner_id: int,
        item_id: int,
        reason: typing.Optional[int] = 0,
        **kwargs,
    ):
        """market.report method


        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param reason: Complaint reason. Possible values: *'0' - spam,, *'1' - child porn,, *'2' - extremism,, *'3' - violence,, *'4' - drugs propaganda,, *'5' - adult materials,, *'6' - insult.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.report", params)

        model = BaseOkResponse

        return model(**response).response

    async def report_comment(
        self,
        owner_id: int,
        comment_id: int,
        reason: int,
        **kwargs,
    ):
        """market.reportComment method


        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param reason: Complaint reason. Possible values: *'0' - spam,, *'1' - child porn,, *'2' - extremism,, *'3' - violence,, *'4' - drugs propaganda,, *'5' - adult materials,, *'6' - insult.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.reportComment", params)

        model = BaseOkResponse

        return model(**response).response

    async def restore(
        self,
        owner_id: int,
        item_id: int,
        **kwargs,
    ):
        """market.restore method


        :param owner_id: ID of an item owner community.
        :param item_id: Deleted item ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.restore", params)

        model = BaseOkResponse

        return model(**response).response

    async def restore_comment(
        self,
        owner_id: int,
        comment_id: int,
        **kwargs,
    ):
        """market.restoreComment method


        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: deleted comment id
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.restoreComment", params)

        model = BaseBoolResponse

        return model(**response).response

    async def save_product_photo(
        self,
        upload_response: str,
        **kwargs,
    ):
        """market.saveProductPhoto method


        :param upload_response: Upload response
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.saveProductPhoto", params)

        model = MarketPhotoIdResponse

        return model(**response).response

    @typing.overload
    async def search(
        self,
        owner_id: int,
        extended: typing.Literal[True] = True,
        album_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        sort: typing.Optional[int] = 0,
        rev: typing.Optional[int] = 1,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        status: typing.Optional[typing.List[int]] = None,
        need_variants: typing.Optional[bool] = None,
        **kwargs,
    ): ...

    async def search(
        self,
        owner_id: int,
        album_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        sort: typing.Optional[int] = 0,
        rev: typing.Optional[int] = 1,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        extended: typing.Optional[bool] = "0",
        status: typing.Optional[typing.List[int]] = None,
        need_variants: typing.Optional[bool] = None,
        **kwargs,
    ):
        """market.search method


        :param owner_id: ID of an items owner community.
        :param album_id:
        :param q: Search query, for example "pink slippers".
        :param price_from: Minimum item price value.
        :param price_to: Maximum item price value.
        :param sort:
        :param rev: '0' - do not use reverse order, '1' - use reverse order
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        :param extended: '1' - to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param status:
        :param need_variants: Add variants to response if exist
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.search", params)

        model = self.get_model(
            ((("extended",), MarketSearchExtendedResponse),),
            default=MarketSearchResponse,
            params=params,
        )

        return model(**response).response

    async def search_items(
        self,
        q: str,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 30,
        category_id: typing.Optional[int] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        sort_by: typing.Optional[int] = 3,
        sort_direction: typing.Optional[int] = 1,
        country: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
        **kwargs,
    ):
        """market.searchItems method


        :param q:
        :param offset:
        :param count:
        :param category_id:
        :param price_from:
        :param price_to:
        :param sort_by:
        :param sort_direction:
        :param country:
        :param city:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.searchItems", params)

        model = MarketSearchResponse

        return model(**response).response

    async def search_items_basic(
        self,
        q: str,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 30,
        category_id: typing.Optional[int] = None,
        price_from: typing.Optional[int] = None,
        price_to: typing.Optional[int] = None,
        sort_by: typing.Optional[int] = 3,
        sort_direction: typing.Optional[int] = 0,
        country: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
        only_my_groups: typing.Optional[bool] = None,
        **kwargs,
    ):
        """market.searchItemsBasic method


        :param q:
        :param offset:
        :param count:
        :param category_id:
        :param price_from:
        :param price_to:
        :param sort_by:
        :param sort_direction:
        :param country:
        :param city:
        :param only_my_groups:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.searchItemsBasic", params)

        model = MarketSearchBasicResponse

        return model(**response).response

    async def ungroup_items(
        self,
        group_id: int,
        item_group_id: int,
        **kwargs,
    ):
        """market.ungroupItems method


        :param group_id: Group id.
        :param item_group_id: Items group id.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("market.ungroupItems", params)

        model = BaseOkResponse

        return model(**response).response


__all__ = ("MarketCategory",)
