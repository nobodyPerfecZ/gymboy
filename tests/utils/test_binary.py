import unittest

from gymboy.utils.binary import *


class TestBinary(unittest.TestCase):
    """Tests the methods under binary.py."""

    def test_bytes_bit_count(self):
        """Tests the bytes_bit_count() method."""
        numbers1 = [0x00, 0x00]
        numbers2 = [0x12, 0x34]
        numbers3 = [0xFF, 0xFF]

        result1 = bytes_bit_count(numbers1)
        result2 = bytes_bit_count(numbers2)
        result3 = bytes_bit_count(numbers3)

        self.assertEqual(result1, 0)
        self.assertEqual(result2, 5)
        self.assertEqual(result3, 16)

    def test_bytes_to_int(self):
        """Tests the bytes_to_int() method."""
        numbers1 = [0x12, 0x34]
        numbers2 = [0x00, 0x01]
        numbers3 = [0xFF, 0xFF]

        result1 = bytes_to_int(numbers1)
        result2 = bytes_to_int(numbers2)
        result3 = bytes_to_int(numbers3)

        self.assertEqual(result1, 4660)
        self.assertEqual(result2, 1)
        self.assertEqual(result3, 65535)

    def test_bcds_to_integer(self):
        """Tests the bcds_to_integer() method."""
        numbers1 = [0x00, 0x31, 0x75]
        numbers2 = [0x00, 0x30, 0x00]
        numbers3 = [0xFF, 0xFF, 0xFF]

        result1 = bcds_to_integer(numbers1)
        result2 = bcds_to_integer(numbers2)
        result3 = bcds_to_integer(numbers3)

        self.assertEqual(result1, 3175)
        self.assertEqual(result2, 3000)
        self.assertEqual(result3, 1666665)


if __name__ == "__main__":
    unittest.main()
