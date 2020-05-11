from eth_utils import (
    decode_hex,
    remove_0x_prefix,
)
from hypothesis import (
    given,
    strategies as st,
)
import pytest

from hexbytes import (
    HexBytes,
)

hexstr_strategy = st.from_regex(r'\A(0[xX])?[0-9a-fA-F]*\Z')


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


@given(st.binary(), st.integers())
def test_hexbytes_index(primitive, index):
    hexbytes = HexBytes(primitive)
    if index >= len(primitive) or index < -1 * len(primitive):
        with pytest.raises(IndexError):
            hexbytes[index]
    else:
        assert hexbytes[index] == primitive[index]


@given(st.binary(), st.integers(), st.integers())
def test_slice(primitive, start, stop):
    hexbytes = HexBytes(primitive)
    expected = HexBytes(primitive[start:stop])
    assert hexbytes[start:stop] == expected


@given(st.binary(), st.integers(), st.integers(), st.integers())
def test_slice_stepped(primitive, start, stop, step):
    hexbytes = HexBytes(primitive)
    if step == 0:
        step = None
    expected = HexBytes(primitive[start:stop:step])
    assert hexbytes[start:stop:step] == expected
