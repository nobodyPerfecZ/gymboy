"""Gymboy environments."""

# Tetris environments
from gymboy.environments.tetris import TetrisFlatten, TetrisImage

# Mario environments
from gymboy.environments.mario import SuperMarioLand1Flatten, SuperMarioLand1Image

# Pokemon environments
from gymboy.environments.pokemon import (
    PokemonBlue,
    PokemonRed,
    PokemonYellow,
    PokemonGold,
    PokemonSilver,
)


__all__ = [
    "TetrisFlatten",
    "TetrisImage",
    "SuperMarioLand1Flatten",
    "SuperMarioLand1Image",
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
    "PokemonGold",
    "PokemonSilver",
]
