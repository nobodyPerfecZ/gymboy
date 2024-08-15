"""Pokemon Gen 2 environments."""

from gymboy.environments.pokemon.gen_2 import gold
from gymboy.environments.pokemon.gen_2 import silver


PokemonGold = gold.PokemonGold
PokemonSilver = silver.PokemonSilver


__all__ = [
    "PokemonGold",
    "PokemonSilver",
]
