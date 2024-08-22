import numpy as np
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_1.constant import *
from gymboy.utils.binary import *


def get_badges(pyboy: PyBoy, offset: int = 0) -> int:
    """
    Returns the current number of badges.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        int:
            The current number of badges
    """
    return bytes_bit_count([pyboy.memory[BADGE_COUNT_ADDRESS - offset]])


def get_money(pyboy: PyBoy, offset: int = 0) -> int:
    """
    Returns the current money.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        int:
            The current money
    """
    return bcds_to_integer(pyboy.memory[MONEY_ADDRESS - offset : MONEY_ADDRESS - offset + 3])


def get_team_size(pyboy: PyBoy, offset: int = 0) -> int:
    """
    Returns the current number of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        int:
            The current number of pokemons in your team
    """
    return pyboy.memory[TEAM_SIZE_ADDRESS - offset]


def get_levels(pyboy: PyBoy, offset: int = 0) -> np.ndarray:
    """
    Returns the current levels of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        np.ndarray:
            The current levels of pokemons in your team
    """
    return np.array(
        [pyboy.memory[level_address - offset] for level_address in LEVELS_ADDRESSES]
    )


def get_hps(pyboy: PyBoy, offset: int = 0) -> np.ndarray:
    """
    Returns the current HPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        np.ndarray:
            The current HPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(pyboy.memory[hp_address - offset : hp_address - offset + 2])
            for hp_address in HP_ADDRESSES
        ]
    )


def get_max_hps(pyboy: PyBoy, offset: int = 0) -> np.ndarray:
    """
    Returns the max HPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        np.ndarray:
            The max HPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(
                pyboy.memory[max_hp_address - offset : max_hp_address - offset + 2]
            )
            for max_hp_address in MAX_HP_ADDRESSES
        ]
    )


def get_exps(pyboy: PyBoy, offset: int = 0) -> np.ndarray:
    """
    Returns the current EXPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        np.ndarray:
            The current EXPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(pyboy.memory[exp_address - offset : exp_address - offset + 3])
            for exp_address in EXP_ADDRESSES
        ]
    )


def get_moves(pyboy: PyBoy, offset: int = 0) -> np.ndarray:
    """
    Returns the current move IDs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        np.ndarray:
            The current move IDs of pokemons in your team
    """
    return np.array(
        [
            pyboy.memory[move_address - offset : move_address - offset + 4]
            for move_address in MOVE_ADDRESSES
        ]
    )


def get_pps(pyboy: PyBoy, offset: int = 0) -> np.ndarray:
    """
    Returns the current PPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        np.ndarray:
            The current PPs of pokemons in your team
    """
    return np.array(
        [
            pyboy.memory[pp_address - offset : pp_address - offset + 4]
            for pp_address in PP_ADDRESSES
        ]
    )


def get_max_pps(pyboy: PyBoy, offset: int = 0) -> np.ndarray:
    """
    Returns the max PPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        np.ndarray:
            The max PPs of pokemons in your team
    """
    return np.array(
        [
            [MOVES_TO_MAX_PP[move] if move != 0 else 0 for move in pokemon]
            for pokemon in get_moves(pyboy, offset=offset)
        ]
    )


def get_seen_pokemons(pyboy: PyBoy, offset: int = 0) -> int:
    """
    Returns the current number of seen pokemons.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        int:
            The current number of seen pokemons.
    """
    return bytes_bit_count(
        pyboy.memory[
            POKEDEX_SEEN_START_ADDRESS - offset : POKEDEX_SEEN_END_ADDRESS - offset
        ]
    )


def get_events(pyboy: PyBoy, offset: int = 0) -> int:
    """
    Returns the current number of occurred events.

    Args:
        pyboy (PyBoy):
            The game boy instance

        offset (int):
            The offset of the memory location

    Returns:
        int:
            The current number of occured events.
    """
    return bytes_bit_count(
        pyboy.memory[
            EVENT_FLAGS_START_ADDRESS - offset : EVENT_FLAGS_END_ADDRESS - offset
        ]
    )
