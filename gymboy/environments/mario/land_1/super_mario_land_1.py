from typing import Any, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from ....utils import resource_path
from .memory import (
    coins,
    game_area,
    game_over,
    level_finished,
    lives,
    score,
    time,
    time_over,
    world_level,
)


class SuperMarioLand1Flatten(gym.Env):
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
    The observation is an (324,) array that consists:
    - [0]: The current world
    - [1]: The current level
    - [2]: The current lives
    - [3]: The current time left
    - [4:]: The simplified game area

    ## Rewards
    The reward is the sum of:
    - The normalized score
    - The normalized number of coins
    - -1.0 if the time is over
    - 1.0 if the level is finished
    - -1.0 if the game is over

    ## Version History
    - v1: Original version
    """

    def __init__(
        self,
        rom_path: str | None = None,
        init_state_path: str | None = None,
        n_frameskip: int = 60,
        sound: bool = False,
        render_mode: str | None = None,
    ):
        if rom_path is None:
            rom_path = resource_path(
                "resources/roms/mario/land_1/super_mario_land_1.gb"
            )

        if init_state_path is None:
            init_state_path = resource_path(
                "resources/states/mario/land_1/super_mario_land_1_1_1.state"
            )

        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        # Default actions and observation shape
        self.actions = ["", "a", "b", "left", "right", "up", "down", "start", "select"]
        self.observation_shape = (324,)

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
        self,
        action: ActType,
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
        terminated = game_over(self.pyboy) or level_finished(self.pyboy)
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
        world_obs, level_obs = world_level(self.pyboy)
        world_obs, level_obs = np.array([world_obs]), np.array([level_obs])
        lives_obs = np.array([lives(self.pyboy)])
        time_obs = np.array([time(self.pyboy)])
        game_area_obs = game_area(self.pyboy).flatten()
        return np.concatenate(
            (world_obs, level_obs, lives_obs, time_obs, game_area_obs)
        )

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        score_reward = score(self.pyboy) / 999999
        coin_reward = coins(self.pyboy) / 99
        time_over_reward = -1.0 if time_over(self.pyboy) else 0.0
        level_finished_reward = 1.0 if level_finished(self.pyboy) else 0.0
        game_over_reward = -1.0 if game_over(self.pyboy) else 0.0
        return (
            score_reward
            + coin_reward
            + time_over_reward
            + level_finished_reward
            + game_over_reward
        )


class SuperMarioLand1Image(gym.Env):
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
    The observation is an (144, 160, 3) array representing the RGB image of the game screen.

    ## Rewards
    The reward is the sum of:
    - The normalized score
    - The normalized number of coins
    - -1.0 if the time is over
    - 1.0 if the level is finished
    - -1.0 if the game is over

    ## Version History
    - v1: Original version
    """

    def __init__(
        self,
        rom_path: str | None = None,
        init_state_path: str | None = None,
        n_frameskip: int = 60,
        sound: bool = False,
        render_mode: str | None = None,
    ):
        if rom_path is None:
            rom_path = resource_path(
                "resources/roms/mario/land_1/super_mario_land_1.gb"
            )

        if init_state_path is None:
            init_state_path = resource_path(
                "resources/states/mario/land_1/super_mario_land_1_1_1.state"
            )

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
        self,
        action: ActType,
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
        terminated = game_over(self.pyboy) or level_finished(self.pyboy)
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
        score_reward = score(self.pyboy) / 999999
        coin_reward = coins(self.pyboy) / 99
        time_over_reward = -1.0 if time_over(self.pyboy) else 0.0
        level_finished_reward = 1.0 if level_finished(self.pyboy) else 0.0
        game_over_reward = -1.0 if game_over(self.pyboy) else 0.0
        return (
            score_reward
            + coin_reward
            + time_over_reward
            + level_finished_reward
            + game_over_reward
        )
