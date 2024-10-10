import numpy as np
from pyboy import PyBoy

from ....utils import bcds_to_integer
from .constant import (
    GAME_OVER_ADDRESS,
    LEVEL_ADDRESS,
    NEXT_BLOCK_ADDRESS,
    SCORE_ADDRESS,
)


def score(pyboy: PyBoy) -> int:
    """
    Returns the current score of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current score of the game
    """
    return bcds_to_integer(reversed(pyboy.memory[SCORE_ADDRESS : SCORE_ADDRESS + 3]))


def level(pyboy: PyBoy) -> int:
    """
    Returns the current level of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current level of the game
    """
    return pyboy.memory[LEVEL_ADDRESS]


def next_block(pyboy: PyBoy) -> int:
    """
    Returns the next block of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The next block of the game
    """
    return pyboy.memory[NEXT_BLOCK_ADDRESS] & 0b11111100


def game_over(pyboy: PyBoy) -> bool:
    """
    Returns True if the game is over.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        bool:
            The game is over
    """
    return (
        pyboy.memory[GAME_OVER_ADDRESS] == 0x0D
        or pyboy.memory[GAME_OVER_ADDRESS] == 0x04
    )


def game_area(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the current game area.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The current game area
    """
    return pyboy.game_area()
