"""An version of OpenAI's infamous env.make(env_name)."""

import os
from typing import Callable

import gymnasium as gym

from .environments import (
    KirbyDreamLand1FullImage,
    KirbyDreamLand1MinimalImage,
    PokemonBlueFullImage,
    PokemonBlueMinimalImage,
    PokemonGoldFullImage,
    PokemonGoldMinimalImage,
    PokemonRedFullImage,
    PokemonRedMinimalImage,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
    SuperMarioLand1FullImage,
    SuperMarioLand1MinimalImage,
    TetrisFullImage,
    TetrisMinimalImage,
)
from .environments.env import PyBoyEnv

ENV_TO_ROM = {
    "Kirby-Dream-Land-1-full-image-v1": "kirby_dream_land_1.gb",
    "Kirby-Dream-Land-1-minimal-image-v1": "kirby_dream_land_1.gb",
    "Pokemon-Blue-full-image-v1": "pokemon_blue.gb",
    "Pokemon-Blue-minimal-image-v1": "pokemon_blue.gb",
    "Pokemon-Gold-full-image-v1": "pokemon_gold.gbc",
    "Pokemon-Gold-minimal-image-v1": "pokemon_gold.gbc",
    "Pokemon-Red-full-image-v1": "pokemon_red.gb",
    "Pokemon-Red-minimal-image-v1": "pokemon_red.gb",
    "Pokemon-Silver-full-image-v1": "pokemon_silver.gbc",
    "Pokemon-Silver-minimal-image-v1": "pokemon_silver.gbc",
    "Pokemon-Yellow-full-image-v1": "pokemon_yellow.gbc",
    "Pokemon-Yellow-minimal-image-v1": "pokemon_yellow.gbc",
    "Super-Mario-Land-1-full-image-v1": "super_mario_land_1.gb",
    "Super-Mario-Land-1-minimal-image-v1": "super_mario_land_1.gb",
    "Tetris-full-image-v1": "tetris.gb",
    "Tetris-minimal-image-v1": "tetris.gb",
}

ENV_TO_STATE = {
    "Kirby-Dream-Land-1-full-image-v1": "kirby_dream_land_1_after_intro.state",
    "Kirby-Dream-Land-1-minimal-image-v1": "kirby_dream_land_1_after_intro.state",
    "Pokemon-Blue-full-image-v1": "pokemon_blue_after_intro.state",
    "Pokemon-Blue-minimal-image-v1": "pokemon_blue_after_intro.state",
    "Pokemon-Gold-full-image-v1": "pokemon_gold_after_intro.state",
    "Pokemon-Gold-minimal-image-v1": "pokemon_gold_after_intro.state",
    "Pokemon-Red-full-image-v1": "pokemon_red_after_intro.state",
    "Pokemon-Red-minimal-image-v1": "pokemon_red_after_intro.state",
    "Pokemon-Silver-full-image-v1": "pokemon_silver_after_intro.state",
    "Pokemon-Silver-minimal-image-v1": "pokemon_silver_after_intro.state",
    "Pokemon-Yellow-full-image-v1": "pokemon_yellow_after_intro.state",
    "Pokemon-Yellow-minimal-image-v1": "pokemon_yellow_after_intro.state",
    "Super-Mario-Land-1-full-image-v1": "super_mario_land_1_after_intro.state",
    "Super-Mario-Land-1-minimal-image-v1": "super_mario_land_1_after_intro.state",
    "Tetris-full-image-v1": "tetris_after_intro.state",
    "Tetris-minimal-image-v1": "tetris_after_intro.state",
}


