"""Pokemon Gen 2 environments."""

from gymboy.environments.pokemon.gen_2.gold import PokemonGoldFlatten, PokemonGoldImage
from gymboy.environments.pokemon.gen_2.silver import (
    PokemonSilverFlatten,
    PokemonSilverImage,
)

__all__ = [
    "PokemonGoldFlatten",
    "PokemonGoldImage",
    "PokemonSilverFlatten",
    "PokemonSilverImage",
]
