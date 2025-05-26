"""Pokemon environments."""

from .gen_1 import (
    PokemonBlueFullImage,
    PokemonBlueMinimalImage,
    PokemonRedFullImage,
    PokemonRedMinimalImage,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
)
from .gen_2 import (
    PokemonGoldFullImage,
    PokemonGoldMinimalImage,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
)

__all__ = [
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
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
