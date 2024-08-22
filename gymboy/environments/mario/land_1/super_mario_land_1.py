from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from gymboy.environments.mario.land_1.memory import *


class SuperMarioLand1(gym.Env):
    """Super Mario Land 1 environment."""

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/mario/land_1/super_mario_land_1.gb",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/mario/land_1/super_mario_land_1_1_1.state",
        score_factor: float = 1.0,
        coin_factor: float = 1.0,
        live_factor: float = 1.0,
        time_factor: float = 1.0,
        time_over_factor: float = 1.0,
        level_finished_factor: float = 1.0,
        game_over_factor: float = 1.0,
        sound: bool = False,
        render_mode: Optional[str] = None,
    ):
        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        self.score_factor = score_factor
        self.coin_factor = coin_factor
        self.live_factor = live_factor
        self.time_factor = time_factor
        self.time_over_factor = time_over_factor
        self.level_finished_factor = level_finished_factor
        self.game_over_factor = game_over_factor

        # Default actions and observation shape
        self.actions = ["", "a", "b", "left", "right", "up", "down", "start", "select"]
        self.observation_shape = (144, 160, 3)

        # Create action and observation spaces
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(
            low=0, high=255, shape=self.observation_shape, dtype=np.uint8
        )

        # Create the environment
        if self.render_mode == "human":
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound)
            self.pyboy.set_emulation_speed(1)
        else:
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound)
            self.pyboy.set_emulation_speed(0)

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
        self.pyboy.tick(1)

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
        # Compute the single rewards
        score_reward = self.score_factor * self.get_score_reward()
        coin_reward = self.coin_factor * self.get_coins_reward()
        live_reward = self.live_factor * self.get_lives_reward()
        time_reward = self.time_factor * self.get_time_reward()
        time_over_reward = self.time_over_factor * self.time_over_reward()
        level_finished_reward = (
            self.level_finished_factor * self.level_finished_reward()
        )
        game_over_reward = self.game_over_factor * self.game_over_reward()

        return (
            score_reward
            + coin_reward
            + live_reward
            + time_reward
            + time_over_reward
            + level_finished_reward
            + game_over_reward
        )

    def get_obs(self) -> np.ndarray:
        """Returns the current observation as an RGB image."""
        # Get the current screen RGBA image
        observation = self.pyboy.screen.ndarray

        # Convert RGBA to RGB image
        observation = cv2.cvtColor(observation, cv2.COLOR_RGBA2RGB)

        return observation

    def get_score_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the scores received."""
        return get_score(self.pyboy) / 999999

    def get_coins_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the coins received."""
        return get_coins(self.pyboy) / 99

    def get_lives_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the lives left."""
        return get_lives(self.pyboy) / 99

    def get_time_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the time left."""
        return get_time(self.pyboy) / 400

    def time_over_reward(self) -> float:
        """Returns the rewards for the time over."""
        if time_over(self.pyboy):
            return -1.0
        return 0.0

    def level_finished_reward(self) -> float:
        """Returns the rewards for the level finished."""
        if level_finished(self.pyboy):
            return 1.0
        return 0.0

    def game_over_reward(self) -> float:
        """Returns the rewards for the game over."""
        if game_over(self.pyboy):
            return -1.0
        return 0.0
