"""Pokemon Gen 1 environments."""

from .blue import PokemonBlueFlatten, PokemonBlueImage
from .red import PokemonRedFlatten, PokemonRedImage
from .yellow import PokemonYellowFlatten, PokemonYellowImage

__all__ = [
    "PokemonBlueFlatten",
    "PokemonBlueImage",
    "PokemonRedFlatten",
    "PokemonRedImage",
    "PokemonYellowFlatten",
    "PokemonYellowImage",
]

assert __all__ == sorted(__all__)
