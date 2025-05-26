"""Gymboy environments."""

# Kirby environments
from .kirby import KirbyDreamLand1FullImage, KirbyDreamLand1MinimalImage

# Mario environments
from .mario import SuperMarioLand1FullImage, SuperMarioLand1MinimalImage

# Pokemon environments
from .pokemon import (
    PokemonBlueFullImage,
    PokemonBlueMinimalImage,
    PokemonGoldFullImage,
    PokemonGoldMinimalImage,
    PokemonRedFullImage,
    PokemonRedMinimalImage,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
)

# Tetris environments
from .tetris import TetrisFullImage, TetrisMinimalImage

__all__ = [
    "KirbyDreamLand1FullImage",
    "KirbyDreamLand1MinimalImage",
    "PokemonBlueFullImage",
    "PokemonBlueMinimalImage",
    "PokemonGoldFullImage",
    "PokemonGoldMinimalImage",
    "PokemonRedFullImage",
    "PokemonRedMinimalImage",
    "PokemonSilverFullImage",
    "PokemonSilverMinimalImage",
    "PokemonYellowFullImage",
    "PokemonYellowMinimalImage",
    "SuperMarioLand1FullImage",
    "SuperMarioLand1MinimalImage",
    "TetrisFullImage",
    "TetrisMinimalImage",
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
