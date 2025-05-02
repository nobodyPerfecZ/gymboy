"""Pokemon Gen 2 environments."""

from .gold import PokemonGoldFlatten, PokemonGoldFullImage, PokemonGoldMinimalImage
from .silver import (
    PokemonSilverFlatten,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
)

__all__ = [
    "PokemonGoldFlatten",
    "PokemonGoldFullImage",
    "PokemonGoldMinimalImage",
    "PokemonSilverFlatten",
    "PokemonSilverFullImage",
    "PokemonSilverMinimalImage",
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
