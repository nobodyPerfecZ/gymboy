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
        self.rom_path = "./resources/roms/mario/land_1/super_mario_land_1.gb"
        self.init_state_path1 = (
            "./resources/states/mario/land_1/super_mario_land_1_after_intro.state"
        )
        self.init_state_path2 = (
            "./resources/states/mario/land_1/super_mario_land_1_lvl_1_1.state"
        )
        self.init_state_path3 = (
            "./resources/states/mario/land_1/super_mario_land_1_lvl_1_2.state"
        )

        self.pyboy1 = PyBoy(self.rom_path, sound_emulated=False)
        with open(self.init_state_path1, "rb") as f:
            self.pyboy1.load_state(f)
        self.pyboy1.tick(1)

        self.pyboy2 = PyBoy(self.rom_path, sound_emulated=False)
        with open(self.init_state_path2, "rb") as f:
            self.pyboy2.load_state(f)
        self.pyboy2.tick(1)

        self.pyboy3 = PyBoy(self.rom_path, sound_emulated=False)
        with open(self.init_state_path3, "rb") as f:
            self.pyboy3.load_state(f)
        self.pyboy3.tick(1)

    def tearDown(self):
        self.pyboy1.stop()
        self.pyboy2.stop()
        self.pyboy3.stop()

    def test_score(self):
        """Tests the _score() method."""
        self.assertEqual(0, _score(self.pyboy1))
        self.assertEqual(2700, _score(self.pyboy2))
        self.assertEqual(9270, _score(self.pyboy3))

    def test_world_level(self):
        """Tests the _world_level() method."""
        self.assertEqual((1, 1), _world_level(self.pyboy1))
        self.assertEqual((1, 1), _world_level(self.pyboy2))
        self.assertEqual((1, 2), _world_level(self.pyboy3))

    def test_coins(self):
        """Tests the _coins() method."""
        self.assertEqual(0, _coins(self.pyboy1))
        self.assertEqual(11, _coins(self.pyboy2))
        self.assertEqual(25, _coins(self.pyboy3))

    def test_lives(self):
        """Tests the _lives() method."""
        self.assertEqual(2, _lives(self.pyboy1))
        self.assertEqual(0, _lives(self.pyboy2))
        self.assertEqual(3, _lives(self.pyboy3))

    def test_time(self):
        """Tests the _time() method."""
        self.assertEqual(399, _time(self.pyboy1))
        self.assertEqual(398, _time(self.pyboy2))
        self.assertEqual(398, _time(self.pyboy3))

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
            np.array(
                [
                    [
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                    ],
                    [
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        321,
                        322,
                        321,
                        322,
                        323,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        324,
                        325,
                        326,
                        325,
                        326,
                        327,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        310,
                        350,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        310,
                        300,
                        300,
                        350,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        129,
                        310,
                        300,
                        300,
                        300,
                        300,
                        350,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        310,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        350,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        310,
                        350,
                        310,
                        300,
                        300,
                        300,
                        300,
                        306,
                        307,
                        300,
                        300,
                        350,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        368,
                        369,
                        300,
                        0,
                        1,
                        300,
                        306,
                        307,
                        305,
                        300,
                        300,
                        300,
                        300,
                        350,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        310,
                        370,
                        371,
                        300,
                        16,
                        17,
                        300,
                        305,
                        300,
                        305,
                        300,
                        300,
                        300,
                        300,
                        300,
                        350,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                    ],
                    [
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                    ],
                ]
            ),
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy2),
            np.array(
                [
                    [
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                    ],
                    [
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        244,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        244,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        130,
                        130,
                        130,
                        128,
                        130,
                        130,
                        300,
                        244,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        244,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        129,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        244,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        244,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        244,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        129,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        130,
                        130,
                        130,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        306,
                        307,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        306,
                        307,
                        305,
                        0,
                        1,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        305,
                        300,
                        305,
                        16,
                        17,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        336,
                        338,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                    ],
                    [
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        336,
                        338,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                    ],
                ]
            ),
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy3),
            np.array(
                [
                    [
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                        339,
                    ],
                    [
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                        320,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        321,
                        322,
                        323,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        321,
                        322,
                        323,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        324,
                        325,
                        326,
                        327,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        324,
                        325,
                        326,
                        327,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        244,
                        300,
                        244,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        360,
                        361,
                        361,
                        361,
                        362,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        306,
                        307,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        311,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        305,
                        306,
                        307,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        311,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        300,
                        300,
                        305,
                        305,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        311,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        306,
                        307,
                        305,
                        305,
                        300,
                        300,
                        300,
                        300,
                        360,
                        361,
                        361,
                        361,
                        361,
                        362,
                        300,
                        311,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        305,
                        300,
                        0,
                        1,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        311,
                        311,
                        300,
                        300,
                        300,
                        311,
                        300,
                        300,
                    ],
                    [
                        300,
                        300,
                        305,
                        300,
                        16,
                        17,
                        300,
                        300,
                        300,
                        300,
                        300,
                        300,
                        311,
                        311,
                        300,
                        300,
                        300,
                        311,
                        300,
                        300,
                    ],
                    [
                        300,
                        338,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        352,
                        336,
                        300,
                        300,
                        311,
                        311,
                        300,
                        300,
                        300,
                        311,
                        300,
                        300,
                    ],
                    [
                        300,
                        338,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        353,
                        336,
                        300,
                        300,
                        311,
                        311,
                        300,
                        300,
                        300,
                        311,
                        300,
                        300,
                    ],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
