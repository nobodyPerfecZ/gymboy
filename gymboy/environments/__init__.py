"""Gymboy environments."""

# Tetris environments
from gymboy.environments.tetris import TetrisFlatten, TetrisImage

# Mario environments
from gymboy.environments.mario import SuperMarioLand1Flatten, SuperMarioLand1Image

# Pokemon environments
from gymboy.environments.pokemon import (
    PokemonBlueFlatten,
    PokemonBlueImage,
    PokemonRedFlatten,
    PokemonRedImage,
    PokemonYellowFlatten,
    PokemonYellowImage,
    PokemonGoldFlatten,
    PokemonGoldImage,
    PokemonSilverFlatten,
    PokemonSilverImage,
)


__all__ = [
    "TetrisFlatten",
    "TetrisImage",
    "SuperMarioLand1Flatten",
    "SuperMarioLand1Image",
    "PokemonBlueFlatten",
    "PokemonBlueImage",
    "PokemonRedFlatten",
    "PokemonRedImage",
    "PokemonYellowFlatten",
    "PokemonYellowImage",
    "PokemonGoldFlatten",
    "PokemonGoldImage",
    "PokemonSilverFlatten",
    "PokemonSilverImage",
]
