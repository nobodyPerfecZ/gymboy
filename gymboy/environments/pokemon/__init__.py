"""Pokemon environments."""

from .gen_1 import (
    PokemonBlueFlatten,
    PokemonBlueImage,
    PokemonRedFlatten,
    PokemonRedImage,
    PokemonYellowFlatten,
    PokemonYellowImage,
)
from .gen_2 import (
    PokemonGoldFlatten,
    PokemonGoldImage,
    PokemonSilverFlatten,
    PokemonSilverImage,
)

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
]

assert __all__ == sorted(__all__)
