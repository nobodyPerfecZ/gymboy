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

    def test_score(self):
        """Tests the score() method."""
        self.assertEqual(7900, score(self.pyboy))

    def test_world_level(self):
        """Tests the world_level() method."""
        self.assertEqual((1, 1), world_level(self.pyboy))

    def test_coins(self):
        """Tests the coins() method."""
        self.assertEqual(35, coins(self.pyboy))

    def test_lives(self):
        """Tests the lives() method."""
        self.assertEqual(2, lives(self.pyboy))

    def test_time(self):
        """Tests the time() method."""
        self.assertEqual(264, time(self.pyboy))

    def test_time_over(self):
        """Tests the time_over() method."""
        self.assertFalse(time_over(self.pyboy))

    def test_level_finished(self):
        """Tests the level_finished() method."""
        self.assertFalse(level_finished(self.pyboy))

    def test_game_over(self):
        """Tests the game_over() method."""
        self.assertFalse(game_over(self.pyboy))

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            game_area(self.pyboy),
            np.array([
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300,   1,   0, 300, 300, 300, 300, 300, 300, 275, 289],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300,  17,  16, 300, 300, 300, 300, 300, 300, 292, 313],
                [300, 300, 300, 300, 300, 300, 300, 300, 239, 239, 239, 300, 300, 300, 300, 300, 300, 142, 143, 142],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 239, 239, 239, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 142, 143],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 275, 289],
                [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 292, 313],
                [142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143, 142, 143],
            ]),
        )


if __name__ == "__main__":
    unittest.main()
