"""Tests kirby/dream_land_1/_memory.py."""

import unittest
import numpy as np
from pyboy import PyBoy

from gymboy.environments.kirby.dream_land_1._memory import (
    _boss_health,
    _game_area,
    _game_over,
    _kirby_health,
    _lives,
    _score,
)


class TestMemory12(unittest.TestCase):
    """Tests the methods under kirby/dream_land_1/_memory.py."""

    def setUp(self):
        self.pyboy = PyBoy(
            "./gymboy/resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb"
        )
        with open(
            "./gymboy/resources/states/kirby/dream_land_1/kirby_dream_land_1_test.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_score(self):
        """Tests the _score() method."""
        self.assertEqual(2800, _score(self.pyboy))

    def test_kirby_health(self):
        """Tests the _kirby_health() method."""
        self.assertEqual(1, _kirby_health(self.pyboy))

    def test_boss_health(self):
        """Tests the _boss_health() method."""
        self.assertEqual(0, _boss_health(self.pyboy))

    def test_lives(self):
        """Tests the _lives() method."""
        self.assertEqual(5, _lives(self.pyboy))

    def test_game_over(self):
        """Tests the _game_over() method."""
        self.assertFalse(_game_over(self.pyboy))

    def test_game_area(self):
        """Tests the _game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy),
            np.array(
                [
                    [292, 383, 383, 383, 383, 301, 383, 383, 383, 297, 383, 383, 383, 293, 292, 383, 383, 383, 383, 290],
                    [383, 298, 383, 383, 383, 383, 300, 294, 295, 296, 383, 383, 299, 383, 383, 298, 383, 383, 383, 383],
                    [383, 297, 383, 383, 383, 290, 291, 383, 383, 383, 383, 301, 383, 383, 383, 297, 383, 290, 291, 383],
                    [295, 296, 383, 383, 383, 383, 383, 383, 383, 383, 383, 383, 300, 294, 295, 296, 383, 383, 383, 383],
                    [383, 290, 291, 383, 383, 383, 383, 383, 383, 293, 292, 383, 383, 383, 383, 383, 383, 330, 331, 331],
                    [383, 383, 383, 383, 383, 383, 383, 383, 299, 383, 383, 298, 383, 383, 383, 383, 383, 334, 328, 328],
                    [383, 383, 383, 293, 292, 383, 383, 301, 383, 383, 383, 297, 383, 383, 383, 383, 383, 334, 328, 328],
                    [383, 383, 299, 383, 383, 298, 383, 383, 300, 294, 295, 296, 383, 383, 383, 383, 299, 334, 328, 328],
                    [383, 301, 383, 383, 383, 297, 383, 383, 383, 383, 383, 307, 308, 383, 383, 301, 383, 334, 328, 328],
                    [274, 383, 300, 294, 295, 296, 383,  14,  32,  76,  92, 309, 310, 383, 383, 383, 300, 334, 328, 328],
                    [332, 272, 274, 383, 383, 383, 383, 383, 383, 383, 383, 309, 310, 308, 383, 383, 383, 334, 328, 328],
                    [333, 275, 276, 272, 274, 272, 274,  34,  48,  50, 383, 309, 310, 310, 383, 272, 274, 334, 328, 328],
                    [328, 331, 331, 331, 331, 331, 332, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 328, 328, 328],
                    [328, 277, 278, 328, 328, 328, 333, 328, 328, 328, 328, 277, 278, 277, 278, 277, 278, 277, 278, 277],
                    [278, 279, 281, 277, 278, 328, 328, 331, 332, 277, 278, 279, 281, 279, 281, 279, 281, 279, 281, 279],
                    [281, 280, 282, 279, 281, 277, 278, 328, 333, 279, 281, 280, 282, 280, 282, 280, 282, 280, 282, 280],
                ],
            ),
        )


if __name__ == "__main__":
    unittest.main()
