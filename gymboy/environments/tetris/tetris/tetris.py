from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from gymboy.environments.tetris.tetris.memory import *


class TetrisFlatten(gym.Env):
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
    An (182,) array, where arr[0] is the current level, arr[1] is the next block, and arr[2:] is a simplified game area.

    ## Rewards
    The current score normalized, plus -1.0 if the game is over.

    ## Version History
    - v1: Original version
    """

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/tetris/tetris/tetris.gb",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/tetris/tetris/tetris_9.state",
        n_frameskip: int = 60,
        sound: bool = False,
        render_mode: Optional[str] = None,
    ):
        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        # Default actions
        self.actions = ["", "a", "b", "left", "right", "up", "down", "start", "select"]
        self.observation_shape = (182,)

        # Create action and observation spaces
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=self.observation_shape,
            dtype=np.float32,
        )

        # Create the environment
        if self.render_mode == "human":
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound)
            self.pyboy.set_emulation_speed(1)
            self.n_frameskip = 1
        else:
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound, window="null")
            self.pyboy.set_emulation_speed(0)
            self.n_frameskip = n_frameskip

    def step(
        self, action: ActType
    ) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        assert self.action_space.contains(
            action
        ), f"{action!r} ({type(action)}) invalid"

        # Perform the action
        if action == 0:
            pass
        else:
            self.pyboy.button(self.actions[action])
        self.pyboy.tick(self.n_frameskip)

        observation = self.get_obs()
        reward = self.get_reward()
        terminated = game_over(self.pyboy)
        truncated = False
        info = {}

        return observation, reward, terminated, truncated, info

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[ObsType, dict[str, Any]]:  # type: ignore
        if self.init_state_path is None:
            # Case: Reset the game
            self.pyboy.game_wrapper.reset_game()
        else:
            # Case: Load the initial game state
            with open(self.init_state_path, "rb") as f:
                self.pyboy.load_state(f)
        self.pyboy.tick(1)

        # Get the initial observation and info
        observation = self.get_obs()
        info = {}

        return observation, info

    def render(self) -> RenderFrame | list[RenderFrame] | None:
        return None

    def close(self):
        self.pyboy.stop()

    def get_obs(self) -> np.ndarray:
        """Returns the current observation."""
        level = np.array([get_level(self.pyboy)])
        next_block = np.array([get_next_block(self.pyboy)])
        game_area = self.pyboy.game_area().flatten()
        return np.concatenate((level, next_block, game_area)).astype(np.float32)

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        score_reward = get_score(self.pyboy) / 999999
        game_over_reward = -1.0 if game_over(self.pyboy) else 0.0
        return score_reward + game_over_reward


class TetrisImage(gym.Env):
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
    An (144, 160, 3) array representing the RGB image of the game screen.

    ## Rewards
    The current score normalized, plus -1.0 if the game is over.

    ## Version History
    - v1: Original version
    """

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/tetris/tetris/tetris.gb",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/tetris/tetris/tetris_9.state",
        n_frameskip: int = 60,
        sound: bool = False,
        render_mode: Optional[str] = None,
    ):
        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        # Default actions and observation shape
        self.actions = ["", "a", "b", "left", "right", "up", "down", "start", "select"]
        self.observation_shape = (144, 160, 3)

        # Create action and observation spaces
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=self.observation_shape,
            dtype=np.uint8,
        )

        # Create the environment
        if self.render_mode == "human":
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound)
            self.pyboy.set_emulation_speed(1)
            self.n_frameskip = 1
        else:
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound)
            self.pyboy.set_emulation_speed(0)
            self.n_frameskip = n_frameskip

    def step(
        self, action: ActType
    ) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        assert self.action_space.contains(
            action
        ), f"{action!r} ({type(action)}) invalid"

        # Perform the action
        if action == 0:
            pass
        else:
            self.pyboy.button(self.actions[action])
        self.pyboy.tick(self.n_frameskip)

        observation = self.get_obs()
        reward = self.get_reward()
        terminated = game_over(self.pyboy)
        truncated = False
        info = {}

        return observation, reward, terminated, truncated, info

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[ObsType, dict[str, Any]]:  # type: ignore
        if self.init_state_path is None:
            # Case: Reset the game
            self.pyboy.game_wrapper.reset_game()
        else:
            # Case: Load the initial game state
            with open(self.init_state_path, "rb") as f:
                self.pyboy.load_state(f)
        self.pyboy.tick(1)

        # Get the initial observation and info
        observation = self.get_obs()
        info = {}

        return observation, info

    def render(self) -> RenderFrame | list[RenderFrame] | None:
        return None

    def close(self):
        self.pyboy.stop()

    def get_obs(self) -> np.ndarray:
        """Returns the current observation."""
        return cv2.cvtColor(self.pyboy.screen.ndarray, cv2.COLOR_RGBA2RGB)

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        score_reward = get_score(self.pyboy) / 999999
        game_over_reward = -1.0 if game_over(self.pyboy) else 0.0
        return score_reward + game_over_reward
