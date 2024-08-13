"""Mario environments."""

from gymboy.environments.mario import land_2
from gymboy.environments.mario import land


SuperMarioLand = land.SuperMarioLand
SuperMarioLand2 = land_2.SuperMarioLand2

__all__ = [
    "SuperMarioLand",
    "SuperMarioLand2",
]
