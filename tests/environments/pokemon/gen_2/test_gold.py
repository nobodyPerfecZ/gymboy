import unittest

import numpy as np

import gymboy


class TestPokemonGold(unittest.TestCase):
    """Tests the PokemonGold class."""

    def setUp(self):
        self.env = gymboy.make("Pokemon-Gold-v1")

    def tearDown(self):
        self.env.close()

    def test_step(self):
        """Tests the step() method."""
        self.env.reset()

        obs, reward, terminated, truncated, info = self.env.step(0)

        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(terminated, bool)
        self.assertIsInstance(truncated, bool)
        self.assertIsInstance(info, dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()

        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)

    def test_get_reward(self):
        """Tests the get_reward() method."""
        self.env.reset()

        reward = self.env.get_reward()

        np.testing.assert_allclose(1.0, reward)

    def test_get_obs(self):
        """Tests the get_obs() method."""
        self.env.reset()

        obs = self.env.get_obs()

        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)


if __name__ == "__main__":
    unittest.main()
