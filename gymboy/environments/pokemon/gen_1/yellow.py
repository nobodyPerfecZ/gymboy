"""Pokemon Yellow environments."""

from abc import ABC
from typing import Any

import numpy as np
import skimage as ski
from gymnasium import spaces

from gymboy.environments.env import PyBoyEnv

from ._constant import EVENT_FLAGS_END_ADDRESS, EVENT_FLAGS_START_ADDRESS
from ._memory import (
    _badges,
    _events,
    _exps,
    _game_area,
    _hps,
    _levels,
    _max_hps,
    _max_pps,
    _money,
    _moves,
    _pokemon_ids,
    _pps,
    _seen_pokemons,
    _team_size,
)


class PokemonYellow(PyBoyEnv, ABC):
    """
    Abstract class for the Pokemon Yellow environment.

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
            cartridge_title="POKEMON YELLOW",
            rom_path=rom_path,
            init_state_path=init_state_path,
            n_frameskip=n_frameskip,
            sound=sound,
            render_mode=render_mode,
        )

    def reward(self) -> float:
        badges = _badges(self.pyboy, yellow=True) / 8
        money = _money(self.pyboy, yellow=True) / 999999
        pokemon_levels = np.sum(_levels(self.pyboy, yellow=True)) / 600
        pokemons_seen = _seen_pokemons(self.pyboy, yellow=True) / 151
        number_of_events = _events(self.pyboy, yellow=True) / (
            8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)
        )
        return badges + money + pokemon_levels + pokemons_seen + number_of_events

    def terminated(self) -> bool:
        return False

    def truncated(self) -> bool:
        return False


class PokemonYellowFullImage(PokemonYellow):
    """
    The Pokemon Yellow environment.

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
    The observation is a dictionary containing:
    - 'pokemon':
        - 'ids': An (6,) array representing the IDs of the pokemons in the team
        - 'team_size': An (1,) array representing the size of the team
        - 'exps': An (6,) array representing the experience points of the pokemons
        - 'levels': An (6,) array representing the levels of the pokemons
        - 'max_hps': An (6,) array representing the maximum HPs of the pokemons
        - 'hps': An (6,) array representing the current HPs of the pokemons
        - 'moves': An (6, 4) array representing the moves of the pokemons
        - 'max_pps': An (6, 4) array representing the maximum PPs of the moves
        - 'pps': An (6, 4) array representing the current PPs of the moves
    - 'badges': An (1,) array representing the number of badges
    - 'money': An (1,) array representing the amount of money
    - 'img': An (144, 160, 3) array representing the RGB image of the game screen

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
        return spaces.Dict(
            {
                "pokemon": spaces.Dict(
                    {
                        "ids": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "team_size": spaces.Box(
                            -np.inf, np.inf, shape=(1,), dtype=np.float32
                        ),
                        "exps": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "levels": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "max_hps": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "hps": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "moves": spaces.Box(
                            -np.inf, np.inf, shape=(6, 4), dtype=np.float32
                        ),
                        "max_pps": spaces.Box(
                            -np.inf, np.inf, shape=(6, 4), dtype=np.float32
                        ),
                        "pps": spaces.Box(
                            -np.inf, np.inf, shape=(6, 4), dtype=np.float32
                        ),
                    }
                ),
                "badges": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "money": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "img": spaces.Box(0, 255, shape=(144, 160, 3), dtype=np.uint8),
            }
        )

    def observation(self) -> dict[str, Any]:
        ids = _pokemon_ids(self.pyboy, yellow=True).astype(np.float32)
        team_size = np.array([_team_size(self.pyboy, yellow=True)]).astype(np.float32)
        exps = _exps(self.pyboy, yellow=True).astype(np.float32)
        levels = _levels(self.pyboy, yellow=True).astype(np.float32)
        max_hps = _max_hps(self.pyboy, yellow=True).astype(np.float32)
        hps = _hps(self.pyboy, yellow=True).astype(np.float32)
        moves = _moves(self.pyboy, yellow=True).astype(np.float32)
        max_pps = _max_pps(self.pyboy, yellow=True).astype(np.float32)
        pps = _pps(self.pyboy, yellow=True).astype(np.float32)
        badges = np.array([_badges(self.pyboy, yellow=True)]).astype(np.float32)
        money = np.array([_money(self.pyboy, yellow=True)]).astype(np.float32)
        img = (
            (255 * ski.color.rgba2rgb(self.pyboy.screen.image))
            .clip(0, 255)
            .astype(np.uint8)
        )
        return {
            "pokemon": {
                "ids": ids,
                "team_size": team_size,
                "exps": exps,
                "levels": levels,
                "max_hps": max_hps,
                "hps": hps,
                "moves": moves,
                "max_pps": max_pps,
                "pps": pps,
            },
            "badges": badges,
            "money": money,
            "img": img,
        }


