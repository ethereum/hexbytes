import pytest

from eth_utils import (
    decode_hex,
    remove_0x_prefix,
    to_bytes as standard_to_bytes,
)
from hypothesis import (
    given,
    strategies as st,
)

from hexbytes import (
    HexBytes,
)

hexstr_strategy = st.from_regex(r"\A(0[xX])?[0-9a-fA-F]*\Z")


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


@given(st.binary())
def test_bytearray_inputs(primitive):
    byte_array_input = bytearray(primitive)
    wrapped = HexBytes(byte_array_input)
    assert_equal(wrapped, primitive)


@given(st.binary())
def test_memoryview_inputs(primitive):
    memoryview_input = memoryview(primitive)
    wrapped = HexBytes(memoryview_input)
    assert_equal(wrapped, primitive)


@pytest.mark.parametrize(
    "boolval, expected_repr",
    (
        (True, "HexBytes('0x01')"),
        (False, "HexBytes('0x00')"),
    ),
)
def test_bool_inputs(boolval, expected_repr):
    wrapped = HexBytes(boolval)
    assert repr(wrapped) == expected_repr
    assert_equal(wrapped, standard_to_bytes(boolval))


@given(st.integers(max_value=-1))
def test_invalid_integer_inputs(integer):
    with pytest.raises(ValueError) as exc_info:
        HexBytes(integer)

    message = str(exc_info.value)
    assert "negative" in message
    assert str(integer) in message


@given(st.integers(min_value=0))
def test_integer_inputs(integer):
    wrapped = HexBytes(integer)
    assert hex(integer)[2:] in repr(wrapped)
    assert_equal(wrapped, standard_to_bytes(integer))


@given(hexstr_strategy)
def test_hex_inputs(hex_input):
    wrapped = HexBytes(hex_input)
    if len(hex_input) % 2 == 0:
        even_hex_input = hex_input
    else:
        even_hex_input = "0" + remove_0x_prefix(hex_input)
    expected = decode_hex(even_hex_input)
    assert_equal(wrapped, expected)


def test_pretty_output():
    hb = HexBytes(b"\x0F\x1a")
    assert repr(hb) == "HexBytes('0x0f1a')"


def test_does_not_break_bytes_hex():
    hb = HexBytes(b"\x0F\x1a")
    assert hb.hex() == "0f1a"


def test_to_0x_hex():
    hb = HexBytes(b"\x0F\x1a")
    assert hb.to_0x_hex() == "0x0f1a"


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
