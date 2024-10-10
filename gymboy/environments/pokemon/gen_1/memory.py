import numpy as np
from pyboy import PyBoy

from ....utils import bcds_to_integer, bytes_bit_count, bytes_to_int

from .constant import (
    BADGE_COUNT_ADDRESS,
    EVENT_FLAGS_END_ADDRESS,
    EVENT_FLAGS_START_ADDRESS,
    EXP_ADDRESSES,
    HP_ADDRESSES,
    LEVELS_ADDRESSES,
    MAX_HP_ADDRESSES,
    MONEY_ADDRESS,
    MOVE_ADDRESSES,
    MOVES_TO_MAX_PP,
    POKEDEX_SEEN_END_ADDRESS,
    POKEDEX_SEEN_START_ADDRESS,
    POKEMON_IDS_ADDRESSES,
    PP_ADDRESSES,
    TEAM_SIZE_ADDRESS,
)


def badges(pyboy: PyBoy, yellow: bool = False) -> int:
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


def money(pyboy: PyBoy, yellow: bool = False) -> int:
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


def pokemon_ids(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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


def team_size(pyboy: PyBoy, yellow: bool = False) -> int:
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


def levels(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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


def hps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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


def max_hps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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


def exps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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


def moves(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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


def pps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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


def max_pps(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
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
            for pokemon in moves(pyboy, yellow=yellow)
        ]
    )


def seen_pokemons(pyboy: PyBoy, yellow: bool = False) -> int:
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


def events(pyboy: PyBoy, yellow: bool = False) -> int:
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


def game_area(pyboy: PyBoy, yellow: bool = False) -> np.ndarray:
    """
    Returns the current game area.

    Args:
        pyboy (PyBoy):
            The game boy instance

        yellow (bool):
            The flag to indicate if the game is Pokemon Yellow

    Returns:
        np.ndarray:
            The current game area
    """
    if not yellow:
        return pyboy.game_area()
    else:
        # Set the screen area
        xx, yy, width, height = (0, 0, 20, 18)

        # Get the tile matrix
        area = np.ndarray(shape=(height, width), dtype=np.uint32)
        for y in range(height):
            SCX = pyboy.screen.tilemap_position_list[(yy + y) * 8][0] // 8
            SCY = pyboy.screen.tilemap_position_list[(yy + y) * 8][1] // 8
            for x in range(width):
                _x = (xx + x + SCX) % 32
                _y = (yy + y + SCY) % 32
                area[y, x] = pyboy.tilemap_background.tile_identifier(_x, _y)

        # Get the sprites
        sprites = [pyboy.get_sprite(s) for s in range(40)]

        # Add the sprites to the tile matrix
        for s in sprites:
            _x = (s.x // 8) - xx
            _y = (s.y // 8) - yy
            if 0 <= _y < height and 0 <= _x < width:
                area[_y][_x] = s.tile_identifier

        return area
