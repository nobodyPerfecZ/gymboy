"""Pokemon Gen 1 environments."""

from gymboy.environments.pokemon.gen_1 import blue
from gymboy.environments.pokemon.gen_1 import red
from gymboy.environments.pokemon.gen_1 import yellow

PokemonBlue = blue.PokemonBlue
PokemonRed = red.PokemonRed
PokemonYellow = yellow.PokemonYellow


__all__ = [
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
]
