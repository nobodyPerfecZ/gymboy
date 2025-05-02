"""Super Mario Land environments."""

from .super_mario_land_1 import (
    SuperMarioLand1Flatten,
    SuperMarioLand1FullImage,
    SuperMarioLand1MinimalImage,
)

__all__ = [
    "SuperMarioLand1Flatten",
    "SuperMarioLand1FullImage",
    "SuperMarioLand1MinimalImage",
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
