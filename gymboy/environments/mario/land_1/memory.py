from pyboy import PyBoy

from gymboy.environments.mario.land_1.constant import *
from gymboy.utils.binary import *


def get_score(pyboy: PyBoy) -> int:
    """
    Returns the current score of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current score of the game
    """
    return bcds_to_integer(pyboy.memory[SCORE_ADDRESS : SCORE_ADDRESS + 3])


def get_world_level(pyboy: PyBoy) -> tuple[int, int]:
    """
    Returns the current world and level of the game.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        tuple[int, int]:
            The current (world, level) of the game
    """
    world_level = pyboy.memory[WORLD_LEVEL_ADDRESS]
    return world_level >> 4, world_level & 0x0F


def get_coins(pyboy: PyBoy) -> int:
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


def get_lives(pyboy: PyBoy) -> int:
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


def get_time(pyboy: PyBoy) -> int:
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


def time_over(pyboy: PyBoy) -> bool:
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


def level_finished(pyboy: PyBoy) -> bool:
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
    return pyboy.memory[GAME_OVER_ADDRESS] == 0x39
