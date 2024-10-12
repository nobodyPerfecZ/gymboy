from pyboy import PyBoy

import numpy as np
from gymboy.utils.binary import reduced_bcds_to_integer

from ._constant import (
    BOSS_HEALTH_ADDRESS,
    KIRBY_HEALTH_ADDRESS,
    LIVES_ADDRESS,
    SCORE_ADDRESS,
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
    return reduced_bcds_to_integer(pyboy.memory[SCORE_ADDRESS : SCORE_ADDRESS + 5])


def _kirby_health(pyboy: PyBoy) -> int:
    """
    Returns the current health of Kirby.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current health of kirby
    """
    return pyboy.memory[KIRBY_HEALTH_ADDRESS]


def _boss_health(pyboy: PyBoy) -> int:
    """
    Returns the current health of the boss.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current health of the boss
    """
    return pyboy.memory[BOSS_HEALTH_ADDRESS]


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
    return pyboy.memory[LIVES_ADDRESS]


def _game_over(pyboy: PyBoy) -> bool:
    """
    Returns whether the game is over.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        bool:
            Whether the game is over
    """
    return bool(pyboy.game_wrapper.game_over())


def _game_area(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the game area of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The game area of the game
    """
    return pyboy.game_wrapper.game_area()
