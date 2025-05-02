"""An version of OpenAI's infamous env.make(env_name)."""

from typing import Callable

import gymnasium as gym

from .environments import (
    KirbyDreamLand1Flatten,
    KirbyDreamLand1FullImage,
    KirbyDreamLand1MinimalImage,
    PokemonBlueFlatten,
    PokemonBlueFullImage,
    PokemonBlueMinimalImage,
    PokemonGoldFlatten,
    PokemonGoldFullImage,
    PokemonGoldMinimalImage,
    PokemonRedFlatten,
    PokemonRedFullImage,
    PokemonRedMinimalImage,
    PokemonSilverFlatten,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
    PokemonYellowFlatten,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
    SuperMarioLand1Flatten,
    SuperMarioLand1FullImage,
    SuperMarioLand1MinimalImage,
    TetrisFlatten,
    TetrisFullImage,
    TetrisMinimalImage,
)


def make(
    env_id: str, rom_path: str, init_state_path: str | None = None, **env_kwargs
) -> gym.Env:
    """
    A self-version of OpenAI's infamous env.make(env_name).

    Args:
        env_id (str):
            A string identifier for the environment.

        **env_kwargs:
            Keyword arguments to pass to the environment.

    Returns:
        gym.Env:
            The Gymboy environment
    """
    if env_id not in registered_envs:
        raise ValueError(f"{env_id} is not in registered gymboy environments.")

    # 1. Kirby environments
    if env_id == "Kirby-Dream-Land-1-flatten-v1":
        env = KirbyDreamLand1Flatten(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Kirby-Dream-Land-1-full-image-v1":
        env = KirbyDreamLand1FullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Kirby-Dream-Land-1-minimal-image-v1":
        env = KirbyDreamLand1MinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )

    # 2. Pokemon environments
    elif env_id == "Pokemon-Blue-flatten-v1":
        env = PokemonBlueFlatten(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Blue-full-image-v1":
        env = PokemonBlueFullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Blue-minimal-image-v1":
        env = PokemonBlueMinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Pokemon-Gold-flatten-v1":
        env = PokemonGoldFlatten(
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
    elif env_id == "Pokemon-Red-flatten-v1":
        env = PokemonRedFlatten(
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
    elif env_id == "Pokemon-Silver-flatten-v1":
        env = PokemonSilverFlatten(
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
    elif env_id == "Pokemon-Yellow-flatten-v1":
        env = PokemonYellowFlatten(
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
    elif env_id == "Super-Mario-Land-1-flatten-v1":
        env = SuperMarioLand1Flatten(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Super-Mario-Land-1-full-image-v1":
        env = SuperMarioLand1FullImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
    elif env_id == "Super-Mario-Land-1-minimal-image-v1":
        env = SuperMarioLand1MinimalImage(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )

    # 4. Tetris environments
    elif env_id == "Tetris-flatten-v1":
        env = TetrisFlatten(
            rom_path=rom_path, init_state_path=init_state_path, **env_kwargs
        )
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
) -> gym.vector.VectorEnv:
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
        gym.vector.VectorEnv:
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
    "Kirby-Dream-Land-1-flatten-v1",
    "Kirby-Dream-Land-1-full-image-v1",
    "Kirby-Dream-Land-1-minimal-image-v1",
    "Pokemon-Blue-flatten-v1",
    "Pokemon-Blue-full-image-v1",
    "Pokemon-Blue-minimal-image-v1",
    "Pokemon-Gold-flatten-v1",
    "Pokemon-Gold-full-image-v1",
    "Pokemon-Gold-minimal-image-v1",
    "Pokemon-Red-flatten-v1",
    "Pokemon-Red-full-image-v1",
    "Pokemon-Red-minimal-image-v1",
    "Pokemon-Silver-flatten-v1",
    "Pokemon-Silver-full-image-v1",
    "Pokemon-Silver-minimal-image-v1",
    "Pokemon-Yellow-flatten-v1",
    "Pokemon-Yellow-full-image-v1",
    "Pokemon-Yellow-minimal-image-v1",
    "Super-Mario-Land-1-flatten-v1",
    "Super-Mario-Land-1-full-image-v1",
    "Super-Mario-Land-1-minimal-image-v1",
    "Tetris-flatten-v1",
    "Tetris-full-image-v1",
    "Tetris-minimal-image-v1",
]

assert registered_envs == sorted(registered_envs)
