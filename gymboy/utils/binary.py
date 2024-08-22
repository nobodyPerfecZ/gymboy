def bytes_bit_count(numbers: list[int]) -> int:
    """
    Counts the number of bits set to 1.

    Args:
        numbers (list[int]):
            The list of byte values

    Returns:
        int:
            The number of bits set to 1.

    Examples:
        >>> bytes_bit_count([0x00, 0x00])
        0
        >>> bytes_bit_count([0x12, 0x34])
        5
        >>> bytes_bit_count([0xFF, 0xFF])
        16
    """
    return sum(number.bit_count() for number in numbers)


def bytes_to_int(numbers: list[int]) -> int:
    """
    Converts a list of bytes in big-endian order to an integer.

    Args:
        numbers (list[int]):
            The list of byte values

    Returns:
        int:
            The integer value

    Examples:
        >>> bytes_to_int([0x00, 0x01])
        0
        >>> bytes_to_int([0x12, 0x34])
        4660
        >>> bytes_to_int([0xFF, 0xFF])
        65535
    """
    return int.from_bytes(numbers, byteorder="big")


def bcds_to_integer(numbers: list[int]) -> int:
    """
    Converts a list of BCD numbers to an integer.

    The BCD numbers only contains bytes with values from 0x00 to 0x99,
    where the high and low hex values contains values from 0x00 to 0x09.

    Args:
        numbers (list[int]):
            The list of BCD numbers

    Returns:
        int:
            The integer value

    Examples:
        >>> bcds_to_integer([0x01, 0x02, 0x03, 0x04])
        1020304
        >>> bcds_to_integer([0x00, 0x31, 0x75])
        3175
        >>> bcds_to_integer([0x00, 0x30, 0x00])
        3000
    """
    result = 0
    for byte in numbers:
        # Get the high and low hex value of a byte 0xAB
        high_hex = (byte >> 4) & 0x0F  # 0xA
        low_hex = byte & 0x0F  # 0xB
        result = result * 100 + high_hex * 10 + low_hex
    return result


def reduced_bcds_to_integer(numbers: list[int]) -> int:
    """
    Converts a list of reduced BCD numbers to an integer.

    The reduced BCD numbers only contains bytes with values from 0x00 to 0x09,
    where only the low hex value is used to represent a decimal number.

    Args:
        numbers (list[int]):
            The list of BCD numbers

    Returns:
        int:
            The integer value

    Examples:
        >>> reduced_bcds_to_integer([0x01, 0x02, 0x03, 0x04])
        1234
        >>> reduced_bcds_to_integer([0x00, 0x03, 0x00])
        30
        >>> reduced_bcds_to_integer([0x03, 0x00, 0x00])
        300
    """
    result = 0
    for byte in numbers:
        # Get the low hex value of a byte 0xAB
        low_hex = byte & 0x0F  # 0xB
        result = result * 10 + low_hex
    return result
