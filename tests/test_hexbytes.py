from eth_utils import (
    decode_hex,
    remove_0x_prefix,
)
from hypothesis import (
    given,
    strategies as st,
)

from hexbytes import (
    HexBytes,
)

hexstr_strategy = st.from_regex('\A(0[xX])?[0-9a-fA-F]*\Z')


def assert_equal(hexbytes, bytes_expected):
    assert hexbytes == bytes_expected
    assert len(hexbytes) == len(bytes_expected)
    for byte_actual, byte_expected in zip(hexbytes, bytes_expected):
        assert byte_actual == byte_expected
    assert bytes(hexbytes) == bytes_expected


@given(st.binary())
def test_bytes_inputs(primitive):
    wrapped = HexBytes(primitive)
    assert_equal(wrapped, primitive)


@given(hexstr_strategy)
def test_hex_inputs(hex_input):
    wrapped = HexBytes(hex_input)
    if len(hex_input) % 2 == 0:
        even_hex_input = hex_input
    else:
        even_hex_input = '0' + remove_0x_prefix(hex_input)
    expected = decode_hex(even_hex_input)
    assert_equal(wrapped, expected)


def test_pretty_output():
    hb = HexBytes(b'\x0F\x1a')
    assert repr(hb) == "HexBytes('0x0f1a')"
