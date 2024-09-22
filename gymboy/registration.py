"""An version of OpenAI's infamous env.make(env_name)."""

from typing import Callable

import gymnasium as gym

from gymboy.environments.mario import SuperMarioLand1Flatten, SuperMarioLand1Image
from gymboy.environments.pokemon import (
    PokemonBlue,
    PokemonGold,
    PokemonRed,
    PokemonSilver,
    PokemonYellow,
)
from gymboy.environments.tetris import TetrisImage, TetrisFlatten


def make(env_id: str, **env_kwargs) -> gym.Env:
    """
    A self-version of OpenAI's infamous env.make(env_name).

    Args:
        env_id (str):
            A string identifier for the environment

        **env_kwargs:
            Keyword arguments to pass to the environment

    Returns:
        gym.Env:
            The environment
    """
    if env_id not in registered_envs:
        raise ValueError(f"{env_id} is not in registered gymboy environments.")

    # 1. Tetris environments
    if env_id == "Tetris-flatten-v1":
        env = TetrisFlatten(**env_kwargs)
    elif env_id == "Tetris-image-v1":
        env = TetrisImage(**env_kwargs)

    # 2. Mario environments
    elif env_id == "Super-Mario-Land-1-flatten-v1":
        env = SuperMarioLand1Flatten(**env_kwargs)
    elif env_id == "Super-Mario-Land-1-image-v1":
        env = SuperMarioLand1Image(**env_kwargs)

    # 3. Pokemon environments
    elif env_id == "Pokemon-Blue-v1":
        env = PokemonBlue(**env_kwargs)
    elif env_id == "Pokemon-Red-v1":
        env = PokemonRed(**env_kwargs)
    elif env_id == "Pokemon-Yellow-v1":
        env = PokemonYellow(**env_kwargs)
    elif env_id == "Pokemon-Gold-v1":
        env = PokemonSilver(**env_kwargs)
    elif env_id == "Pokemon-Silver-v1":
        env = PokemonGold(**env_kwargs)
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

        num_envs (int, optional):
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

    def create_env(env_num: int) -> Callable[[], gym.Env]:
        def _make_env():
            return make(env_id, **env_kwargs)

        return _make_env

    env_fns = [create_env(env_num) for env_num in range(num_envs)]

    if vectorization_mode == "async":
        return gym.vector.AsyncVectorEnv(env_fns)
    else:
        return gym.vector.SyncVectorEnv(env_fns)


registered_envs = [
    "Tetris-flatten-v1",
    "Tetris-image-v1",
    "Super-Mario-Land-1-flatten-v1",
    "Super-Mario-Land-1-image-v1",
    "Pokemon-Blue-v1",
    "Pokemon-Red-v1",
    "Pokemon-Yellow-v1",
    "Pokemon-Gold-v1",
    "Pokemon-Silver-v1",
]
