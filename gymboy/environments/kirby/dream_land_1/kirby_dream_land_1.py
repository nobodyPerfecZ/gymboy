"""Kirby's Dream Land 1 environments."""

from abc import ABC

import numpy as np
import skimage as ski
from gymnasium import spaces

from gymboy.environments.env import PyBoyEnv

from ._memory import _game_area, _game_over, _kirby_health, _lives, _score


class KirbyDreamLand1(PyBoyEnv, ABC):
    """Abstract class for the Kirby's Dream Land 1 environment."""

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
        score = _score(self.pyboy) / 99999
        game_over = -1.0 if _game_over(self.pyboy) else 0.0
        return score + game_over

    def terminated(self) -> bool:
        return _game_over(self.pyboy)

    def truncated(self) -> bool:
        return False


class KirbyDreamLand1Flatten(KirbyDreamLand1):
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
    The observation is an (322,) array that consists:
    - [0]: The current health of Kirby
    - [1]: The current lives of Kirby
    - [2:]: The simplified game area

    ## Rewards
    The reward is the sum of:
    - The normalized score
    - -1.0 if the game is over

    ## Version History
    - v1: Original version

    Args:
        rom_path (str | None):
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
            shape=(322,),
            dtype=np.float32,
        )

    def obs(self) -> np.ndarray:
        kirby_health = np.array([_kirby_health(self.pyboy)])
        lives = np.array([_lives(self.pyboy)])
        game_area = _game_area(self.pyboy).flatten()
        return np.concatenate((kirby_health, lives, game_area)).astype(np.float32)


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
    The observation is an (144, 160, 3) array representing the RGB image of the game
    screen.

    ## Rewards
    The reward is the sum of:
    - The normalized score
    - -1.0 if the game is over

    ## Version History
    - v1: Original version

    Args:
        rom_path (str | None):
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
    The observation is an (16, 20) array representing a simplified view of the game
    screen.

    ## Rewards
    The reward is the sum of:
    - The normalized score
    - -1.0 if the game is over

    ## Version History
    - v1: Original version

    Args:
        rom_path (str | None):
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
            shape=(16, 20),
            dtype=np.float32,
        )

    def obs(self) -> np.ndarray:
        return _game_area(self.pyboy).astype(np.float32)
