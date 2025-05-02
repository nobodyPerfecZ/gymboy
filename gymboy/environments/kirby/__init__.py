"""Kirby environments."""

from .dream_land_1 import (
    KirbyDreamLand1Flatten,
    KirbyDreamLand1FullImage,
    KirbyDreamLand1MinimalImage,
)

__all__ = [
    "KirbyDreamLand1Flatten",
    "KirbyDreamLand1FullImage",
    "KirbyDreamLand1MinimalImage",
]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
