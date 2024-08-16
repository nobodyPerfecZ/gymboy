"""Gymboy environments."""

from gymboy.environments import mario
from gymboy.environments import pokemon

# Mario environments
SuperMarioLand1 = mario.SuperMarioLand1
SuperMarioLand2 = mario.SuperMarioLand2

# Pokemon environments
PokemonBlue = pokemon.PokemonBlue
PokemonRed = pokemon.PokemonRed
PokemonYellow = pokemon.PokemonYellow
PokemonGold = pokemon.PokemonGold
PokemonSilver = pokemon.PokemonSilver

__all__ = [
    "SuperMarioLand1",
    "SuperMarioLand2",
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
    "PokemonGold",
    "PokemonSilver",
]
