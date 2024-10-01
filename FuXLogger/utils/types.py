import sys

# 通过判断版本来判断类型注解的支持性
if sys.version_info >= (3, 12):
    from typing import Union
    type Message = Union[str, bytes]
else:
    from typing import TypeVar
    Message = TypeVar('Message', str, bytes)