import binascii
from typing import (
    Union,
)


def to_bytes(val: Union[bool, bytearray, bytes, int, str]) -> bytes:
    """
    Equivalent to: `eth_utils.hexstr_if_str(eth_utils.to_bytes, val)` .

    Convert a hex string, integer, or bool, to a bytes representation.
    Alternatively, pass through bytes or bytearray as a bytes value.
    """
    type_var = type(val)
    if type_var is bytes:
        return val  # type: ignore
    elif type_var is str:
        return hexstr_to_bytes(val)  # type: ignore
    elif type_var is bytearray:
        return bytes(val)  # type: ignore
    elif type_var is int:
        if val < 0:  # type: ignore
            raise ValueError(f"Cannot convert negative integer {val} to bytes")  # type: ignore
        else:
            return hexstr_to_bytes(hex(val))  # type: ignore
    elif type_var is bool:
        return b"\x01" if val else b"\x00"
    else:
        raise TypeError(f"Cannot convert {val!r} of type {type_var} to bytes")


def hexstr_to_bytes(hexstr: str) -> bytes:
    if hexstr.startswith(("0x", "0X")):
        non_prefixed_hex = hexstr[2:]
    else:
        non_prefixed_hex = hexstr

    # if the hex string is odd-length, then left-pad it to an even length
    if len(hexstr) % 2:
        padded_hex = "0" + non_prefixed_hex
    else:
        padded_hex = non_prefixed_hex

    try:
        ascii_hex = padded_hex.encode('ascii')
    except UnicodeDecodeError:
        raise ValueError(f"hex string {padded_hex} may only contain [0-9a-fA-F] characters")
    else:
        return binascii.unhexlify(ascii_hex)
