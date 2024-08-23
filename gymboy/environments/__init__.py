"""Gymboy environments."""

from gymboy.environments import tetris
from gymboy.environments import mario
from gymboy.environments import pokemon

# Tetris environments
Tetris = tetris.Tetris

# Mario environments
SuperMarioLand1 = mario.SuperMarioLand1

# Pokemon environments
PokemonBlue = pokemon.PokemonBlue
PokemonRed = pokemon.PokemonRed
PokemonYellow = pokemon.PokemonYellow
PokemonGold = pokemon.PokemonGold
PokemonSilver = pokemon.PokemonSilver

__all__ = [
    "Tetris",
    "SuperMarioLand1",
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
    "PokemonGold",
    "PokemonSilver",
]
