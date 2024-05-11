import inspect

from vkbottle_types.codegen.responses.pages import *  # noqa: F403,F401

from .base_response import BaseResponse

_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if not (inspect.isclass(item) and issubclass(item, BaseResponse)):
        continue
    if item.__name__ == "BaseModel":
        continue
    item.model_rebuild()
    for parent in item.__bases__:
        if parent.__name__ == item.__name__:
            parent.model_fields.update(item.model_fields)
            parent.model_rebuild()
