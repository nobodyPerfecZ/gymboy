from pyboy import PyBoy

from gymboy.utils.binary import *
from gymboy.environments.tetris.tetris.constant import *


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
    return bcds_to_integer(reversed(pyboy.memory[SCORE_ADDRESS : SCORE_ADDRESS + 3]))


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
