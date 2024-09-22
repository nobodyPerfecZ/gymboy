from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from gymboy.environments.mario.land_1.memory import *


class SuperMarioLand1Flatten(gym.Env):
    """Super Mario Land 1 environment."""

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/mario/land_1/super_mario_land_1.gb",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/mario/land_1/super_mario_land_1_1_1.state",
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

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        score_reward = get_score(self.pyboy) / 999999
        coin_reward = get_coins(self.pyboy) / 99
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

    def get_obs(self) -> np.ndarray:
        """Returns the current observation."""
        lives = np.array([get_lives(self.pyboy)])
        world, level = get_world_level(self.pyboy)
        world, level = np.array([world]), np.array([level])
        time = np.array([get_time(self.pyboy)])
        game_area = self.pyboy.game_area().flatten()
        return np.concatenate((lives, world, level, time, game_area))


class SuperMarioLand1Image(gym.Env):
    """Super Mario Land 1 environment."""

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/mario/land_1/super_mario_land_1.gb",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/mario/land_1/super_mario_land_1_1_1.state",
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

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        score_reward = get_score(self.pyboy) / 999999
        coin_reward = get_coins(self.pyboy) / 99
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

    def get_obs(self) -> np.ndarray:
        """Returns the current observation."""
        return cv2.cvtColor(self.pyboy.screen.ndarray, cv2.COLOR_RGBA2RGB)
