"""Gymboy environments."""

# Tetris environments
from gymboy.environments.tetris import TetrisFlatten, TetrisImage

# Mario environments
from gymboy.environments.mario import SuperMarioLand1

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
    "SuperMarioLand1",
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
    "PokemonGold",
    "PokemonSilver",
]
