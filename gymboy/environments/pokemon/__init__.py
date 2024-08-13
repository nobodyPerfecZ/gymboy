"""Pokemon environments."""

from gymboy.environments.pokemon import blue
from gymboy.environments.pokemon import red
from gymboy.environments.pokemon import yellow
from gymboy.environments.pokemon import gold
from gymboy.environments.pokemon import silver


PokemonBlue = blue.PokemonBlue
PokemonRed = red.PokemonRed
PokemonYellow = yellow.PokemonYellow
PokemonGold = gold.PokemonGold
PokemonSilver = silver.PokemonSilver


__all__ = [
    "PokemonBlue",
    "PokemonRed",
    "PokemonYellow",
    "PokemonGold",
    "PokemonSilver",
]
