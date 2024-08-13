from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy


class PokemonSilver(gym.Env):
    """Pokemon Silver environment."""

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/pokemon_silver.gbc",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/pokemon_silver_after_intro.state",
        render_mode: Optional[str] = None,
    ):
        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.render_mode = render_mode

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
            self.pyboy = PyBoy(
                gamerom=rom_path,
            )
        else:
            self.pyboy = PyBoy(
                gamerom=rom_path,
                window="null",
            )

    def _get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        return 1.0

    def _get_obs(self) -> np.ndarray:
        """Returns the current observation as an RGB image."""
        # Get the current screen RGBA image
        observation = self.pyboy.screen.ndarray

        # Convert RGBA to RGB image
        observation = cv2.cvtColor(observation, cv2.COLOR_RGBA2RGB)

        return observation

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

        observation = self._get_obs()
        reward = self._get_reward()
        terminated = False

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

        # Get the initial observation and info
        observation = self._get_obs()
        info = {}

        return observation, info

    def render(self) -> RenderFrame | list[RenderFrame] | None:
        if self.render_mode == "human":
            self.pyboy.tick()
            return self._get_obs()
        elif self.render_mode == "rgb_array":
            return self._get_obs()
        elif self.render_mode is None:
            return None
        else:
            raise ValueError("Invalid render mode.")

    def close(self):
        self.pyboy.stop()
