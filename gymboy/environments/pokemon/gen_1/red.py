"""Pokemon Red environments."""

# pylint: disable=protected-access
from typing import Any, SupportsFloat

import skimage as ski
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame
from pyboy import PyBoy

from gymboy.utils import (
    check_action,
    check_cartridge_title,
    check_frameskip,
    check_rom_file,
    check_state_file,
    resource_path,
)

from ._constant import EVENT_FLAGS_END_ADDRESS, EVENT_FLAGS_START_ADDRESS
from ._memory import (
    _badges,
    _events,
    _game_area,
    _hps,
    _levels,
    _money,
    _moves,
    _pokemon_ids,
    _pps,
    _seen_pokemons,
)


class PokemonRedFlatten(gym.Env):
    """
    The Pokemon Red environment.

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

    Args:
        rom_path (str | None):
            The path to the ROM file.
            If ``None``, ``resources/roms/pokemon/gen_1/pokemon_red.gb`` will be used

        init_state_path (str | None):
            The path to the initial state file.
            If ``None``, ``resources/states/pokemon/gen_1/pokemon_red_after_intro.state`` will be used

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.
            If ``True``, the sound will be played

        render_mode (str | None):
            The mode in which the game will be rendered.
            If ``human``, the game will be rendered
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
            rom_path = resource_path("resources/roms/pokemon/gen_1/pokemon_red.gb")

        if init_state_path is None:
            init_state_path = resource_path(
                "resources/states/pokemon/gen_1/pokemon_red_after_intro.state"
            )

        # Checks
        check_rom_file(rom_path)
        check_state_file(init_state_path)
        check_frameskip(n_frameskip)

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
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound)
            self.pyboy.set_emulation_speed(1)
            self.n_frameskip = 1
        else:
            self.pyboy = PyBoy(gamerom=rom_path, sound=self.sound, window="null")
            self.pyboy.set_emulation_speed(0)
            self.n_frameskip = n_frameskip

        # Check if the cartridge title is correct
        check_cartridge_title(self.pyboy, "POKEMON RED")

    def step(
        self,
        action: ActType,
    ) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        # Check if the action is valid
        check_action(action, self.action_space)

        # Perform the action
        if action == 0:
            pass
        else:
            self.pyboy.button(self.actions[action])

        # Progress the game
        self.pyboy.tick(self.n_frameskip)

        # Get the observation, reward, done and info
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
            self.pyboy.game_wrapper.reset_game(seed)
        else:
            # Case: Load the initial game state
            with open(self.init_state_path, "rb") as f:
                self.pyboy.load_state(f)
                self.pyboy.game_wrapper._set_timer_div(seed)

        # Check if the cartridge title is correct
        check_cartridge_title(self.pyboy, "POKEMON RED")

        # Progress the game
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
        pokemon_ids = _pokemon_ids(self.pyboy, yellow=False)
        levels = _levels(self.pyboy, yellow=False)
        hps = _hps(self.pyboy, yellow=False)
        moves = _moves(self.pyboy, yellow=False).flatten()
        pps = _pps(self.pyboy, yellow=False).flatten()
        game_area = _game_area(self.pyboy, yellow=False).flatten()
        return np.concatenate((pokemon_ids, levels, hps, moves, pps, game_area)).astype(
            np.float32
        )

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        badges = _badges(self.pyboy, yellow=False) / 8
        money = _money(self.pyboy, yellow=False) / 999999
        pokemon_levels = np.sum(_levels(self.pyboy, yellow=False)) / 600
        pokemons_seen = _seen_pokemons(self.pyboy, yellow=False) / 151
        number_of_events = _events(self.pyboy, yellow=False) / (
            8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)
        )
        return badges + money + pokemon_levels + pokemons_seen + number_of_events


class PokemonRedFullImage(gym.Env):
    """
    The Pokemon Red environment.

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

    Args:
        rom_path (str | None):
            The path to the ROM file.
            If ``None``, ``resources/roms/pokemon/gen_1/pokemon_red.gb`` will be used

        init_state_path (str | None):
            The path to the initial state file.
            If ``None``, ``resources/states/pokemon/gen_1/pokemon_red_after_intro.state`` will be used

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.
            If ``True``, the sound will be played

        render_mode (str | None):
            The mode in which the game will be rendered.
            If ``human``, the game will be rendered
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
            rom_path = resource_path("resources/roms/pokemon/gen_1/pokemon_red.gb")
        if init_state_path is None:
            init_state_path = resource_path(
                "resources/states/pokemon/gen_1/pokemon_red_after_intro.state"
            )

        # Checks
        check_rom_file(rom_path)
        check_state_file(init_state_path)
        check_frameskip(n_frameskip)

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

        # Check if the cartridge title is correct
        check_cartridge_title(self.pyboy, "POKEMON RED")

    def step(
        self,
        action: ActType,
    ) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        # Check if the action is valid
        check_action(action, self.action_space)

        # Perform the action
        if action == 0:
            pass
        else:
            self.pyboy.button(self.actions[action])

        # Progress the game
        self.pyboy.tick(self.n_frameskip)

        # Get the observation, reward, done and info
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
            self.pyboy.game_wrapper.reset_game(seed)
        else:
            # Case: Load the initial game state
            with open(self.init_state_path, "rb") as f:
                self.pyboy.load_state(f)
                self.pyboy.game_wrapper._set_timer_div(seed)

        # Check if the cartridge title is correct
        check_cartridge_title(self.pyboy, "POKEMON RED")

        # Progress the game
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
        return ski.color.rgba2rgb(self.pyboy.screen.ndarray).astype(np.uint8)

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        badges = _badges(self.pyboy, yellow=False) / 8
        money = _money(self.pyboy, yellow=False) / 999999
        pokemon_levels = np.sum(_levels(self.pyboy, yellow=False)) / 600
        pokemons_seen = _seen_pokemons(self.pyboy, yellow=False) / 151
        number_of_events = _events(self.pyboy, yellow=False) / (
            8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)
        )
        return badges + money + pokemon_levels + pokemons_seen + number_of_events


