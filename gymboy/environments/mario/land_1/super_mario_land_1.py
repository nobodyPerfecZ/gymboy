"""Super Mario Land 1 environments."""

from abc import ABC

import numpy as np
import skimage as ski
from gymnasium import spaces


from gymboy.environments.env import PyBoyEnv

from ._memory import (
    _coins,
    _game_area,
    _game_over,
    _level_finished,
    _lives,
    _score,
    _time,
    _time_over,
    _world_level,
)


class SuperMarioLand1(PyBoyEnv, ABC):
    """Abstract class for the Super Mario Land 1 environment."""

    def __init__(
        self,
        rom_path: str,
        init_state_path: str | None = None,
        n_frameskip: int = 1,
        sound: bool = False,
        render_mode: str | None = None,
    ):
        super().__init__(
            cartridge_title="SUPER MARIOLAND",
            rom_path=rom_path,
            init_state_path=init_state_path,
            n_frameskip=n_frameskip,
            sound=sound,
            render_mode=render_mode,
        )

    def reward(self) -> float:
        if _time_over(self.pyboy) or _game_over(self.pyboy):
            return -1.0
        if _level_finished(self.pyboy):
            return 1.0
        return _score(self.pyboy) / 999999

    def terminated(self) -> bool:
        return _game_over(self.pyboy)

    def truncated(self) -> bool:
        return False


class SuperMarioLand1Flatten(SuperMarioLand1):
    """
    The Super Mario Land 1 environment.

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
    The observation is an (325,) array that consists:
    - [0]: The current world
    - [1]: The current level
    - [2]: The current lives
    - [3]: The current number of coins
    - [4]: The current time left
    - [5:]: The simplified game area

    ## Rewards
    The reward is:
    - -1.0 if the time or the game is over
    - 1.0 if the level is finished
    - otherwise the normalized score

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
            shape=(325,),
            dtype=np.float32,
        )

    def obs(self) -> np.ndarray:
        world, level = _world_level(self.pyboy)
        world, level = np.array([world]), np.array([level])
        lives = np.array([_lives(self.pyboy)])
        coins = np.array([_coins(self.pyboy)])
        time = np.array([_time(self.pyboy)])
        game_area = _game_area(self.pyboy).flatten()
        return np.concatenate((world, level, lives, coins, time, game_area)).astype(
            np.float32
        )


class SuperMarioLand1FullImage(SuperMarioLand1):
    """
    The Super Mario Land 1 environment.

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
    The reward is:
    - -1.0 if the time or the game is over
    - 1.0 if the level is finished
    - otherwise the normalized score

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
        """Returns the current observation."""
        return ski.color.rgba2rgb(self.pyboy.screen.ndarray).astype(np.uint8)


class SuperMarioLand1MinimalImage(SuperMarioLand1):
    """
    The Super Mario Land 1 environment.

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
    The reward is:
    - -1.0 if the time or the game is over
    - 1.0 if the level is finished
    - otherwise the normalized score

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
        """Returns the current observation."""
        return _game_area(self.pyboy).astype(np.float32)
