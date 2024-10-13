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
        self.rom_path = "./gymboy/resources/roms/mario/land_1/super_mario_land_1.gb"
        self.init_state_path1 = "./gymboy/resources/states/mario/land_1/super_mario_land_1_test_1.state"
        self.init_state_path2 = "./gymboy/resources/states/mario/land_1/super_mario_land_1_test_2.state"
        self.init_state_path3 = "./gymboy/resources/states/mario/land_1/super_mario_land_1_test_3.state"

        self.pyboy1 = PyBoy(self.rom_path)
        with open(self.init_state_path1, "rb") as f:
            self.pyboy1.load_state(f)
        self.pyboy1.tick(1)

        self.pyboy2 = PyBoy(self.rom_path)
        with open(self.init_state_path2, "rb") as f:
            self.pyboy2.load_state(f)
        self.pyboy2.tick(1)

        self.pyboy3 = PyBoy(self.rom_path)
        with open(self.init_state_path3, "rb") as f:
            self.pyboy3.load_state(f)
        self.pyboy3.tick(1)

    def tearDown(self):
        self.pyboy1.stop()
        self.pyboy2.stop()
        self.pyboy3.stop()

    def test_score(self):
        """Tests the _score() method."""
        self.assertEqual(7900, _score(self.pyboy1))
        self.assertEqual(12090, _score(self.pyboy2))
        self.assertEqual(18770, _score(self.pyboy3))

    def test_world_level(self):
        """Tests the _world_level() method."""
        self.assertEqual((1, 1), _world_level(self.pyboy1))
        self.assertEqual((1, 2), _world_level(self.pyboy2))
        self.assertEqual((1, 3), _world_level(self.pyboy3))

    def test_coins(self):
        """Tests the _coins() method."""
        self.assertEqual(35, _coins(self.pyboy1))
        self.assertEqual(41, _coins(self.pyboy2))
        self.assertEqual(47, _coins(self.pyboy3))

    def test_lives(self):
        """Tests the _lives() method."""
        self.assertEqual(2, _lives(self.pyboy1))
        self.assertEqual(1, _lives(self.pyboy2))
        self.assertEqual(6, _lives(self.pyboy3))

    def test_time(self):
        """Tests the _time() method."""
        self.assertEqual(264, _time(self.pyboy1))
        self.assertEqual(388, _time(self.pyboy2))
        self.assertEqual(395, _time(self.pyboy3))

    def test_time_over(self):
        """Tests the _time_over() method."""
        self.assertFalse(_time_over(self.pyboy1))
        self.assertFalse(_time_over(self.pyboy2))
        self.assertFalse(_time_over(self.pyboy3))

    def test_level_finished(self):
        """Tests the _level_finished() method."""
        self.assertFalse(_level_finished(self.pyboy1))
        self.assertFalse(_level_finished(self.pyboy2))
        self.assertFalse(_level_finished(self.pyboy3))

    def test_game_over(self):
        """Tests the _game_over() method."""
        self.assertFalse(_game_over(self.pyboy1))
        self.assertFalse(_game_over(self.pyboy2))
        self.assertFalse(_game_over(self.pyboy3))

    def test_game_area(self):
        """Tests the _game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy1),
            np.array([
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
            ]),
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy2),
            np.array([
                [339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339, 339],
                [320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320, 320],
                [300, 300, 300, 300, 321, 322, 323, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 324, 325, 326, 327, 300, 300, 300, 300, 244, 129, 244, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 300, 300,   0,   1, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 300, 300,  16,  17, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 360, 361, 361, 361, 362, 360, 361, 362, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 300, 300, 311, 300, 300, 300, 311, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 300, 300, 311, 300, 300, 300, 311, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 300, 300, 311, 300, 300, 300, 311, 300, 300, 300, 300, 300, 300, 300],
                [300, 360, 361, 361, 361, 361, 362, 300, 311, 300, 300, 300, 311, 300, 360, 361, 361, 361, 361, 361],
                [300, 300, 300, 311, 311, 300, 300, 300, 311, 300, 300, 300, 311, 300, 300, 300, 300, 311, 310, 350],
                [300, 300, 300, 311, 311, 300, 300, 300, 311, 300, 300, 300, 311, 300, 300, 300, 300, 311, 300, 300],
                [336, 300, 300, 311, 311, 300, 300, 300, 311, 300, 300, 300, 311, 300, 310, 350, 310, 311, 300, 300],
                [336, 300, 300, 311, 311, 300, 300, 300, 311, 300, 300, 300, 311, 310, 300, 300, 350, 311, 300, 300],
            ])
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy3),
            np.array([
                [357, 358, 357, 358, 357, 358, 357, 358, 357, 358, 357, 358, 357, 366, 365, 358, 357, 358, 357, 358],
                [366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365],
                [365, 366, 365, 366, 365, 366, 365, 358, 300, 300, 300, 300, 300, 300, 300, 300, 357, 366, 365, 366],
                [366, 365, 366, 365, 358, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 357, 366, 365],
                [365, 366, 345, 346, 341, 342, 343, 344, 345, 346, 343, 300, 342, 299, 341, 343, 312, 312, 357, 358],
                [357, 358, 347, 348, 300, 300, 300, 299, 347, 348, 341, 300, 343, 300, 300, 300, 299, 341, 357, 358],
                [357, 358, 300, 300, 300, 349, 300, 300, 300, 300, 300, 300, 300, 300, 349, 300, 300, 300, 357, 358],
                [357, 358, 300, 300, 300, 309, 300, 300, 300, 300, 300, 300, 300, 300, 309, 300, 300, 300, 357, 358],
                [357, 358, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 357, 358],
                [357, 358, 351, 300, 300, 300, 300, 300, 300, 300, 351, 300, 300, 300, 300, 300, 300, 300, 300, 300],
                [357, 358, 300, 300, 300, 300, 300, 129, 130, 129, 130, 129, 300, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],
                [300, 300, 300, 300,  32,  33, 300, 300, 300, 300, 300, 300, 300, 357, 358, 300, 300, 300, 300, 300],
                [300, 300, 300, 300,  48,  49, 300, 300, 300, 300, 300, 300, 300, 357, 358, 300, 300, 300, 300, 300],
                [357, 358, 357, 358, 357, 358, 357, 358, 357, 358, 357, 358, 357, 366, 365, 358, 357, 358, 357, 358],
                [366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365, 366, 365],
            ])
        )


if __name__ == "__main__":
    unittest.main()
