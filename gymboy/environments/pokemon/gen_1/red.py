from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_1.constant import *
from gymboy.utils.binary import *


class PokemonRed(gym.Env):
    """Pokemon Red environment."""

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/pokemon_red.gb",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/pokemon_red_after_intro.state",
        badge_factor: float = 1.0,
        money_factor: float = 1.0,
        team_size_factor: float = 1.0,
        levels_factor: float = 1.0,
        hps_factor: float = 1.0,
        pps_factor: float = 1.0,
        seen_pokemons_factor: float = 1.0,
        events_factor: float = 1.0,
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
        self.events_factor = events_factor

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
        number_of_events_reward = self.events_factor * self.get_events_reward()

        return (
            badges_reward
            + money_reward
            + pokemon_team_size_reward
            + pokemon_levels_reward
            + pokemon_hps_reward
            + pokemon_pps_reward
            + pokemons_seen_reward
            + number_of_events_reward
        )

    def get_obs(self) -> np.ndarray:
        """Returns the current observation as an RGB image."""
        # Get the current screen RGBA image
        observation = self.pyboy.screen.ndarray

        # Convert RGBA to RGB image
        observation = cv2.cvtColor(observation, cv2.COLOR_RGBA2RGB)

        return observation

    def get_badges(self) -> int:
        """Returns the number of badges."""
        return bytes_bit_count([self.pyboy.memory[BADGE_COUNT_ADDRESS]])

    def get_max_badges(self) -> int:
        """Returns the maximum number of badges."""
        return 8

    def get_badges_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the number of badges collected."""
        return self.get_badges() / self.get_max_badges()

    def get_money(self) -> int:
        """Returns the money."""
        return bcds_to_integer(
            self.pyboy.memory[MONEY_ADDRESS : MONEY_ADDRESS + 3], digit=100
        )

    def get_max_money(self) -> int:
        """Returns the maximum money."""
        return 999999

    def get_money_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the money collected."""
        return self.get_money() / self.get_max_money()

    def get_team_size(self) -> int:
        """Returns the number of pokemons in team."""
        return self.pyboy.memory[TEAM_SIZE_ADDRESS]

    def get_max_team_size(self) -> int:
        """Returns the maximum number of pokemons in team."""
        return 6

    def get_team_size_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the team size."""
        return self.get_team_size() / self.get_max_team_size()

    def get_levels(self) -> np.ndarray:
        """Returns the levels of the pokemons in the team."""
        return np.array(
            [self.pyboy.memory[level_address] for level_address in LEVELS_ADDRESSES]
        )

    def get_max_levels(self) -> np.ndarray:
        """Returns the maximum levels of the pokemons in the team."""
        return np.array([100, 100, 100, 100, 100, 100])

    def get_levels_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the level earned."""
        return np.sum(self.get_levels()) / np.sum(self.get_max_levels())

    def get_hps(self) -> np.ndarray:
        """Returns the current HPs of the pokemons in the team."""
        return np.array(
            [
                bytes_to_int(self.pyboy.memory[hp_address : hp_address + 2])
                for hp_address in HP_ADDRESSES
            ]
        )

    def get_max_hps(self) -> np.ndarray:
        """Returns the max HPs of the pokemons in the team."""
        return np.array(
            [
                bytes_to_int(self.pyboy.memory[max_hp_address : max_hp_address + 2])
                for max_hp_address in MAX_HP_ADDRESSES
            ]
        )

    def get_hps_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the Pokemon HPs."""
        hps = self.get_hps()
        max_hps = self.get_max_hps()

        if np.all(max_hps == 0):
            # Case: All pokemons are dead or player has no pokemons (beginning of the game)
            return 0.0
        return np.sum(hps) / np.sum(hps)

    def get_exps(self) -> np.ndarray:
        """Returns the experience of the pokemons in the team."""
        return np.array(
            [
                bytes_to_int(self.pyboy.memory[exp_address : exp_address + 3])
                for exp_address in EXP_ADDRESSES
            ]
        )

    def get_moves(self) -> np.ndarray:
        """Returns the moves of the pokemons in the team."""
        return np.array(
            [
                self.pyboy.memory[move_address : move_address + 4]
                for move_address in MOVE_ADDRESSES
            ]
        )

    def get_pps(self) -> np.ndarray:
        """Returns the current power points (PPs) of the pokemons in the team."""
        return np.array(
            [
                self.pyboy.memory[pp_address : pp_address + 4]
                for pp_address in PP_ADDRESSES
            ]
        )

    def get_max_pps(self) -> np.ndarray:
        """Returns the max power points (PPs) of the pokemons in the team."""
        return np.array(
            [
                [MOVES_TO_MAX_PP[move] if move != 0 else 0 for move in pokemon]
                for pokemon in self.get_moves()
            ]
        )

    def get_pps_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the Pokemon PPs."""
        pps = self.get_pps()
        max_pps = self.get_max_pps()

        if np.all(max_pps == 0):
            # Case: All pokemons are dead or player has no pokemons (beginning of the game)
            return 0.0
        return np.sum(pps) / np.sum(max_pps)

    def get_seen_pokemons(self) -> int:
        """Returns the number of seen pokemons."""
        return bytes_bit_count(
            self.pyboy.memory[POKEDEX_SEEN_START_ADDRESS:POKEDEX_SEEN_END_ADDRESS]
        )

    def get_max_seen_pokemons(self) -> int:
        """Returns the number of maximum pokemons."""
        return 151

    def get_seen_pokemons_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the seen pokemons."""
        return self.get_seen_pokemons() / self.get_max_seen_pokemons()

    def get_events(self) -> int:
        """Returns the number of events experienced."""
        return bytes_bit_count(
            self.pyboy.memory[EVENT_FLAGS_START_ADDRESS:EVENT_FLAGS_END_ADDRESS]
        )

    def get_max_events(self) -> int:
        """Returns the maximum number of events experienced."""
        return 8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)

    def get_events_reward(self) -> float:
        """Returns the normalized rewards (0.0, 1.0) to signalize the experienced events."""
        return self.get_events() / self.get_max_events()
