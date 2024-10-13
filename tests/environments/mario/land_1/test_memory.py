"""Tests mario/land_1/_memory.py."""

import unittest

import numpy as np
from pyboy import PyBoy

from gymboy.environments.mario.land_1._memory import (
    _coins,
    _game_area,
    _game_over,
    _level_finished,
    _lives,
    _score,
    _time,
    _time_over,
    _world_level,
)


class TestMemory(unittest.TestCase):
    """Tests the methods under mario/land_1/_memory.py."""

    def setUp(self):
        self.pyboy = PyBoy("./gymboy/resources/roms/mario/land_1/super_mario_land_1.gb")
        with open(
            "./gymboy/resources/states/mario/land_1/super_mario_land_1_1_1_test.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_score(self):
        """Tests the _score() method."""
        self.assertEqual(7900, _score(self.pyboy))

    def test_world_level(self):
        """Tests the _world_level() method."""
        self.assertEqual((1, 1), _world_level(self.pyboy))

    def test_coins(self):
        """Tests the _coins() method."""
        self.assertEqual(35, _coins(self.pyboy))

    def test_lives(self):
        """Tests the _lives() method."""
        self.assertEqual(2, _lives(self.pyboy))

    def test_time(self):
        """Tests the _time() method."""
        self.assertEqual(264, _time(self.pyboy))

    def test_time_over(self):
        """Tests the _time_over() method."""
        self.assertFalse(_time_over(self.pyboy))

    def test_level_finished(self):
        """Tests the _level_finished() method."""
        self.assertFalse(_level_finished(self.pyboy))

    def test_game_over(self):
        """Tests the _game_over() method."""
        self.assertFalse(_game_over(self.pyboy))

    def test_game_area(self):
        """Tests the _game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy),
            np.array(
                [
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 1, 0, 300, 300, 300, 300, 300, 300, 275, 289 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 17, 16, 300, 300, 300, 300, 300, 300, 292, 313 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 239, 239, 239, 300, 300, 300, 300, 300, 300, 142, 143, 142 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 239, 239, 239, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 275, 289 ],
                    [ 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 292, 313 ],
                    [ 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143 ],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
