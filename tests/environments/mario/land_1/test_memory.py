import unittest

from pyboy import PyBoy

from gymboy.environments.mario.land_1.memory import *


class TestMemory(unittest.TestCase):
    """Tests the methods under methods.py."""

    def setUp(self):
        self.pyboy = PyBoy(
            gamerom="./gymboy/resources/roms/mario/land_1/super_mario_land_1.gb"
        )
        with open(
            "./tests/resources/states/mario/land_1/super_mario_land_1_1_1_end.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_get_score(self):
        """Tests the get_score() method."""
        self.assertEqual(7900, get_score(self.pyboy))

    def test_get_world_level(self):
        """Tests the get_world_level() method."""
        self.assertEqual((1, 1), get_world_level(self.pyboy))

    def test_get_coins(self):
        """Tests the get_coins() method."""
        self.assertEqual(35, get_coins(self.pyboy))

    def test_get_lives(self):
        """Tests the get_lives() method."""
        self.assertEqual(2, get_lives(self.pyboy))

    def test_get_time(self):
        """Tests the get_time() method."""
        self.assertEqual(264, get_time(self.pyboy))

    def test_time_over(self):
        """Tests the time_over() method."""
        self.assertFalse(time_over(self.pyboy))

    def test_level_finished(self):
        """Tests the level_finished() method."""
        self.assertFalse(level_finished(self.pyboy))

    def test_game_over(self):
        """Tests the game_over() method."""
        self.assertFalse(game_over(self.pyboy))


if __name__ == "__main__":
    unittest.main()
