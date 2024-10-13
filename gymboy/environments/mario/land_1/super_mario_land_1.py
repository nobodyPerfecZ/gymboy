"""Super Mario Land 1 environments."""

# pylint: disable=protected-access
from typing import Any, SupportsFloat

import gymnasium as gym
import numpy as np
import skimage as ski
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

from ._memory import (
    _coins,
    _game_area,
    _game_over,
    _level_finished,
    _lives,
    _score,
    _time,
    _time_over,
    _world_level,
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

    Args:
        rom_path (str | None):
            The path to the ROM file.
            If ``None``, ``resources/roms/mario/land_1/super_mario_land_1.gb`` will be used

        init_state_path (str | None):
            The path to the initial state file.
            If ``None``, ``resources/states/mario/land_1/super_mario_land_1_1_1.state`` will be used

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
            rom_path = resource_path(
                "resources/roms/mario/land_1/super_mario_land_1.gb"
            )
        if init_state_path is None:
            init_state_path = resource_path(
                "resources/states/mario/land_1/super_mario_land_1_1_1.state"
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

        # Check if the cartridge title is correct
        check_cartridge_title(self.pyboy, "SUPER MARIOLAN")

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
        terminated = _game_over(self.pyboy) or _level_finished(self.pyboy)
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
        check_cartridge_title(self.pyboy, "SUPER MARIOLAN")

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
        world, level = _world_level(self.pyboy)
        world, level = np.array([world]), np.array([level])
        lives = np.array([_lives(self.pyboy)])
        time = np.array([_time(self.pyboy)])
        game_area = _game_area(self.pyboy).flatten()
        return np.concatenate((world, level, lives, time, game_area)).astype(np.float32)

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        score = _score(self.pyboy) / 999999
        coin = _coins(self.pyboy) / 99
        time_over = -1.0 if _time_over(self.pyboy) else 0.0
        level_finished = 1.0 if _level_finished(self.pyboy) else 0.0
        game_over = -1.0 if _game_over(self.pyboy) else 0.0
        return score + coin + time_over + level_finished + game_over


class SuperMarioLand1FullImage(gym.Env):
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

    Args:
        rom_path (str | None):
            The path to the ROM file.
            If ``None``, ``resources/roms/mario/land_1/super_mario_land_1.gb`` will be used

        init_state_path (str | None):
            The path to the initial state file.
            If ``None``, ``resources/states/mario/land_1/super_mario_land_1_1_1.state`` will be used

        n_frameskip (int):
            The number of frames to skip between each action

        sound (bool):
            The flag to dis-/enable the sound.
            If ``True``, the sound will be played

        render_mode (str | None):
            The mode in which the game will be rendered.
            If ``human``, the game will be rendered in normal speed
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
        check_cartridge_title(self.pyboy, "SUPER MARIOLAN")

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
        terminated = _game_over(self.pyboy) or _level_finished(self.pyboy)
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
        check_cartridge_title(self.pyboy, "SUPER MARIOLAN")

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
        score = _score(self.pyboy) / 999999
        coin = _coins(self.pyboy) / 99
        time_over = -1.0 if _time_over(self.pyboy) else 0.0
        level_finished = 1.0 if _level_finished(self.pyboy) else 0.0
        game_over = -1.0 if _game_over(self.pyboy) else 0.0
        return score + coin + time_over + level_finished + game_over


class SuperMarioLand1MinimalImage(gym.Env):
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
    The observation is an (16, 20) array representing a simplified view of the game screen.

    ## Rewards
    The reward is the sum of:
    - The normalized score
    - The normalized number of coins
    - -1.0 if the time is over
    - 1.0 if the level is finished
    - -1.0 if the game is over

    ## Version History
    - v1: Original version

    Args:
        rom_path (str | None):
            The path to the ROM file.
            If ``None``, ``resources/roms/mario/land_1/super_mario_land_1.gb`` will be used

        init_state_path (str | None):
            The path to the initial state file.
            If ``None``, ``resources/states/mario/land_1/super_mario_land_1_1_1.state`` will be used

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
            rom_path = resource_path(
                "resources/roms/mario/land_1/super_mario_land_1.gb"
            )
        if init_state_path is None:
            init_state_path = resource_path(
                "resources/states/mario/land_1/super_mario_land_1_1_1.state"
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
        self.observation_shape = (16, 20)

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
        check_cartridge_title(self.pyboy, "SUPER MARIOLAN")

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
        terminated = _game_over(self.pyboy) or _level_finished(self.pyboy)
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
        check_cartridge_title(self.pyboy, "SUPER MARIOLAN")

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
        return _game_area(self.pyboy).astype(np.float32)

    def get_reward(self) -> SupportsFloat:
        """Returns the current reward."""
        score = _score(self.pyboy) / 999999
        coin = _coins(self.pyboy) / 99
        time_over = -1.0 if _time_over(self.pyboy) else 0.0
        level_finished = 1.0 if _level_finished(self.pyboy) else 0.0
        game_over = -1.0 if _game_over(self.pyboy) else 0.0
        return score + coin + time_over + level_finished + game_over
