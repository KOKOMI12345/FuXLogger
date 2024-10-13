import sys
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
# 通过判断版本来判断类型注解的支持性
if TYPE_CHECKING:
   if sys.version_info >= (3, 12):
       type Message = Union[str, bytes]
   else:
       Message = TypeVar('Message', str, bytes)
else:
    Message = TypeVar('Message', str, bytes)