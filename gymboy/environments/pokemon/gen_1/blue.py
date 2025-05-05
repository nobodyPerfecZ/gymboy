"""Pokemon Blue environments."""

from abc import ABC

import numpy as np
import skimage as ski
from gymnasium import spaces

from gymboy.environments.env import PyBoyEnv

from ._constant import EVENT_FLAGS_END_ADDRESS, EVENT_FLAGS_START_ADDRESS
from ._memory import (
    _badges,
    _events,
    _game_area,
    _hps,
    _levels,
    _money,
    _moves,
    _pokemon_ids,
    _pps,
    _seen_pokemons,
)


class PokemonBlue(PyBoyEnv, ABC):
    """
    Abstract class for the Pokemon Blue environment.

    Args:
        rom_path (str):
            The path to the ROM file.

        init_state_path (str | None):
            The path to the initial state file.

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.

        render_mode (str | None):
            The mode in which the game will be rendered.
    """

    def __init__(
        self,
        rom_path: str,
        init_state_path: str | None = None,
        n_frameskip: int = 1,
        sound: bool = False,
        render_mode: str | None = None,
    ):
        super().__init__(
            cartridge_title="POKEMON BLUE",
            rom_path=rom_path,
            init_state_path=init_state_path,
            n_frameskip=n_frameskip,
            sound=sound,
            render_mode=render_mode,
        )

    def reward(self) -> float:
        badges = _badges(self.pyboy, yellow=False) / 8
        money = _money(self.pyboy, yellow=False) / 999999
        pokemon_levels = np.sum(_levels(self.pyboy, yellow=False)) / 600
        pokemons_seen = _seen_pokemons(self.pyboy, yellow=False) / 151
        number_of_events = _events(self.pyboy, yellow=False) / (
            8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)
        )
        return badges + money + pokemon_levels + pokemons_seen + number_of_events

    def terminated(self) -> bool:
        return False

    def truncated(self) -> bool:
        return False


class PokemonBlueFlatten(PokemonBlue):
    """
    The Pokemon Blue environment.

    ## Action Space
    The action space consists of 9 discrete actions:
    - 0: No action
    - 1: Press A
    - 2: Press B
    - 3: Press Left
    - 4: Press Right
    - 5: Press Up
    - 6: Press Down
    - 7: Press Start
    - 8: Press Select

    ## Observation Space
    The observation is an (426,) array that consists:
    - [0:6]: The ids each pokemon in the team
    - [6:12]: The levels of each pokemon in the team
    - [12:18]: The hps of each pokemon in the team
    - [18:42]: The ids of the moves of each pokemon in the team
    - [42:66]: The pps of the moves of each pokemon in the team
    - [66:]: The simplified game area

    ## Rewards
    The reward is the sum of:
    - The normalized number of badges
    - The normalized amount of money
    - The normalized sum of the levels of the pokemons
    - The normalized number of pokemons seen
    - The normalized number of events

    ## Version History
    - v1: Original version

    Args:
        rom_path (str):
            The path to the ROM file.

        init_state_path (str | None):
            The path to the initial state file.

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.

        render_mode (str | None):
            The mode in which the game will be rendered.
    """

    @property
    def observation_space(self) -> spaces.Space:
        return spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(426,),
            dtype=np.float32,
        )

    def obs(self) -> np.ndarray:
        pokemon_ids = _pokemon_ids(self.pyboy, yellow=False)
        levels = _levels(self.pyboy, yellow=False)
        hps = _hps(self.pyboy, yellow=False)
        moves = _moves(self.pyboy, yellow=False).flatten()
        pps = _pps(self.pyboy, yellow=False).flatten()
        game_area = _game_area(self.pyboy, yellow=False).flatten()
        return np.concatenate((pokemon_ids, levels, hps, moves, pps, game_area)).astype(
            np.float32
        )


class PokemonBlueFullImage(PokemonBlue):
    """
    The Pokemon Blue environment.

    ## Action Space
    The action space consists of 9 discrete actions:
    - 0: No action
    - 1: Press A
    - 2: Press B
    - 3: Press Left
    - 4: Press Right
    - 5: Press Up
    - 6: Press Down
    - 7: Press Start
    - 8: Press Select

    ## Observation Space
    The observation is an (144, 160, 3) array representing the RGB image of the game
    screen.

    ## Rewards
    The reward is the sum of:
    - The normalized number of badges
    - The normalized amount of money
    - The normalized sum of the levels of the pokemons
    - The normalized number of pokemons seen
    - The normalized number of events

    ## Version History
    - v1: Original version

    Args:
        rom_path (str):
            The path to the ROM file.

        init_state_path (str | None):
            The path to the initial state file.

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.

        render_mode (str | None):
            The mode in which the game will be rendered.
    """

    @property
    def observation_space(self) -> spaces.Space:
        return spaces.Box(
            low=0,
            high=255,
            shape=(144, 160, 3),
            dtype=np.uint8,
        )

    def obs(self) -> np.ndarray:
        return ski.color.rgba2rgb(self.pyboy.screen.ndarray).astype(np.uint8)


class PokemonBlueMinimalImage(PokemonBlue):
    """
    The Pokemon Blue environment.

    ## Action Space
    The action space consists of 9 discrete actions:
    - 0: No action
    - 1: Press A
    - 2: Press B
    - 3: Press Left
    - 4: Press Right
    - 5: Press Up
    - 6: Press Down
    - 7: Press Start
    - 8: Press Select

    ## Observation Space
    The observation is an (18, 20) array representing a simplified view of the game
    screen.

    ## Rewards
    The reward is the sum of:
    - The normalized number of badges
    - The normalized amount of money
    - The normalized sum of the levels of the pokemons
    - The normalized number of pokemons seen
    - The normalized number of events

    ## Version History
    - v1: Original version

    Args:
        rom_path (str):
            The path to the ROM file.

        init_state_path (str | None):
            The path to the initial state file.

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.

        render_mode (str | None):
            The mode in which the game will be rendered.
    """

    @property
    def observation_space(self) -> spaces.Space:
        return spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(18, 20),
            dtype=np.float32,
        )

    def obs(self) -> np.ndarray:
        return _game_area(self.pyboy, yellow=False).astype(np.float32)
