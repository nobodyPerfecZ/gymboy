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

        np.testing.assert_allclose(1.0517383917383918, reward)

    def test_get_obs(self):
        """Tests the get_obs() method."""
        self.env.reset()

        obs = self.env.get_obs()

        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        num_envs = 3
        vectorized_env = gymboy.make_vec(
            env_id="Super-Mario-Land-1-v1",
            num_envs=num_envs,
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

        vectorized_env.close()

    def test_get_world_level(self):
        """Tests the get_world_level() method."""
        self.env.reset()

        world_level = self.env.get_world_level()

        self.assertEqual((1, 1), world_level)

    def test_get_score(self):
        """Tests the get_score() method."""
        self.env.reset()

        score = self.env.get_score()

        self.assertEqual(7900, score)

    def test_get_max_score(self):
        """Tests the get_max_score() method."""
        self.env.reset()

        score = self.env.get_max_score()

        self.assertEqual(999999, score)

    def test_get_score_reward(self):
        """Tests the get_score_reward() method."""
        self.env.reset()

        score_reward = self.env.get_score_reward()

        np.testing.assert_allclose(0.0079000079000079, score_reward)

    def test_get_coins(self):
        """Tests the get_coins() method."""
        self.env.reset()

        coins = self.env.get_coins()

        self.assertEqual(35, coins)

    def test_get_max_coins(self):
        """Tests the get_max_coins() method."""
        self.env.reset()

        max_coins = self.env.get_max_coins()

        self.assertEqual(99, max_coins)

    def test_get_coins_reward(self):
        """Tests the get_coins_reward() method."""
        self.env.reset()

        coins_reward = self.env.get_coins_reward()

        np.testing.assert_allclose(0.35353535353535354, coins_reward)

    def test_get_lives_left(self):
        """Tests the get_lives_left() method."""
        self.env.reset()

        lives_left = self.env.get_lives_left()

        self.assertEqual(3, lives_left)

    def test_get_max_lives_left(self):
        """Tests the get_max_lives_left() method."""
        self.env.reset()

        max_lives_left = self.env.get_max_lives_left()

        self.assertEqual(99, max_lives_left)

    def test_get_lives_left_reward(self):
        """Tests the get_lives_left_reward() method."""
        self.env.reset()

        lives_left_reward = self.env.get_lives_left_reward()

        np.testing.assert_allclose(0.030303030303030304, lives_left_reward)

    def test_get_time_left(self):
        """Tests the get_time_left() method."""
        self.env.reset()

        time_left = self.env.get_time_left()

        self.assertEqual(264, time_left)

    def test_get_max_time_left(self):
        """Tests the get_max_time_left() method."""
        self.env.reset()

        max_time_left = self.env.get_max_time_left()

        self.assertEqual(400, max_time_left)

    def test_get_time_left_reward(self):
        """Tests the get_time_left_reward() method."""
        self.env.reset()

        time_left_reward = self.env.get_time_left_reward()

        np.testing.assert_allclose(0.66, time_left_reward)

    def test_game_over(self):
        """Tests the game_over() method."""
        self.env.reset()

        game_over = self.env.game_over()

        self.assertFalse(game_over)

    def test_game_over_reward(self):
        """Tests the game_over_reward() method."""
        self.env.reset()

        game_over_reward = self.env.game_over_reward()

        self.assertEqual(0, game_over_reward)

    def test_game_finished(self):
        """Tests the game_finished() method."""
        self.env.reset()

        game_finished = self.env.game_finished()

        self.assertFalse(game_finished)

    def test_game_finished_reward(self):
        """Tests the game_finished_reward() method."""
        self.env.reset()

        game_finished_reward = self.env.game_finished_reward()

        self.assertEqual(0, game_finished_reward)


if __name__ == "__main__":
    unittest.main()
