"""Gymboy environments."""

# Mario environments
from .mario import SuperMarioLand1Flatten, SuperMarioLand1Image

# Pokemon environments
from .pokemon import (
    PokemonBlueFlatten,
    PokemonBlueImage,
    PokemonGoldFlatten,
    PokemonGoldImage,
    PokemonRedFlatten,
    PokemonRedImage,
    PokemonSilverFlatten,
    PokemonSilverImage,
    PokemonYellowFlatten,
    PokemonYellowImage,
)

# Tetris environments
from .tetris import TetrisFlatten, TetrisImage

__all__ = [
    "PokemonBlueFlatten",
    "PokemonBlueImage",
    "PokemonGoldFlatten",
    "PokemonGoldImage",
    "PokemonRedFlatten",
    "PokemonRedImage",
    "PokemonSilverFlatten",
    "PokemonSilverImage",
    "PokemonYellowFlatten",
    "PokemonYellowImage",
    "SuperMarioLand1Flatten",
    "SuperMarioLand1Image",
    "TetrisFlatten",
    "TetrisImage",
]

assert __all__ == sorted(__all__)