class PokemonRedMinimalImage(gym.Env):
    """
    The Pokemon Red environment.

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
    The observation is an (18, 20) array representing a simplified view of the game screen.

    ## Rewards
    The reward is the sum of:
    - The normalized number of badges
    - The normalized amount of money
    - The normalized sum of the levels of the pokemons
    - The normalized number of pokemons seen
    - The normalized number of events

    ## Version History
    - v1: Original version

    Args:
        rom_path (str | None):
            The path to the ROM file.
            If ``None``, ``resources/roms/pokemon/gen_1/pokemon_red.gb`` will be used

        init_state_path (str | None):
            The path to the initial state file.
            If ``None``, ``resources/states/pokemon/gen_1/pokemon_red_after_intro.state`` will be used

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.
            If ``True``, the sound will be played

        render_mode (str | None):
            The mode in which the game will be rendered.
            If ``human``, the game will be rendered
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
            rom_path = resource_path("resources/roms/pokemon/gen_1/pokemon_red.gb")

        if init_state_path is None:
            init_state_path = resource_path(
                "resources/states/pokemon/gen_1/pokemon_red_after_intro.state"
            )

        # Checks
        check_rom_file(rom_path)
        check_state_file(init_state_path)
        check_frameskip(n_frameskip)

        self.rom_path = rom_path
        self.init_state_path = init_state_path
        self.sound = sound
        self.render_mode = render_mode

        # Default actions and observation shape
        self.actions = ["", "a", "b", "left", "right", "up", "down", "start", "select"]
        self.observation_shape = (18, 20)

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

        # Check if the cartridge title is correct
        check_cartridge_title(self.pyboy, "POKEMON RED")

    def step(
        self,
        action: ActType,
    ) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        # Check if the action is valid
        check_action(action, self.action_space)

        # Perform the action
        if action == 0:
            pass
        else:
            self.pyboy.button(self.actions[action])

        # Progress the game
        self.pyboy.tick(self.n_frameskip)

        # Get the observation, reward, done and info
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
            self.pyboy.game_wrapper.reset_game(seed)
        else:
            # Case: Load the initial game state
            with open(self.init_state_path, "rb") as f:
                self.pyboy.load_state(f)
                self.pyboy.game_wrapper._set_timer_div(seed)

        # Check if the cartridge title is correct
        check_cartridge_title(self.pyboy, "POKEMON RED")

        # Progress the game
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
        return _game_area(self.pyboy, yellow=False).astype(np.float32)

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        badges = _badges(self.pyboy, yellow=False) / 8
        money = _money(self.pyboy, yellow=False) / 999999
        pokemon_levels = np.sum(_levels(self.pyboy, yellow=False)) / 600
        pokemons_seen = _seen_pokemons(self.pyboy, yellow=False) / 151
        number_of_events = _events(self.pyboy, yellow=False) / (
            8 * (EVENT_FLAGS_END_ADDRESS - EVENT_FLAGS_START_ADDRESS)
        )
        return badges + money + pokemon_levels + pokemons_seen + number_of_events
