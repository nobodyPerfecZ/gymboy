"""Gymboy environments."""

# Kirby environments
from .kirby import KirbyDreamLand1Flatten, KirbyDreamLand1Image

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
    "KirbyDreamLand1Flatten",
    "KirbyDreamLand1Image",
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
