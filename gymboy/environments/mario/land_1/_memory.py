from typing import Tuple
import numpy as np
from pyboy import PyBoy

from gymboy.utils import bcds_to_integer, reduced_bcds_to_integer

from ._constant import (
    COINS_ADDRESS,
    GAME_OVER_ADDRESS,
    LEVEL_COMPLETE,
    LIVES_ADDRESS,
    SCORE_ADDRESS,
    TIME_UP_ADDRESS,
    TIMES_ADDRESS,
    WORLD_LEVEL_ADDRESS,
)


def _score(pyboy: PyBoy) -> int:
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


def _world_level(pyboy: PyBoy) -> Tuple[int, int]:
    """
    Returns the current world and level of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        Tuple[int, int]:
            The current (world, level) of the game
    """
    return (
        pyboy.memory[WORLD_LEVEL_ADDRESS] >> 4,
        pyboy.memory[WORLD_LEVEL_ADDRESS] & 0x0F,
    )


def _coins(pyboy: PyBoy) -> int:
    """
    Returns the current number of coins of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current number of coins of the game
    """
    return reduced_bcds_to_integer(pyboy.memory[COINS_ADDRESS : COINS_ADDRESS + 2])


def _lives(pyboy: PyBoy) -> int:
    """
    Returns the current number of lives of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current number of lives of the game
    """
    return reduced_bcds_to_integer([pyboy.memory[LIVES_ADDRESS]])


def _time(pyboy: PyBoy) -> int:
    """
    Returns the current time of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current time of the game
    """
    return reduced_bcds_to_integer(pyboy.memory[TIMES_ADDRESS : TIMES_ADDRESS + 3])


def _time_over(pyboy: PyBoy) -> bool:
    """
    Returns True if the time is over.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        bool:
            The time is over
    """
    return pyboy.memory[TIME_UP_ADDRESS] == 0xFF


def _level_finished(pyboy: PyBoy) -> bool:
    """
    Returns True if the level is finished.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        bool:
            The level is finished
    """
    return 0x05 <= pyboy.memory[LEVEL_COMPLETE] <= 0x07


def _game_over(pyboy: PyBoy) -> bool:
    """
    Returns True if the game is over.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        bool:
            The game is over
    """
    return pyboy.memory[GAME_OVER_ADDRESS] == 0x39


def _game_area(pyboy: PyBoy) -> np.ndarray:
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
