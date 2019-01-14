from typing import (
    cast,
    Type,
    Union,
)

from eth_utils import (
    hexstr_if_str,
    to_bytes,
)


class HexBytes(bytes):
    '''
    This class is a *very* thin wrapper around the python
    built-in :class:`bytes` class. It has these three changes:

    1. Accepts hex strings as an initializing value
    2. Returns hex with prefix '0x' from :meth:`HexBytes.hex`
    3. The string representation at console is in hex
    '''
    def __new__(cls: Type[bytes], val: Union[bytes, int, str]) -> "HexBytes":
        bytesval = hexstr_if_str(to_bytes, val)
        return cast(HexBytes, super().__new__(cls, bytesval))  # type: ignore  # https://github.com/python/typeshed/issues/2686  # noqa: E501

    def hex(self) -> str:
        '''
        Just like :meth:`bytes.hex`, but prepends "0x"
        '''
        return '0x' + super().hex()

    def __repr__(self) -> str:
        return 'HexBytes(%r)' % self.hex()
