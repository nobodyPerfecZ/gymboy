from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_2.memory import *


class PokemonGold(gym.Env):
    """Pokemon Gold environment."""

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/pokemon/gen_2/gold/pokemon_gold.gbc",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/pokemon/gen_2/gold/pokemon_gold_after_intro.state",
        badge_factor: float = 1.0,
        money_factor: float = 1.0,
        team_size_factor: float = 1.0,
        levels_factor: float = 1.0,
        hps_factor: float = 1.0,
        pps_factor: float = 1.0,
        seen_pokemons_factor: float = 1.0,
        sound: bool = False,
        render_mode: Optional[str] = None,
    ):
        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        self.badge_factor = badge_factor
        self.money_factor = money_factor
        self.team_size_factor = team_size_factor
        self.levels_factor = levels_factor
        self.hps_factor = hps_factor
        self.pps_factor = pps_factor
        self.seen_pokemons_factor = seen_pokemons_factor

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

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        # Compute the single rewards
        badges_reward = self.badge_factor * self.get_badges_reward()
        money_reward = self.money_factor * self.get_money_reward()
        pokemon_team_size_reward = self.team_size_factor * self.get_team_size_reward()
        pokemon_levels_reward = self.levels_factor * self.get_levels_reward()
        pokemon_hps_reward = self.hps_factor * self.get_hps_reward()
        pokemon_pps_reward = self.pps_factor * self.get_pps_reward()
        pokemons_seen_reward = (
            self.seen_pokemons_factor * self.get_seen_pokemons_reward()
        )

        return (
            badges_reward
            + money_reward
            + pokemon_team_size_reward
            + pokemon_levels_reward
            + pokemon_hps_reward
            + pokemon_pps_reward
            + pokemons_seen_reward
        )

    def get_obs(self) -> np.ndarray:
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
        self.pyboy.tick(1)

        observation = self.get_obs()
        reward = self.get_reward()
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
        self.pyboy.tick(1)

        # Get the initial observation and info
        observation = self.get_obs()
        info = {}

        return observation, info

    def render(self) -> RenderFrame | list[RenderFrame] | None:
        return None

    def close(self):
        self.pyboy.stop()

    def get_badges_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the number of badges collected."""
        return get_badges(self.pyboy) / 16

    def get_money_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the money collected."""
        return get_money(self.pyboy) / 999999

    def get_team_size_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the team size."""
        return get_team_size(self.pyboy) / 6

    def get_levels_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the level earned."""
        return np.sum(get_levels(self.pyboy)) / 600

    def get_hps_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the Pokemon HPs."""
        hps = get_hps(self.pyboy)
        max_hps = get_max_hps(self.pyboy)
        return np.sum(hps) / np.sum(max_hps) if np.any(max_hps != 0) else 0.0

    def get_pps_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the Pokemon PPs."""
        pps = get_pps(self.pyboy)
        max_pps = get_max_pps(self.pyboy)
        return np.sum(pps) / np.sum(max_pps) if np.any(max_pps != 0) else 0.0

    def get_seen_pokemons_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the seen pokemons."""
        return get_seen_pokemons(self.pyboy) / 251
