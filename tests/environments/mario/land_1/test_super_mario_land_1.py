import unittest

import numpy as np

import gymboy


class TestSuperMarioLand(unittest.TestCase):
    """Tests the SuperMarioLand class."""

    def setUp(self):
        self.env = gymboy.make(
            env_id="Super-Mario-Land-1-v1",
            init_state_path="./tests/resources/states/mario/land_1/super_mario_land_1_1_1_end.state",
        )
        self.env.reset()

    def tearDown(self):
        self.env.close()

    def test_step(self):
        """Tests the step() method."""
        obs, reward, terminated, truncated, info = self.env.step(0)
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(terminated, bool)
        self.assertIsInstance(truncated, bool)
        self.assertIsInstance(info, dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
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
        np.testing.assert_allclose(1.0416373816373816, self.env.get_reward())

    def test_get_obs(self):
        """Tests the get_obs() method."""
        obs = self.env.get_obs()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        num_envs = 3
        vectorized_env = gymboy.make_vec(
            env_id="Super-Mario-Land-1-v1",
            num_envs=num_envs,
            vectorization_mode="sync",
            init_state_path="./tests/resources/states/mario/land_1/super_mario_land_1_1_1_end.state",
        )

        obs, info = vectorized_env.reset()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((num_envs, 144, 160, 3), obs.shape)

        obs, reward, terminated, truncated, info = vectorized_env.step([0] * num_envs)
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((num_envs, 144, 160, 3), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        obs, reward, terminated, truncated, info = vectorized_env.step([1] * num_envs)
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((num_envs, 144, 160, 3), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        vectorized_env.close()

    def test_get_score_reward(self):
        """Tests the get_score_reward() method."""
        np.testing.assert_allclose(0.0079000079000079, self.env.get_score_reward())

    def test_get_coins_reward(self):
        """Tests the get_coins_reward() method."""
        np.testing.assert_allclose(0.35353535353535354, self.env.get_coins_reward())

    def test_get_lives_reward(self):
        """Tests the get_lives_reward() method."""
        np.testing.assert_allclose(0.020202020202020204, self.env.get_lives_reward())

    def test_get_time_reward(self):
        """Tests the get_time_reward() method."""
        np.testing.assert_allclose(0.66, self.env.get_time_reward())

    def test_time_over_reward(self):
        """Tests the time_over_reward() method."""
        self.assertEqual(0.0, self.env.time_over_reward())

    def test_level_finished_reward(self):
        """Tests the level_finished_reward() method."""
        self.assertEqual(0.0, self.env.level_finished_reward())

    def test_game_over_reward(self):
        """Tests the game_over_reward() method."""
        self.assertEqual(0, self.env.game_over_reward())


if __name__ == "__main__":
    unittest.main()
