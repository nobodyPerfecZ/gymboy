from typing import Any, Optional, SupportsFloat

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from ..constant import EVENT_FLAGS_END_ADDRESS, EVENT_FLAGS_START_ADDRESS
from ..memory import (
    badges,
    events,
    game_area,
    hps,
    levels,
    money,
    moves,
    pokemon_ids,
    pps,
    seen_pokemons,
)


class PokemonYellowFlatten(gym.Env):
    """
    The Pokemon Yellow environment.

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
    The observation is an (426,) array that consists:
    - [0:6]: The ids each pokemon in the team
    - [6:12]: The levels of each pokemon in the team
    - [12:18]: The hps of each pokemon in the team
    - [18:42]: The ids of the moves of each pokemon in the team
    - [42:66]: The pps of the moves of each pokemon in the team
    - [66:]: The simplified game area

    ## Rewards
    The reward is the sum of:
    - The normalized number of badges
    - The normalized amount of money
    - The normalized sum of the levels of the pokemons
    - The normalized number of pokemons seen
    - The normalized number of events

    ## Version History
    - v1: Original version
    """

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/pokemon/gen_1/yellow/pokemon_yellow.gbc",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/pokemon/gen_1/yellow/pokemon_yellow_after_intro.state",
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
        self.observation_shape = (426,)

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
            self.pyboy = PyBoy(
                gamerom=rom_path,
                sound=self.sound,
            )
            self.pyboy.set_emulation_speed(1)
            self.n_frameskip = 1
        else:
            self.pyboy = PyBoy(
                gamerom=rom_path,
                sound=self.sound,
                window="null",
            )
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

    def get_obs(self) -> np.ndarray:
        """Returns the current observation."""
        pokemon_ids_obs = pokemon_ids(self.pyboy, yellow=True)
        levels_obs = levels(self.pyboy, yellow=True)
        hps_obs = hps(self.pyboy, yellow=True)
        moves_obs = moves(self.pyboy, yellow=True).flatten()
        pps_obs = pps(self.pyboy, yellow=True).flatten()
        game_area_obs = game_area(self.pyboy, yellow=True).flatten()
        return np.concatenate(
            (pokemon_ids_obs, levels_obs, hps_obs, moves_obs, pps_obs, game_area_obs)
        )

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        badges_reward = badges(self.pyboy, yellow=True) / 8
        money_reward = money(self.pyboy, yellow=True) / 999999
        pokemon_levels_reward = np.sum(levels(self.pyboy, yellow=True)) / 600
        pokemons_seen_reward = seen_pokemons(self.pyboy, yellow=True) / 151
        number_of_events_reward = events(self.pyboy, yellow=True) / (
            8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)
        )
        return (
            badges_reward
            + money_reward
            + pokemon_levels_reward
            + pokemons_seen_reward
            + number_of_events_reward
        )


class PokemonYellowImage(gym.Env):
    """
    The Pokemon Yellow environment.

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
    - The normalized number of badges
    - The normalized amount of money
    - The normalized sum of the levels of the pokemons
    - The normalized number of pokemons seen
    - The normalized number of events

    ## Version History
    - v1: Original version
    """

    def __init__(
        self,
        rom_path: str = "./gymboy/resources/roms/pokemon/gen_1/yellow/pokemon_yellow.gbc",
        init_state_path: Optional[
            str
        ] = "./gymboy/resources/states/pokemon/gen_1/yellow/pokemon_yellow_after_intro.state",
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

    def get_obs(self) -> np.ndarray:
        """Returns the current observation."""
        return cv2.cvtColor(self.pyboy.screen.ndarray, cv2.COLOR_RGBA2RGB)

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        badges_reward = badges(self.pyboy, yellow=True) / 8
        money_reward = money(self.pyboy, yellow=True) / 999999
        pokemon_levels_reward = np.sum(levels(self.pyboy, yellow=True)) / 600
        pokemons_seen_reward = seen_pokemons(self.pyboy, yellow=True) / 151
        number_of_events_reward = events(self.pyboy, yellow=True) / (
            8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)
        )
        return (
            badges_reward
            + money_reward
            + pokemon_levels_reward
            + pokemons_seen_reward
            + number_of_events_reward
        )
