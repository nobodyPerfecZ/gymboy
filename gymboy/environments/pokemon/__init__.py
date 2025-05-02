"""Pokemon environments."""

from .gen_1 import (
    PokemonBlueFlatten,
    PokemonBlueFullImage,
    PokemonBlueMinimalImage,
    PokemonRedFlatten,
    PokemonRedFullImage,
    PokemonRedMinimalImage,
    PokemonYellowFlatten,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
)
from .gen_2 import (
    PokemonGoldFlatten,
    PokemonGoldFullImage,
    PokemonGoldMinimalImage,
    PokemonSilverFlatten,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
)

__all__ = [
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
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
