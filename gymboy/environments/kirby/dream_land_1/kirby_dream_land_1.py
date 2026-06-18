"""Kirby's Dream Land 1 environments."""

from abc import ABC
from typing import Any

import numpy as np
import skimage as ski
from gymnasium import spaces

from gymboy.environments.env import PyBoyEnv

from ._memory import _game_area, _game_over, _kirby_health, _lives, _score


class KirbyDreamLand1(PyBoyEnv, ABC):
    """
    Abstract class for the Kirby's Dream Land 1 environment.

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
            cartridge_title="KIRBY DREAM LAN",
            rom_path=rom_path,
            init_state_path=init_state_path,
            n_frameskip=n_frameskip,
            sound=sound,
            render_mode=render_mode,
        )

    def reward(self) -> float:
        if _game_over(self.pyboy):
            return -1.0
        return _score(self.pyboy) / 99999

    def terminated(self) -> bool:
        return _game_over(self.pyboy)

    def truncated(self) -> bool:
        return False


class KirbyDreamLand1FullImage(KirbyDreamLand1):
    """
    The Kirby's Dream Land 1 environment.

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
    - 'health': An (1,) array representing Kirby's health
    - 'lives': An (1,) array representing the number of lives left
    - 'score': An (1,) array representing the current score
    - 'img': An (144, 160, 3) array representing the RGB image of the game screen

    ## Rewards
    The reward is:
    - -1.0 if the game is over
    - otherwise the normalized score

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
                "health": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "lives": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "score": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "img": spaces.Box(0, 255, shape=(144, 160, 3), dtype=np.uint8),
            }
        )

    def observation(self) -> dict[str, Any]:
        kirby_health = np.array([_kirby_health(self.pyboy)]).astype(np.float32)
        lives = np.array([_lives(self.pyboy)]).astype(np.float32)
        score = np.array([_score(self.pyboy)]).astype(np.float32)
        img = (
            (255 * ski.color.rgba2rgb(self.pyboy.screen.image))
            .clip(0, 255)
            .astype(np.uint8)
        )
        return {"health": kirby_health, "lives": lives, "score": score, "img": img}


class KirbyDreamLand1MinimalImage(KirbyDreamLand1):
    """
    The Kirby's Dream Land 1 environment.

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
    - 'health': An (1,) array representing Kirby's health
    - 'lives': An (1,) array representing the number of lives left
    - 'score': An (1,) array representing the current score
    - 'img': An (16, 20) array representing the simplified view of the game screen

    ## Rewards
    The reward is:
    - -1.0 if the game is over
    - otherwise the normalized score

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
                "health": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "lives": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "score": spaces.Box(-np.inf, np.inf, shape=(1,), dtype=np.float32),
                "img": spaces.Box(-np.inf, np.inf, shape=(16, 20), dtype=np.float32),
            }
        )

    def observation(self) -> dict[str, Any]:
        kirby_health = np.array([_kirby_health(self.pyboy)]).astype(np.float32)
        lives = np.array([_lives(self.pyboy)]).astype(np.float32)
        score = np.array([_score(self.pyboy)]).astype(np.float32)
        img = _game_area(self.pyboy).astype(np.float32)
        return {"health": kirby_health, "lives": lives, "score": score, "img": img}
