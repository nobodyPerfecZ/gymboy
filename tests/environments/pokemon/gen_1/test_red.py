import unittest

import numpy as np

import gymboy


class TestPokemonRed(unittest.TestCase):
    """Tests the PokemonRed class."""

    def setUp(self):
        self.env = gymboy.make("Pokemon-Red-v1")

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

        np.testing.assert_allclose(0.003000003000003, reward)

    def test_get_obs(self):
        """Tests the get_obs() method."""
        self.env.reset()

        obs = self.env.get_obs()

        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        num_envs = 3
        vectorized_env = gymboy.make_vec("Pokemon-Red-v1", num_envs=num_envs)

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

    def test_get_badges(self):
        """Tests the get_badges() method."""
        self.env.reset()

        badges = self.env.get_badges()

        self.assertEqual(0, badges)

    def test_get_max_badges(self):
        """Tests the get_max_badges() method."""
        self.env.reset()

        max_badges = self.env.get_max_badges()

        self.assertEqual(8, max_badges)

    def test_get_badges_reward(self):
        """Tests the get_badges_reward() method."""
        self.env.reset()

        badges_reward = self.env.get_badges_reward()

        self.assertEqual(0, badges_reward)

    def test_get_money(self):
        """Tests the get_money() method."""
        self.env.reset()

        money = self.env.get_money()

        self.assertEqual(3000, money)

    def test_get_max_money(self):
        """Tests the get_max_money() method."""
        self.env.reset()

        max_money = self.env.get_max_money()

        self.assertEqual(999999, max_money)

    def test_get_money_reward(self):
        """Tests the get_money_reward() method."""
        self.env.reset()

        money_reward = self.env.get_money_reward()

        np.testing.assert_allclose(0.003000003000003, money_reward)

    def test_get_team_size(self):
        """Tests the get_team_size() method."""
        self.env.reset()

        team_size = self.env.get_team_size()

        self.assertEqual(0, team_size)

    def test_get_max_team_size(self):
        """Tests the get_max_team_size() method."""
        self.env.reset()

        max_team_size = self.env.get_max_team_size()

        self.assertEqual(6, max_team_size)

    def test_get_team_size_reward(self):
        """Tests the get_team_size_reward() method."""
        self.env.reset()

        team_size_reward = self.env.get_team_size_reward()

        self.assertEqual(0, team_size_reward)

    def test_get_levels(self):
        """Tests the get_levels() method."""
        self.env.reset()

        levels = self.env.get_levels()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], levels)

    def test_get_max_levels(self):
        """Tests the get_max_levels() method."""
        self.env.reset()

        max_levels = self.env.get_max_levels()

        np.testing.assert_allclose([100, 100, 100, 100, 100, 100], max_levels)

    def test_get_levels_reward(self):
        """Tests the get_levels_reward() method."""
        self.env.reset()

        levels_reward = self.env.get_levels_reward()

        self.assertEqual(0, levels_reward)

    def test_get_hps(self):
        """Tests the get_hps() method."""
        self.env.reset()

        hps = self.env.get_hps()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], hps)

    def test_get_max_hps(self):
        """Tests the get_max_hps() method."""
        self.env.reset()

        max_hps = self.env.get_max_hps()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], max_hps)

    def test_get_hps_reward(self):
        """Tests the get_hps_reward() method."""
        self.env.reset()

        hps_reward = self.env.get_hps_reward()

        self.assertEqual(0, hps_reward)

    def test_get_exps(self):
        """Tests the get_exps() method."""
        self.env.reset()

        exps = self.env.get_exps()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], exps)

    def test_get_moves(self):
        """Tests the get_moves() method."""
        self.env.reset()

        moves = self.env.get_moves()

        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            moves,
        )

    def test_get_pps(self):
        """Tests the get_pps() method."""
        self.env.reset()

        pps = self.env.get_pps()

        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            pps,
        )

    def test_get_pps_reward(self):
        """Tests the get_pps_reward() method."""
        self.env.reset()

        pps_reward = self.env.get_pps_reward()

        self.assertEqual(0, pps_reward)

    def test_get_seen_pokemons(self):
        """Tests the get_seen_pokemons() method."""
        self.env.reset()

        seen_pokemons = self.env.get_seen_pokemons()

        self.assertEqual(0, seen_pokemons)

    def test_get_max_seen_pokemons(self):
        """Tests the get_max_seen_pokemons() method."""
        self.env.reset()

        max_seen_pokemons = self.env.get_max_seen_pokemons()

        self.assertEqual(151, max_seen_pokemons)

    def test_get_seen_pokemons_reward(self):
        """Tests the get_seen_pokemons_reward() method."""
        self.env.reset()

        seen_pokemons_reward = self.env.get_seen_pokemons_reward()

        self.assertEqual(0, seen_pokemons_reward)

    def test_get_events(self):
        """Tests the get_events() method."""
        self.env.reset()

        events = self.env.get_events()

        self.assertEqual(0, events)

    def test_get_max_events(self):
        """Tests the get_max_events() method."""
        self.env.reset()

        max_events = self.env.get_max_events()

        self.assertEqual(2552, max_events)

    def test_get_events_reward(self):
        """Tests the get_events_reward() method."""
        self.env.reset()

        events_reward = self.env.get_events_reward()

        self.assertEqual(0, events_reward)


if __name__ == "__main__":
    unittest.main()
