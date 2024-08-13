"""An version of OpenAI's infamous env.make(env_name)."""

import gymnasium as gym

from gymboy.environments.pokemon import blue, gold, red, silver, yellow

# =============================================================================


def make(env_id: str, **env_kwargs) -> gym.Env:
    """
    A self-version of OpenAI's infamous env.make(env_name).

    Args:
        env_id (str):
            A string identifier for the environment.

        **env_kwargs:
            Keyword arguments to pass to the environment.

    Returns:

      A tuple of the environment and the default parameters.
    """
    if env_id not in registered_envs:
        raise ValueError(f"{env_id} is not in registered gymboy environments.")

    # 1. Pokemon environments
    if env_id == "Pokemon-Blue-v1":
        env = blue.PokemonBlue(**env_kwargs)
    elif env_id == "Pokemon-Red-v1":
        env = red.PokemonRed(**env_kwargs)
    elif env_id == "Pokemon-Yellow-v1":
        env = yellow.PokemonYellow(**env_kwargs)
    elif env_id == "Pokemon-Gold-v1":
        env = gold.PokemonGold(**env_kwargs)
    elif env_id == "Pokemon-Silver-v1":
        env = silver.PokemonSilver(**env_kwargs)
    else:
        raise ValueError("Environment ID is not registered.")
    return env


registered_envs = [
    "Pokemon-Blue-v1",
    "Pokemon-Red-v1",
    "Pokemon-Yellow-v1",
    "Pokemon-Gold-v1",
    "Pokemon-Silver-v1",
]
