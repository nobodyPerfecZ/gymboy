import unittest

import numpy as np

import gymboy


class TestSuperMarioLand2(unittest.TestCase):
    """Tests the SuperMarioLand2 class."""

    def setUp(self):
        self.env = gymboy.make("Super-Mario-Land-2-v1")

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

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        vectorized_env = gymboy.make_vec("Super-Mario-Land-2-v1", num_envs=10)

        obs, info = vectorized_env.reset()

        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((10, 144, 160, 3), obs.shape)

        obs, reward, terminated, truncated, info = vectorized_env.step([0] * 10)

        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((10, 144, 160, 3), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((10,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((10,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((10,), truncated.shape)
        self.assertIsInstance(info, dict)

        vectorized_env.close()


if __name__ == "__main__":
    unittest.main()
