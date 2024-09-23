import numpy as np
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_1.constant import *
from gymboy.utils.binary import *


def get_badges(pyboy: PyBoy, yellow: bool = False) -> int:
    """
    Returns the current number of badges.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        int:
            The current number of badges
    """
    return bytes_bit_count([pyboy.memory[BADGE_COUNT_ADDRESS - int(yellow)]])


def get_money(pyboy: PyBoy, yellow: bool = False) -> int:
    """
    Returns the current money.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        int:
            The current money
    """
    return bcds_to_integer(
        pyboy.memory[MONEY_ADDRESS - int(yellow) : MONEY_ADDRESS - int(yellow) + 3]
    )


def get_pokemon_ids(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the current pokemon IDs in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool, optional):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The current pokemon IDs in your team
    """
    return np.array(
        [pyboy.memory[pokemon_id - int(yellow)] for pokemon_id in POKEMON_IDS_ADDRESSES]
    )


def get_team_size(pyboy: PyBoy, yellow: bool = False) -> int:
    """
    Returns the current number of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        int:
            The current number of pokemons in your team
    """
    return pyboy.memory[TEAM_SIZE_ADDRESS - int(yellow)]


def get_levels(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the current levels of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The current levels of pokemons in your team
    """
    return np.array(
        [
            pyboy.memory[level_address - int(yellow)]
            for level_address in LEVELS_ADDRESSES
        ]
    )


def get_hps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the current HPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The current HPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(
                pyboy.memory[hp_address - int(yellow) : hp_address - int(yellow) + 2]
            )
            for hp_address in HP_ADDRESSES
        ]
    )


def get_max_hps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the max HPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The max HPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(
                pyboy.memory[
                    max_hp_address - int(yellow) : max_hp_address - int(yellow) + 2
                ]
            )
            for max_hp_address in MAX_HP_ADDRESSES
        ]
    )


def get_exps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the current EXPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The current EXPs of pokemons in your team
    """
    return np.array(
        [
            bytes_to_int(
                pyboy.memory[exp_address - int(yellow) : exp_address - int(yellow) + 3]
            )
            for exp_address in EXP_ADDRESSES
        ]
    )


def get_moves(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the current move IDs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The current move IDs of pokemons in your team
    """
    return np.array(
        [
            pyboy.memory[move_address - int(yellow) : move_address - int(yellow) + 4]
            for move_address in MOVE_ADDRESSES
        ]
    )


def get_pps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the current PPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The current PPs of pokemons in your team
    """
    return np.array(
        [
            pyboy.memory[pp_address - int(yellow) : pp_address - int(yellow) + 4]
            for pp_address in PP_ADDRESSES
        ]
    )


def get_max_pps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the max PPs of pokemons in your team.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The max PPs of pokemons in your team
    """
    return np.array(
        [
            [MOVES_TO_MAX_PP[move] for move in pokemon]
            for pokemon in get_moves(pyboy, yellow=yellow)
        ]
    )


def get_seen_pokemons(pyboy: PyBoy, yellow: bool = False) -> int:
    """
    Returns the current number of seen pokemons.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        int:
            The current number of seen pokemons.
    """
    return bytes_bit_count(
        pyboy.memory[
            POKEDEX_SEEN_START_ADDRESS
            - int(yellow) : POKEDEX_SEEN_END_ADDRESS
            - int(yellow)
        ]
    )


def get_events(pyboy: PyBoy, yellow: bool = False) -> int:
    """
    Returns the current number of occurred events.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        int:
            The current number of occured events.
    """
    return bytes_bit_count(
        pyboy.memory[
            EVENT_FLAGS_START_ADDRESS
            - int(yellow) : EVENT_FLAGS_END_ADDRESS
            - int(yellow)
        ]
    )
