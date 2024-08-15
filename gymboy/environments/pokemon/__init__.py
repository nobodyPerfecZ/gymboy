"""Pokemon environments."""

from gymboy.environments.pokemon import gen_1
from gymboy.environments.pokemon import gen_2


PokemonBlue = gen_1.PokemonBlue
PokemonRed = gen_1.PokemonRed
PokemonYellow = gen_1.PokemonYellow
PokemonGold = gen_2.PokemonGold
PokemonSilver = gen_2.PokemonSilver


__all__ = [
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
    "PokemonGold",
    "PokemonSilver",
]
