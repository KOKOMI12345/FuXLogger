import sys
from typing import TypeVar
from typing import Union
# 通过判断版本来判断类型注解的支持性


if sys.version_info <= (3, 9):
   Message = TypeVar("Message", str, bytes)
elif sys.version_info <= (3, 10):
   Message = Union[str, bytes]
elif sys.version_info >= (3, 12):
   type Message = Union[str, bytes]
else:
   Message = TypeVar("Message", str, bytes)