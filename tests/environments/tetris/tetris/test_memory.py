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
        self.rom_path = "./resources/roms/tetris/tetris/tetris.gb"
        self.init_state_path1 = (
            "./resources/states/tetris/tetris/tetris_after_intro.state"
        )
        self.init_state_path2 = "./resources/states/tetris/tetris/tetris_lvl_5.state"
        self.init_state_path3 = (
            "./resources/states/tetris/tetris/tetris_lvl_5_end.state"
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
        """Tests the score() method."""
        self.assertEqual(0, _score(self.pyboy1))
        self.assertEqual(8913, _score(self.pyboy2))
        self.assertEqual(3790, _score(self.pyboy3))

    def test_level(self):
        """Tests the level() method."""
        self.assertEqual(9, _level(self.pyboy1))
        self.assertEqual(5, _level(self.pyboy2))
        self.assertEqual(5, _level(self.pyboy3))

    def test_next_block(self):
        """Tests the next_block() method."""
        self.assertEqual(8, _next_block(self.pyboy1))
        self.assertEqual(4, _next_block(self.pyboy2))
        self.assertEqual(16, _next_block(self.pyboy3))

    def test_game_over(self):
        """Tests the game_over() method."""
        self.assertFalse(_game_over(self.pyboy1))
        self.assertFalse(_game_over(self.pyboy2))
        self.assertTrue(_game_over(self.pyboy3))

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy1),
            np.array(
                [
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
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
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
                ]
            ),
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy2),
            np.array(
                [
                    [47, 47, 128, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 136, 47, 47, 47, 47, 47, 47, 47],
                    [47, 47, 136, 133, 133, 133, 47, 47, 47, 47],
                    [47, 47, 137, 47, 133, 47, 47, 131, 131, 47],
                    [47, 47, 130, 47, 47, 131, 131, 131, 131, 133],
                    [47, 130, 130, 47, 47, 131, 131, 47, 133, 133],
                    [47, 130, 134, 134, 47, 131, 131, 130, 130, 133],
                    [47, 134, 134, 130, 130, 131, 131, 47, 130, 130],
                    [47, 47, 47, 134, 130, 130, 133, 133, 133, 47],
                    [47, 47, 47, 134, 134, 132, 132, 133, 131, 131],
                    [47, 47, 47, 128, 134, 47, 132, 47, 131, 131],
                    [47, 47, 130, 136, 132, 132, 132, 129, 129, 129],
                    [47, 130, 130, 136, 132, 132, 132, 132, 132, 129],
                    [47, 134, 133, 128, 129, 129, 129, 130, 130, 136],
                    [131, 131, 128, 136, 47, 130, 129, 130, 134, 137],
                    [131, 131, 136, 136, 130, 130, 47, 133, 134, 134],
                    [131, 131, 130, 130, 47, 47, 134, 134, 132, 132],
                    [131, 131, 130, 133, 47, 47, 133, 134, 132, 132],
                ]
            ),
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy3),
            np.array(
                [
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                    [135, 135, 135, 135, 135, 135, 135, 135, 135, 135],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
