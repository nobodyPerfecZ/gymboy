"""Pokemon Gen 2 environments."""

from .gold import PokemonGoldFullImage, PokemonGoldMinimalImage
from .silver import PokemonSilverFullImage, PokemonSilverMinimalImage

__all__ = [
    "PokemonGoldFullImage",
    "PokemonGoldMinimalImage",
    "PokemonSilverFullImage",
    "PokemonSilverMinimalImage",
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
