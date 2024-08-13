"""Gymboy environments."""

from gymboy.environments import mario
from gymboy.environments import pokemon

# Mario environments
SuperMarioLand = mario.SuperMarioLand
SuperMarioLand2 = mario.SuperMarioLand2

# Pokemon environments
PokemonBlue = pokemon.PokemonBlue
PokemonRed = pokemon.PokemonRed
PokemonYellow = pokemon.PokemonYellow
PokemonGold = pokemon.PokemonGold
PokemonSilver = pokemon.PokemonSilver

__all__ = [
    "SuperMarioLand",
    "SuperMarioLand2",
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
    "PokemonGold",
    "PokemonSilver",
]
