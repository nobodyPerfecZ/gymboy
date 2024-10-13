"""Tests tetris/tetris/_memory.py."""

import unittest

import numpy as np
from pyboy import PyBoy

from gymboy.environments.tetris.tetris._memory import (
    _game_area,
    _game_over,
    _level,
    _next_block,
    _score,
)


class TestMemory(unittest.TestCase):
    """Tests the methods under tetris/tetris/_memory.py."""

    def setUp(self):
        self.pyboy = PyBoy(gamerom="./gymboy/resources/roms/tetris/tetris/tetris.gb")
        with open(
            "./gymboy/resources/states/tetris/tetris/tetris_test.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_score(self):
        """Tests the score() method."""
        self.assertEqual(20, _score(self.pyboy))

    def test_level(self):
        """Tests the level() method."""
        self.assertEqual(9, _level(self.pyboy))

    def test_next_block(self):
        """Tests the next_block() method."""
        self.assertEqual(24, _next_block(self.pyboy))

    def test_game_over(self):
        """Tests the game_over() method."""
        self.assertFalse(_game_over(self.pyboy))

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy),
            np.array(
                [
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 129, 129, 129, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 129, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 129, 129, 129],
                    [47, 47, 47, 47, 47, 47, 132, 132, 132, 129],
                    [47, 47, 47, 47, 47, 47, 132, 130, 47, 47],
                    [47, 47, 47, 47, 47, 47, 130, 130, 47, 47],
                    [47, 134, 134, 133, 133, 133, 130, 47, 47, 47],
                    [134, 134, 47, 134, 133, 132, 132, 132, 47, 47],
                    [47, 134, 134, 134, 134, 132, 131, 131, 131, 131],
                    [134, 134, 47, 47, 134, 47, 131, 131, 131, 131],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
