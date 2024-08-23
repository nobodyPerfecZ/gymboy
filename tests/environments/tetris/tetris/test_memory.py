import unittest

from pyboy import PyBoy

from gymboy.environments.tetris.tetris.memory import *


class TestMemory(unittest.TestCase):
    """Tests the methods under methods.py."""

    def setUp(self):
        self.pyboy = PyBoy(gamerom="./gymboy/resources/roms/tetris/tetris/tetris.gb")
        with open(
            "./tests/resources/states/tetris/tetris/tetris_9.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_get_score(self):
        """Tests the get_score() method."""
        self.assertEqual(20, get_score(self.pyboy))

    def test_game_over(self):
        """Tests the game_over() method."""
        self.assertFalse(game_over(self.pyboy))


if __name__ == "__main__":
    unittest.main()
