"""Tests utils/binary.py."""

from typing import List

import pytest

from gymboy.utils import (
    bcds_to_integer,
    bytes_bit_count,
    bytes_to_int,
    reduced_bcds_to_integer,
)


@pytest.mark.parametrize(
    argnames=["numbers", "expected"],
    argvalues=[
        ([0x00, 0x00], 0),
        ([0x00, 0x01], 1),
        ([0x00, 0x02], 1),
        ([0x12, 0x34], 5),
        ([0xFF, 0xFF], 16),
    ],
)
def test_bytes_bit_count(numbers: List[int], expected: int):
    """Tests the bytes_bit_count() method."""
    assert bytes_bit_count(numbers) == expected


@pytest.mark.parametrize(
    argnames=["numbers", "expected"],
    argvalues=[
        ([0x00, 0x00], 0),
        ([0x00, 0x01], 1),
        ([0x00, 0xFF], 255),
        ([0x12, 0x34], 4660),
        ([0xFF, 0xFF], 65535),
    ],
)
def test_bytes_to_int(numbers: List[int], expected: int):
    """Tests the bytes_to_int() method."""
    assert bytes_to_int(numbers) == expected


@pytest.mark.parametrize(
    argnames=["numbers", "expected"],
    argvalues=[
        ([0x00, 0x31, 0x75], 3175),
        ([0x00, 0x30, 0x00], 3000),
        ([0x01, 0x02, 0x03, 0x04], 1020304),
        ([0x01, 0x31, 0x99, 0x05], 1319905),
        ([0x12, 0x34, 0x56, 0x78], 12345678),
    ],
)
def test_bcds_to_integer(numbers: List[int], expected: int):
    """Tests the bcds_to_integer() method."""
    assert bcds_to_integer(numbers) == expected


@pytest.mark.parametrize(
    argnames=["numbers", "expected"],
    argvalues=[
        ([0x01, 0x02, 0x03, 0x04], 1234),
        ([0x00, 0x03, 0x00], 30),
        ([0x03, 0x00, 0x00], 300),
        ([0x09, 0x00, 0x01, 0x02], 9012),
        ([0x09, 0x09, 0x09, 0x09], 9999),
    ],
)
def test_reduced_bcds_to_integer(numbers: List[int], expected: int):
    """Tests the reduced_bcds_to_integer() method."""
    assert reduced_bcds_to_integer(numbers) == expected
