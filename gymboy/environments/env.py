import hashlib
import os
import warnings
from abc import ABC, abstractmethod
from typing import Any

import gymnasium as gym
from gymnasium import spaces
from gymnasium.core import RenderFrame
from pyboy import PyBoy

from gymboy.utils.validation import SUPPORTED_ROMS


class PyBoyEnv(gym.Env, ABC):
    """
    Base class for all PyBoy environments.

    Args:
        cartridge_title (str):
            The title of the cartridge.

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
        cartridge_title: str,
        rom_path: str,
        init_state_path: str | None = None,
        n_frameskip: int = 1,
        sound: bool = False,
        render_mode: str | None = None,
    ):
        if not rom_path.endswith(".gb") and not rom_path.endswith(".gbc"):
            raise ValueError(f"'{rom_path}' is not referring to a ROM file.")
        if not os.path.exists(rom_path):
            raise FileNotFoundError(f"ROM file '{rom_path}' not found.")
        if init_state_path is not None:
            if not init_state_path.endswith(".state"):
                raise ValueError(
                    f"'{init_state_path}' is not referring to a state file."
                )
            if not os.path.exists(init_state_path):
                raise FileNotFoundError(f"State file '{init_state_path}' not found.")
        if n_frameskip <= 0:
            raise ValueError(f"n_frameskip must be greater than 0, got {n_frameskip}.")

        self.cartridge_title = cartridge_title
        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        # Default actions for the gameboy color
        self.actions = ["", "a", "b", "left", "right", "up", "down", "start", "select"]

        # Create the environment
        if self.render_mode == "human":
            self.pyboy = PyBoy(gamerom=rom_path, sound_emulated=self.sound)
            self.pyboy.set_emulation_speed(1)
            self.n_frameskip = 1
        else:
            self.pyboy = PyBoy(
                gamerom=rom_path, sound_emulated=self.sound, window="null"
            )
            self.pyboy.set_emulation_speed(0)
            self.n_frameskip = n_frameskip

        # Check if the cartridge title is correct
        if self.pyboy.cartridge_title != self.cartridge_title:
            raise ValueError(
                f"Cartridge mismatch, got '{self.pyboy.cartridge_title}', "
                + f"expected '{self.cartridge_title}'."
            )

        # Check ROM hash
        if self.cartridge_title in SUPPORTED_ROMS:
            expected_hashes = SUPPORTED_ROMS[self.cartridge_title]
            with open(self.rom_path, "rb") as f:
                rom_data = f.read()
            md5_hash = hashlib.md5(rom_data).hexdigest()
            if md5_hash != expected_hashes["md5"]:
                warnings.warn(
                    f"ROM MD5 mismatch for {self.cartridge_title}. "
                    f"Expected {expected_hashes['md5']}, got {md5_hash}. "
                    "You may be using an incompatible ROM revision or it might be corrupted, "
                    "which could lead to corrupted observations or silent bugs.",
                    UserWarning,
                    stacklevel=2,
                )

    @property
    @abstractmethod
    def observation_space(self) -> spaces.Space:
        """Returns the observation space of the environment."""
        pass

    @property
    def action_space(self) -> spaces.Space:
        """Returns the action space of the environment."""
        return spaces.Discrete(n=len(self.actions))

    def step(
        self,
        action: int,
    ) -> tuple[dict[str, Any], float, bool, bool, dict[str, Any]]:
        if not self.action_space.contains(action):
            raise ValueError(f"{action} ({type(action)}) invalid.")

        # Perform the action
        if action == 0:
            pass
        else:
            self.pyboy.button(self.actions[action])

        # Progress the game
        self.pyboy.tick(self.n_frameskip)

        # Get the observation, reward, done and info
        observation = self.observation()
        reward = self.reward()
        terminated = self.terminated()
        truncated = self.truncated()
        info = {}

        return observation, reward, terminated, truncated, info

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        if self.init_state_path is None:
            # Case: Reset the game
            self.pyboy.game_wrapper.reset_game(seed)
        else:
            # Case: Load the initial game state
            with open(self.init_state_path, "rb") as f:
                self.pyboy.load_state(f)
                self.pyboy.game_wrapper._set_timer_div(seed)

        # Progress the game
        self.pyboy.tick(1)

        # Get the initial observation and info
        observation = self.observation()
        info = {}

        return observation, info

    def render(self) -> RenderFrame | list[RenderFrame] | None:
        return None

    def close(self):
        self.pyboy.stop()

    @abstractmethod
    def observation(self) -> dict[str, Any]:
        """Returns the current observation."""
        pass

    @abstractmethod
    def reward(self) -> float:
        """Returns the current reward."""
        pass

    @abstractmethod
    def terminated(self) -> bool:
        """Returns True if the episode is terminated, False otherwise."""
        pass

    @abstractmethod
    def truncated(self) -> bool:
        """Returns True if the episode is truncated, False otherwise."""
        pass
