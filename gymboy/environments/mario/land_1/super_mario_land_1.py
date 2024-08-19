from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from gymboy.environments.mario.land_1.constant import *
from gymboy.utils.binary import *


class SuperMarioLand1(gym.Env):
    """Super Mario Land 1 environment."""

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/super_mario_land_1.gb",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/super_mario_land_1_1_1.state",
        score_factor: float = 1.0,
        coin_factor: float = 1.0,
        live_factor: float = 1.0,
        time_factor: float = 1.0,
        game_over_factor: float = 1.0,
        game_finished_factor: float = 1.0,
        sound: bool = False,
        render_mode: Optional[str] = None,
    ):
        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        self.world_level = None

        self.score_factor = score_factor
        self.coin_factor = coin_factor
        self.live_factor = live_factor
        self.time_factor = time_factor
        self.game_over_factor = game_over_factor
        self.game_finished_factor = game_finished_factor

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
        terminated = self.game_over() or self.game_finished()
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

        # Update the world level
        self.world_level = self.get_world_level()

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
        live_reward = self.live_factor * self.get_lives_left_reward()
        time_reward = self.time_factor * self.get_time_left_reward()
        game_over_reward = self.game_over_factor * self.game_over_reward()
        game_finished_reward = self.game_finished_factor * self.game_finished_reward()

        return (
            score_reward
            + coin_reward
            + live_reward
            + time_reward
            + game_over_reward
            + game_finished_reward
        )

    def get_obs(self) -> np.ndarray:
        """Returns the current observation as an RGB image."""
        # Get the current screen RGBA image
        observation = self.pyboy.screen.ndarray

        # Convert RGBA to RGB image
        observation = cv2.cvtColor(observation, cv2.COLOR_RGBA2RGB)

        return observation

    def get_score(self) -> int:
        """Returns the current score."""
        return bcds_to_integer(
            self.pyboy.memory[SCORE_ADDRESS : SCORE_ADDRESS + 3], digit=100
        )

    def get_world_level(self) -> tuple[int, int]:
        """Returns the current world and level."""
        world_level = self.pyboy.memory[WORLD_LEVEL_ADDRESS]
        return world_level >> 4, world_level & 0x0F

    def get_max_score(self) -> int:
        """Returns the maximum score."""
        return 999999

    def get_score_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the scores received."""
        return self.get_score() / self.get_max_score()

    def get_coins(self) -> int:
        """Returns the current number of coins."""
        return bcds_to_integer(
            self.pyboy.memory[COINS_ADDRESS : COINS_ADDRESS + 2], digit=10
        )

    def get_max_coins(self) -> int:
        """Returns the maximum number of coins."""
        return 99

    def get_coins_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the coins received."""
        return self.get_coins() / self.get_max_coins()

    def get_lives_left(self) -> int:
        """Returns the current lives left."""
        return bcds_to_integer([self.pyboy.memory[LIVES_LEFT_ADDRESS]], digit=0) + 1

    def get_max_lives_left(self) -> int:
        """Returns the maximum number of lives."""
        return 99

    def get_lives_left_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the lives left."""
        return self.get_lives_left() / self.get_max_lives_left()

    def get_time_left(self) -> int:
        """Returns the current time left."""
        return bcds_to_integer(
            self.pyboy.memory[TIMES_LEFT_ADDRESS : TIMES_LEFT_ADDRESS + 3], digit=10
        )

    def get_max_time_left(self) -> int:
        """Returns the maximum time left."""
        return 400

    def get_time_left_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the time left."""
        return self.get_time_left() / self.get_max_time_left()

    def game_over(self) -> bool:
        """Returns True if the game is over."""
        return self.pyboy.memory[GAME_OVER_ADDRESS] == 0x39

    def game_over_reward(self) -> float:
        """Returns the rewards for the game over."""
        if self.game_over():
            return -1.0
        return 0.0

    def game_finished(self) -> bool:
        """Returns True if the game is finished."""
        if self.world_level is None:
            return False
        return self.world_level != self.get_world_level()

    def game_finished_reward(self) -> float:
        """Returns the rewards for the game finished."""
        if self.game_finished():
            return 1.0
        return 0.0