class PokemonYellowMinimalImage(PokemonYellow):
    """
    The Pokemon Yellow environment.

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
    The observation is a dictionary containing:
    - 'pokemon':
        - 'ids': An (6,) array representing the IDs of the pokemons in the team
        - 'team_size': An (1,) array representing the size of the team
        - 'exps': An (6,) array representing the experience points of the pokemons
        - 'levels': An (6,) array representing the levels of the pokemons
        - 'max_hps': An (6,) array representing the maximum HPs of the pokemons
        - 'hps': An (6,) array representing the current HPs of the pokemons
        - 'moves': An (6, 4) array representing the moves of the pokemons
        - 'max_pps': An (6, 4) array representing the maximum PPs of the moves
        - 'pps': An (6, 4) array representing the current PPs of the moves
    - 'badges': An (1,) array representing the number of badges
    - 'money': An (1,) array representing the amount of money
    - 'img': An (18, 20) array representing the simplified view of the game screen

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
        return spaces.Dict(
            {
                "pokemon": spaces.Dict(
                    {
                        "ids": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "team_size": spaces.Box(
                            -np.inf, np.inf, shape=(1,), dtype=np.float32
                        ),
                        "exps": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "levels": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "max_hps": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "hps": spaces.Box(
                            -np.inf, np.inf, shape=(6,), dtype=np.float32
                        ),
                        "moves": spaces.Box(
                            -np.inf, np.inf, shape=(6, 4), dtype=np.float32
                        ),
                        "max_pps": spaces.Box(
                            -np.inf, np.inf, shape=(6, 4), dtype=np.float32
                        ),
                        "pps": spaces.Box(
                            -np.inf, np.inf, shape=(6, 4), dtype=np.float32
                        ),
                    }
                ),
                "badges": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "money": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "img": spaces.Box(-np.inf, np.inf, shape=(18, 20), dtype=np.float32),
            }
        )

    def observation(self) -> dict[str, Any]:
        ids = _pokemon_ids(self.pyboy, yellow=True).astype(np.float32)
        team_size = np.array([_team_size(self.pyboy, yellow=True)]).astype(np.float32)
        exps = _exps(self.pyboy, yellow=True).astype(np.float32)
        levels = _levels(self.pyboy, yellow=True).astype(np.float32)
        max_hps = _max_hps(self.pyboy, yellow=True).astype(np.float32)
        hps = _hps(self.pyboy, yellow=True).astype(np.float32)
        moves = _moves(self.pyboy, yellow=True).astype(np.float32)
        max_pps = _max_pps(self.pyboy, yellow=True).astype(np.float32)
        pps = _pps(self.pyboy, yellow=True).astype(np.float32)
        badges = np.array([_badges(self.pyboy, yellow=True)]).astype(np.float32)
        money = np.array([_money(self.pyboy, yellow=True)]).astype(np.float32)
        img = _game_area(self.pyboy, yellow=True).astype(np.float32)
        return {
            "pokemon": {
                "ids": ids,
                "team_size": team_size,
                "exps": exps,
                "levels": levels,
                "max_hps": max_hps,
                "hps": hps,
                "moves": moves,
                "max_pps": max_pps,
                "pps": pps,
            },
            "badges": badges,
            "money": money,
            "img": img,
        }
