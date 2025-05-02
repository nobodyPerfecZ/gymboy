"""Gymboy environments."""

# Kirby environments
from .kirby import (
    KirbyDreamLand1Flatten,
    KirbyDreamLand1FullImage,
    KirbyDreamLand1MinimalImage,
)

# Mario environments
from .mario import (
    SuperMarioLand1Flatten,
    SuperMarioLand1FullImage,
    SuperMarioLand1MinimalImage,
)

# Pokemon environments
from .pokemon import (
    PokemonBlueFlatten,
    PokemonBlueFullImage,
    PokemonBlueMinimalImage,
    PokemonGoldFlatten,
    PokemonGoldFullImage,
    PokemonGoldMinimalImage,
    PokemonRedFlatten,
    PokemonRedFullImage,
    PokemonRedMinimalImage,
    PokemonSilverFlatten,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
    PokemonYellowFlatten,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
)

# Tetris environments
from .tetris import TetrisFlatten, TetrisFullImage, TetrisMinimalImage

__all__ = [
    "KirbyDreamLand1Flatten",
    "KirbyDreamLand1FullImage",
    "KirbyDreamLand1MinimalImage",
    "PokemonBlueFlatten",
    "PokemonBlueFullImage",
    "PokemonBlueMinimalImage",
    "PokemonGoldFlatten",
    "PokemonGoldFullImage",
    "PokemonGoldMinimalImage",
    "PokemonRedFlatten",
    "PokemonRedFullImage",
    "PokemonRedMinimalImage",
    "PokemonSilverFlatten",
    "PokemonSilverFullImage",
    "PokemonSilverMinimalImage",
    "PokemonYellowFlatten",
    "PokemonYellowFullImage",
    "PokemonYellowMinimalImage",
    "SuperMarioLand1Flatten",
    "SuperMarioLand1FullImage",
    "SuperMarioLand1MinimalImage",
    "TetrisFlatten",
    "TetrisFullImage",
    "TetrisMinimalImage",
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