def make(
    env_id: str,
    rom_path: str | None = None,
    init_state_path: str | None = None,
    **env_kwargs,
) -> PyBoyEnv:
    """
    A self-version of OpenAI's infamous env.make(env_name).

    Args:
        env_id (str):
            A string identifier for the environment.

        **env_kwargs:
            Keyword arguments to pass to the environment.

    Returns:
        PyBoyEnv:
            The Gymboy environment
    """
    if env_id not in registered_envs:
        raise ValueError(f"{env_id} is not in registered gymboy environments.")

    if rom_path is None:
        rom_dir = os.getenv("GYMBOY_ROM_DIR")
        if not rom_dir:
            raise ValueError("rom_path must be provided or GYMBOY_ROM_DIR must be set.")
        if env_id not in ENV_TO_ROM:
            raise ValueError(f"No default ROM filename known for environment {env_id}.")
        rom_path = os.path.join(rom_dir, ENV_TO_ROM[env_id])

    if init_state_path is None:
        state_dir = os.getenv("GYMBOY_STATE_DIR")
        if state_dir is not None and env_id in ENV_TO_STATE:
            init_state_path = os.path.join(state_dir, ENV_TO_STATE[env_id])

    # 1. Kirby environments
    if env_id == "Kirby-Dream-Land-1-full-image-v1":
        env = KirbyDreamLand1FullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Kirby-Dream-Land-1-minimal-image-v1":
        env = KirbyDreamLand1MinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )

    # 2. Pokemon environments
    elif env_id == "Pokemon-Blue-full-image-v1":
        env = PokemonBlueFullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Blue-minimal-image-v1":
        env = PokemonBlueMinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Gold-full-image-v1":
        env = PokemonGoldFullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Gold-minimal-image-v1":
        env = PokemonGoldMinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Red-full-image-v1":
        env = PokemonRedFullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Red-minimal-image-v1":
        env = PokemonRedMinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Silver-full-image-v1":
        env = PokemonSilverFullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Silver-minimal-image-v1":
        env = PokemonSilverMinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Yellow-full-image-v1":
        env = PokemonYellowFullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Yellow-minimal-image-v1":
        env = PokemonYellowMinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )

    # 3. Mario environments
    elif env_id == "Super-Mario-Land-1-full-image-v1":
        env = SuperMarioLand1FullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Super-Mario-Land-1-minimal-image-v1":
        env = SuperMarioLand1MinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )

    # 4. Tetris environments
    elif env_id == "Tetris-full-image-v1":
        env = TetrisFullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Tetris-minimal-image-v1":
        env = TetrisMinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    else:
        raise ValueError("Environment ID is not registered.")
    return env


def make_vec(
    env_id: str,
    num_envs: int = 1,
    vectorization_mode: str = "sync",
    **env_kwargs,
) -> gym.vector.SyncVectorEnv | gym.vector.AsyncVectorEnv:
    """
    A self-version of OpenAI's infamous env.vec_make(env_name).

    Args:
        env_id (str):
            A string identifier for the environment

        num_envs (int):
            The number of environments

        vectorization_mode (str):
            The vectorization mmode used.
            Can be either "async" or "sync".

    Returns:
        gym.vector.SyncVectorEnv | gym.vector.AsyncVectorEnv:
            The vectorized environment
    """
    if num_envs <= 0:
        raise ValueError("Number of environments must be greater than 0.")
    if vectorization_mode not in ["async", "sync"]:
        raise ValueError("Invalid vectorization mode.")

    def create_env(_: int) -> Callable[[], gym.Env]:
        def _make_env():
            return make(env_id, **env_kwargs)

        return _make_env

    env_fns = [create_env(env_num) for env_num in range(num_envs)]

    if vectorization_mode == "async":
        return gym.vector.AsyncVectorEnv(env_fns)
    else:
        return gym.vector.SyncVectorEnv(env_fns)


registered_envs = [
    "Kirby-Dream-Land-1-full-image-v1",
    "Kirby-Dream-Land-1-minimal-image-v1",
    "Pokemon-Blue-full-image-v1",
    "Pokemon-Blue-minimal-image-v1",
    "Pokemon-Gold-full-image-v1",
    "Pokemon-Gold-minimal-image-v1",
    "Pokemon-Red-full-image-v1",
    "Pokemon-Red-minimal-image-v1",
    "Pokemon-Silver-full-image-v1",
    "Pokemon-Silver-minimal-image-v1",
    "Pokemon-Yellow-full-image-v1",
    "Pokemon-Yellow-minimal-image-v1",
    "Super-Mario-Land-1-full-image-v1",
    "Super-Mario-Land-1-minimal-image-v1",
    "Tetris-full-image-v1",
    "Tetris-minimal-image-v1",
]

assert registered_envs == sorted(registered_envs), (
    f"registered_envs needs to be sorted into {sorted(registered_envs)}!"
)
