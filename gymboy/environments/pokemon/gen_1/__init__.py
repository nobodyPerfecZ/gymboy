"""Pokemon Gen 1 environments."""

from .blue import PokemonBlueFullImage, PokemonBlueMinimalImage
from .red import PokemonRedFullImage, PokemonRedMinimalImage
from .yellow import PokemonYellowFullImage, PokemonYellowMinimalImage

__all__ = [
    "PokemonBlueFullImage",
    "PokemonBlueMinimalImage",
    "PokemonRedFullImage",
    "PokemonRedMinimalImage",
    "PokemonYellowFullImage",
    "PokemonYellowMinimalImage",
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
