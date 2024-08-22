import numpy as np
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_2.constant import *
from gymboy.utils.binary import *


def get_badges(pyboy: PyBoy) -> int:
    """
    Returns the current number of badges.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current number of badges
    """
    return bytes_bit_count(
        [
            pyboy.memory[JOHTO_BADGE_COUNT_ADDRESS],
            pyboy.memory[KANTO_BADGE_COUNT_ADDRESS],
        ]
    )


def get_money(pyboy: PyBoy) -> int:
    """
    Returns the current money.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current money
    """
    return bytes_to_int(pyboy.memory[MONEY_ADDRESS : MONEY_ADDRESS + 3])


def get_team_size(pyboy: PyBoy) -> int:
    """
    Returns the current number of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current number of pokemons in your team
    """
    return pyboy.memory[TEAM_SIZE_ADDRESS]


def get_levels(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the current levels of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The current levels of pokemons in your team
    """
    return np.array([pyboy.memory[level_address] for level_address in LEVELS_ADDRESSES])


def get_hps(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the current HPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The current HPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(pyboy.memory[hp_address : hp_address + 2])
            for hp_address in HP_ADDRESSES
        ]
    )


def get_max_hps(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the max HPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The max HPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(pyboy.memory[max_hp_address : max_hp_address + 2])
            for max_hp_address in MAX_HP_ADDRESSES
        ]
    )


def get_exps(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the current EXPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The current EXPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(pyboy.memory[exp_address : exp_address + 3])
            for exp_address in EXP_ADDRESSES
        ]
    )


def get_moves(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the current move IDs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The current move IDs of pokemons in your team
    """
    return np.array(
        [
            pyboy.memory[move_address : move_address + 4]
            for move_address in MOVE_ADDRESSES
        ]
    )


def get_pps(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the current PPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The current PPs of pokemons in your team
    """
    return np.array(
        [pyboy.memory[pp_address : pp_address + 4] for pp_address in PP_ADDRESSES]
    )


def get_max_pps(pyboy: PyBoy) -> np.ndarray:
    """
    Returns the max PPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        np.ndarray:
            The max PPs of pokemons in your team
    """
    return np.array(
        [[MOVES_TO_MAX_PP[move] for move in pokemon] for pokemon in get_moves(pyboy)]
    )


def get_seen_pokemons(pyboy: PyBoy) -> int:
    """
    Returns the current number of seen pokemons.

    Args:
        pyboy (PyBoy):
            The game boy instance

    Returns:
        int:
            The current number of seen pokemons.
    """
    return bytes_bit_count(
        pyboy.memory[POKEDEX_SEEN_START_ADDRESS:POKEDEX_SEEN_END_ADDRESS]
    )
