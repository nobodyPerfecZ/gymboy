import unittest

import numpy as np

import gymboy


class TestSuperMarioLand(unittest.TestCase):
    """Tests the SuperMarioLand class."""

    def setUp(self):
        self.env1 = gymboy.make("Super-Mario-Land-1-v1", render_mode=None)
        self.env2 = gymboy.make("Super-Mario-Land-1-v1", render_mode="human")
        self.env3 = gymboy.make("Super-Mario-Land-1-v1", render_mode="rgb_array")

    def tearDown(self):
        self.env1.close()
        self.env2.close()
        self.env3.close()

    def test_step(self):
        """Tests the step() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        obs1, reward1, terminated1, truncated1, info1 = self.env1.step(0)
        obs2, reward2, terminated2, truncated2, info2 = self.env2.step(0)
        obs3, reward3, terminated3, truncated3, info3 = self.env3.step(0)

        self.assertIsInstance(obs1, np.ndarray)
        self.assertEqual((144, 160, 3), obs1.shape)
        self.assertIsInstance(reward1, float)
        self.assertIsInstance(terminated1, bool)
        self.assertIsInstance(truncated1, bool)
        self.assertIsInstance(info1, dict)

        self.assertIsInstance(obs2, np.ndarray)
        self.assertEqual((144, 160, 3), obs2.shape)
        self.assertIsInstance(reward2, float)
        self.assertIsInstance(terminated2, bool)
        self.assertIsInstance(truncated2, bool)
        self.assertIsInstance(info2, dict)

        self.assertIsInstance(obs3, np.ndarray)
        self.assertEqual((144, 160, 3), obs3.shape)
        self.assertIsInstance(reward3, float)
        self.assertIsInstance(terminated3, bool)
        self.assertIsInstance(truncated3, bool)
        self.assertIsInstance(info3, dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs1, _ = self.env1.reset()
        obs2, _ = self.env2.reset()
        obs3, _ = self.env3.reset()

        self.assertIsInstance(obs1, np.ndarray)
        self.assertEqual((144, 160, 3), obs1.shape)

        self.assertIsInstance(obs2, np.ndarray)
        self.assertEqual((144, 160, 3), obs1.shape)

        self.assertIsInstance(obs3, np.ndarray)
        self.assertEqual((144, 160, 3), obs1.shape)

    def test_render(self):
        """Tests the render() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        obs1 = self.env1.render()
        obs2 = self.env2.render()
        obs3 = self.env3.render()

        self.assertIsNone(obs1)

        self.assertIsInstance(obs2, np.ndarray)
        self.assertEqual((144, 160, 3), obs2.shape)

        self.assertIsInstance(obs3, np.ndarray)
        self.assertEqual((144, 160, 3), obs3.shape)

    def test_get_reward(self):
        """Tests the get_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        reward1 = self.env1.get_reward()
        reward2 = self.env2.get_reward()
        reward3 = self.env3.get_reward()

        np.testing.assert_allclose(1.0253030303030304, reward1)
        np.testing.assert_allclose(1.0253030303030304, reward2)
        np.testing.assert_allclose(1.0253030303030304, reward3)

    def test_get_obs(self):
        """Tests the get_obs() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        obs1 = self.env1.get_obs()
        obs2 = self.env2.get_obs()
        obs3 = self.env3.get_obs()

        self.assertIsInstance(obs1, np.ndarray)
        self.assertEqual((144, 160, 3), obs1.shape)

        self.assertIsInstance(obs2, np.ndarray)
        self.assertEqual((144, 160, 3), obs1.shape)

        self.assertIsInstance(obs3, np.ndarray)
        self.assertEqual((144, 160, 3), obs1.shape)

    def test_get_world_level(self):
        """Tests the get_world_level() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        world_level1 = self.env1.get_world_level()
        world_level2 = self.env2.get_world_level()
        world_level3 = self.env3.get_world_level()

        self.assertEqual((1, 1), world_level1)
        self.assertEqual((1, 1), world_level2)
        self.assertEqual((1, 1), world_level3)

    def test_get_score(self):
        """Tests the get_score() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        score1 = self.env1.get_score()
        score2 = self.env2.get_score()
        score3 = self.env3.get_score()

        self.assertEqual(0, score1)
        self.assertEqual(0, score2)
        self.assertEqual(0, score3)

    def test_get_max_score(self):
        """Tests the get_max_score() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        score1 = self.env1.get_max_score()
        score2 = self.env2.get_max_score()
        score3 = self.env3.get_max_score()

        self.assertEqual(999999, score1)
        self.assertEqual(999999, score2)
        self.assertEqual(999999, score3)

    def test_get_score_reward(self):
        """Tests the get_score_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        score_reward1 = self.env1.get_score_reward()
        score_reward2 = self.env2.get_score_reward()
        score_reward3 = self.env3.get_score_reward()

        self.assertEqual(0, score_reward1)
        self.assertEqual(0, score_reward2)
        self.assertEqual(0, score_reward3)

    def test_get_coins(self):
        """Tests the get_coins() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        coins1 = self.env1.get_coins()
        coins2 = self.env2.get_coins()
        coins3 = self.env3.get_coins()

        self.assertEqual(0, coins1)
        self.assertEqual(0, coins2)
        self.assertEqual(0, coins3)

    def test_get_max_coins(self):
        """Tests the get_max_coins() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_coins1 = self.env1.get_max_coins()
        max_coins2 = self.env2.get_max_coins()
        max_coins3 = self.env3.get_max_coins()

        self.assertEqual(99, max_coins1)
        self.assertEqual(99, max_coins2)
        self.assertEqual(99, max_coins3)

    def test_get_coins_reward(self):
        """Tests the get_coins_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        coins_reward1 = self.env1.get_coins_reward()
        coins_reward2 = self.env2.get_coins_reward()
        coins_reward3 = self.env3.get_coins_reward()

        self.assertEqual(0, coins_reward1)
        self.assertEqual(0, coins_reward2)
        self.assertEqual(0, coins_reward3)

    def test_get_lives_left(self):
        """Tests the get_lives_left() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        lives_left1 = self.env1.get_lives_left()
        lives_left2 = self.env2.get_lives_left()
        lives_left3 = self.env3.get_lives_left()

        self.assertEqual(3, lives_left1)
        self.assertEqual(3, lives_left2)
        self.assertEqual(3, lives_left3)

    def test_get_max_lives_left(self):
        """Tests the get_max_lives_left() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_lives_left1 = self.env1.get_max_lives_left()
        max_lives_left2 = self.env2.get_max_lives_left()
        max_lives_left3 = self.env3.get_max_lives_left()

        self.assertEqual(99, max_lives_left1)
        self.assertEqual(99, max_lives_left2)
        self.assertEqual(99, max_lives_left3)

    def test_get_lives_left_reward(self):
        """Tests the get_lives_left_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        lives_left_reward1 = self.env1.get_lives_left_reward()
        lives_left_reward2 = self.env2.get_lives_left_reward()
        lives_left_reward3 = self.env3.get_lives_left_reward()

        np.testing.assert_allclose(0.030303030303030304, lives_left_reward1)
        np.testing.assert_allclose(0.030303030303030304, lives_left_reward2)
        np.testing.assert_allclose(0.030303030303030304, lives_left_reward3)

    def test_get_time_left(self):
        """Tests the get_time_left() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        time_left1 = self.env1.get_time_left()
        time_left2 = self.env2.get_time_left()
        time_left3 = self.env3.get_time_left()

        self.assertEqual(398, time_left1)
        self.assertEqual(398, time_left2)
        self.assertEqual(398, time_left3)

    def test_get_max_time_left(self):
        """Tests the get_max_time_left() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_time_left1 = self.env1.get_max_time_left()
        max_time_left2 = self.env2.get_max_time_left()
        max_time_left3 = self.env3.get_max_time_left()

        self.assertEqual(400, max_time_left1)
        self.assertEqual(400, max_time_left2)
        self.assertEqual(400, max_time_left3)

    def test_get_time_left_reward(self):
        """Tests the get_time_left_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        time_left_reward1 = self.env1.get_time_left_reward()
        time_left_reward2 = self.env2.get_time_left_reward()
        time_left_reward3 = self.env3.get_time_left_reward()

        np.testing.assert_allclose(0.995, time_left_reward1)
        np.testing.assert_allclose(0.995, time_left_reward2)
        np.testing.assert_allclose(0.995, time_left_reward3)

    def test_game_over(self):
        """Tests the game_over() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        game_over1 = self.env1.game_over()
        game_over2 = self.env2.game_over()
        game_over3 = self.env3.game_over()

        self.assertFalse(game_over1)
        self.assertFalse(game_over2)
        self.assertFalse(game_over3)

    def test_game_over_reward(self):
        """Tests the game_over_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        game_over_reward1 = self.env1.game_over_reward()
        game_over_reward2 = self.env2.game_over_reward()
        game_over_reward3 = self.env3.game_over_reward()

        self.assertEqual(0, game_over_reward1)
        self.assertEqual(0, game_over_reward2)
        self.assertEqual(0, game_over_reward3)

    def test_game_finished(self):
        """Tests the game_finished() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        game_finished1 = self.env1.game_finished()
        game_finished2 = self.env2.game_finished()
        game_finished3 = self.env3.game_finished()

        self.assertFalse(game_finished1)
        self.assertFalse(game_finished2)
        self.assertFalse(game_finished3)
    
    def test_game_finished_reward(self):
        """Tests the game_finished_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        game_finished_reward1 = self.env1.game_finished_reward()
        game_finished_reward2 = self.env2.game_finished_reward()
        game_finished_reward3 = self.env3.game_finished_reward()

        self.assertEqual(0, game_finished_reward1)
        self.assertEqual(0, game_finished_reward2)
        self.assertEqual(0, game_finished_reward3)


if __name__ == "__main__":
    unittest.main()
