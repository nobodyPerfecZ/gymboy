def bytes_bit_count(numbers: list[int]) -> int:
    """Counts the number of bits set to 1."""
    return sum(number.bit_count() for number in numbers)


def bytes_to_int(numbers: list[int]) -> int:
    """Converts a list of bytes in big-endian order to an integer."""
    return int.from_bytes(numbers, byteorder="big")


def bcds_to_integer(numbers: list[int], digit: int = 100) -> int:
    """Converts a list of binary-coded decimal (BCD) numbers to an integer."""
    result = 0
    for byte in numbers:
        result = digit * result + 10 * ((byte >> 4) & 0x0F) + (byte & 0x0F)
    return result
