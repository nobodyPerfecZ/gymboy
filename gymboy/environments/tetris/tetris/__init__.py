"""Tetris environment."""

from .tetris import TetrisFullImage, TetrisMinimalImage

__all__ = ["TetrisFullImage", "TetrisMinimalImage"]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
