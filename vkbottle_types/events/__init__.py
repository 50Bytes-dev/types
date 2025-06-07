from typing import Union

from .bot_typings import GroupTypes
from .enums import GroupEventType, UserEventType
from .user_typings import UserTypes
from .bot_events import MessageEvent

Event = Union[UserEventType, GroupEventType]


__all__ = ("GroupTypes", "GroupEventType", "UserEventType", "UserTypes", "Event", "MessageEvent")
