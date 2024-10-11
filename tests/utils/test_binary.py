"""Tests utils/binary.py."""

import unittest

from gymboy.utils import (
    bcds_to_integer,
    bytes_bit_count,
    bytes_to_int,
    reduced_bcds_to_integer,
)


class TestBinary(unittest.TestCase):
    """Tests the methods under binary.py."""

    def test_bytes_bit_count(self):
        """Tests the bytes_bit_count() method."""
        numbers1 = [0x00, 0x00]
        numbers2 = [0x00, 0x01]
        numbers3 = [0x00, 0x02]
        numbers4 = [0x12, 0x34]
        numbers5 = [0xFF, 0xFF]

        result1 = bytes_bit_count(numbers1)
        result2 = bytes_bit_count(numbers2)
        result3 = bytes_bit_count(numbers3)
        result4 = bytes_bit_count(numbers4)
        result5 = bytes_bit_count(numbers5)

        self.assertEqual(result1, 0)
        self.assertEqual(result2, 1)
        self.assertEqual(result3, 1)
        self.assertEqual(result4, 5)
        self.assertEqual(result5, 16)

    def test_bytes_to_int(self):
        """Tests the bytes_to_int() method."""
        numbers1 = [0x00, 0x00]
        numbers2 = [0x00, 0x01]
        numbers3 = [0x00, 0xFF]
        numbers4 = [0x12, 0x34]
        numbers5 = [0xFF, 0xFF]

        result1 = bytes_to_int(numbers1)
        result2 = bytes_to_int(numbers2)
        result3 = bytes_to_int(numbers3)
        result4 = bytes_to_int(numbers4)
        result5 = bytes_to_int(numbers5)

        self.assertEqual(result1, 0)
        self.assertEqual(result2, 1)
        self.assertEqual(result3, 255)
        self.assertEqual(result4, 4660)
        self.assertEqual(result5, 65535)

    def test_bcds_to_integer(self):
        """Tests the bcds_to_integer() method."""
        numbers1 = [0x00, 0x31, 0x75]
        numbers2 = [0x00, 0x30, 0x00]
        numbers3 = [0x01, 0x02, 0x03, 0x04]
        numbers4 = [0x01, 0x31, 0x99, 0x05]
        numbers5 = [0x12, 0x34, 0x56, 0x78]

        result1 = bcds_to_integer(numbers1)
        result2 = bcds_to_integer(numbers2)
        result3 = bcds_to_integer(numbers3)
        result4 = bcds_to_integer(numbers4)
        result5 = bcds_to_integer(numbers5)

        self.assertEqual(result1, 3175)
        self.assertEqual(result2, 3000)
        self.assertEqual(result3, 1020304)
        self.assertEqual(result4, 1319905)
        self.assertEqual(result5, 12345678)

    def test_reduced_bcds_to_integer(self):
        """Tests the reduced_bcds_to_integer() method."""
        numbers1 = [0x01, 0x02, 0x03, 0x04]
        numbers2 = [0x00, 0x03, 0x00]
        numbers3 = [0x03, 0x00, 0x00]
        numbers4 = [0x09, 0x00, 0x01, 0x02]
        numbers5 = [0x09, 0x09, 0x09, 0x09]

        result1 = reduced_bcds_to_integer(numbers1)
        result2 = reduced_bcds_to_integer(numbers2)
        result3 = reduced_bcds_to_integer(numbers3)
        result4 = reduced_bcds_to_integer(numbers4)
        result5 = reduced_bcds_to_integer(numbers5)

        self.assertEqual(result1, 1234)
        self.assertEqual(result2, 30)
        self.assertEqual(result3, 300)
        self.assertEqual(result4, 9012)
        self.assertEqual(result5, 9999)


if __name__ == "__main__":
    unittest.main()
