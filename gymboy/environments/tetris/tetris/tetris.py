"""Tetris environments."""

from abc import ABC

import numpy as np
import skimage as ski
from gymnasium import spaces

from gymboy.environments.env import PyBoyEnv

from ._memory import _game_area, _game_over, _level, _next_block, _score


class Tetris(PyBoyEnv, ABC):
    """
    Abstract class for the Tetris environment.

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
            cartridge_title="TETRIS",
            rom_path=rom_path,
            init_state_path=init_state_path,
            n_frameskip=n_frameskip,
            sound=sound,
            render_mode=render_mode,
        )

    def reward(self) -> float:
        if _game_over(self.pyboy):
            return -1.0
        return _score(self.pyboy) / 999999

    def terminated(self) -> bool:
        return _game_over(self.pyboy)

    def truncated(self) -> bool:
        return False


class TetrisFlatten(Tetris):
    """
    The Tetris environment.

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
    The observation is an (182,) array that consists:
    - [0]: The current level
    - [1]: The next block
    - [2:]: The simplified game area

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
        return spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(182,),
            dtype=np.float32,
        )

    def observation(self) -> np.ndarray:
        level = np.array([_level(self.pyboy)])
        next_block = np.array([_next_block(self.pyboy)])
        game_area = _game_area(self.pyboy).flatten()
        return np.concatenate((level, next_block, game_area)).astype(np.float32)


class TetrisFullImage(Tetris):
    """
    The Tetris environment.

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
        return spaces.Box(
            low=0,
            high=255,
            shape=(144, 160, 3),
            dtype=np.uint8,
        )

    def observation(self) -> np.ndarray:
        obs = ski.color.rgba2rgb(self.pyboy.screen.image)
        return (255 * obs).clip(0, 255).astype(np.uint8)


class TetrisMinimalImage(Tetris):
    """
    The Tetris environment.

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
    The observation is an (18, 10) array representing a simplified view of the game
    screen.

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
        return spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(18, 10),
            dtype=np.float32,
        )

    def observation(self) -> np.ndarray:
        return _game_area(self.pyboy).astype(np.float32)
