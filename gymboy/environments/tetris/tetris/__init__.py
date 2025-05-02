"""Tetris environment."""

from .tetris import TetrisFlatten, TetrisFullImage, TetrisMinimalImage

__all__ = ["TetrisFlatten", "TetrisFullImage", "TetrisMinimalImage"]

assert __all__ == sorted(__all__), f"__all__ needs to be sorted into {sorted(__all__)}!"
