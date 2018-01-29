from eth_utils import (
    hexstr_if_str,
    to_bytes,
)


class HexBytes(bytes):
    def __new__(cls, val):
        bytesval = hexstr_if_str(to_bytes, val)
        return super().__new__(cls, bytesval)

    def hex(self):
        return '0x' + super().hex()

    def __repr__(self):
        return 'HexBytes(%r)' % self.hex()
