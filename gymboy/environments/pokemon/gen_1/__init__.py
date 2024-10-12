"""Pokemon Gen 1 environments."""

from .blue import PokemonBlueFlatten, PokemonBlueFullImage, PokemonBlueMinimalImage
from .red import PokemonRedFlatten, PokemonRedFullImage, PokemonRedMinimalImage
from .yellow import (
    PokemonYellowFlatten,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
)

__all__ = [
    "PokemonBlueFlatten",
    "PokemonBlueFullImage",
    "PokemonBlueMinimalImage",
    "PokemonRedFlatten",
    "PokemonRedFullImage",
    "PokemonRedMinimalImage",
    "PokemonYellowFlatten",
    "PokemonYellowFullImage",
    "PokemonYellowMinimalImage",
]

assert __all__ == sorted(__all__)
