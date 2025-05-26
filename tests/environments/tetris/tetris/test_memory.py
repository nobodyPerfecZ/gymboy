"""Tests tetris/tetris/_memory.py."""

import numpy as np
from pyboy import PyBoy

from gymboy.environments.tetris.tetris._memory import (
    _game_area,
    _game_over,
    _level,
    _next_block,
    _score,
)


class TestMemory:
    """Tests the methods under tetris/tetris/_memory.py."""

    rom_path = "./resources/roms/tetris/tetris/tetris.gb"
    init_state_path1 = "./resources/tests/tetris/tetris/tetris_lvl_5.state"
    init_state_path2 = "./resources/tests/tetris/tetris/tetris_lvl_5_end.state"

    @classmethod
    def setup_class(cls):
        cls.pyboy1 = PyBoy(cls.rom_path, sound_emulated=False)
        with open(cls.init_state_path1, "rb") as f:
            cls.pyboy1.load_state(f)
        cls.pyboy1.tick(1)

        cls.pyboy2 = PyBoy(cls.rom_path, sound_emulated=False)
        with open(cls.init_state_path2, "rb") as f:
            cls.pyboy2.load_state(f)
        cls.pyboy2.tick(1)

    @classmethod
    def teardown_class(cls):
        cls.pyboy1.stop()
        cls.pyboy2.stop()

    def test_score(self):
        """Tests the score() method."""
        assert _score(self.pyboy1) == 8913
        assert _score(self.pyboy2) == 3790

    def test_level(self):
        """Tests the level() method."""
        assert _level(self.pyboy1) == 5
        assert _level(self.pyboy2) == 5

    def test_next_block(self):
        """Tests the next_block() method."""
        assert _next_block(self.pyboy1) == 4
        assert _next_block(self.pyboy2) == 16

    def test_game_over(self):
        """Tests the game_over() method."""
        assert _game_over(self.pyboy1) is False
        assert _game_over(self.pyboy2) is True

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy1),
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
            _game_area(self.pyboy2),
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
