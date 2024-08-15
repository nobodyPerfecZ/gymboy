import unittest

import numpy as np

import gymboy


class TestPokemonYellow(unittest.TestCase):
    """Tests the PokemonYellow class."""

    def setUp(self):
        self.env1 = gymboy.make("Pokemon-Yellow-v1", render_mode=None)
        self.env2 = gymboy.make("Pokemon-Yellow-v1", render_mode="human")
        self.env3 = gymboy.make("Pokemon-Yellow-v1", render_mode="rgb_array")

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

        np.testing.assert_allclose(0.003000003000003, reward1)
        np.testing.assert_allclose(0.003000003000003, reward2)
        np.testing.assert_allclose(0.003000003000003, reward3)

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

    def test_get_badges(self):
        """Tests the get_badges() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        badges1 = self.env1.get_badges()
        badges2 = self.env2.get_badges()
        badges3 = self.env3.get_badges()

        self.assertEqual(0, badges1)
        self.assertEqual(0, badges2)
        self.assertEqual(0, badges3)

    def test_get_max_badges(self):
        """Tests the get_max_badges() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_badges1 = self.env1.get_max_badges()
        max_badges2 = self.env2.get_max_badges()
        max_badges3 = self.env3.get_max_badges()

        self.assertEqual(8, max_badges1)
        self.assertEqual(8, max_badges2)
        self.assertEqual(8, max_badges3)

    def test_get_badges_reward(self):
        """Tests the get_badges_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        badges_reward1 = self.env1.get_badges_reward()
        badges_reward2 = self.env2.get_badges_reward()
        badges_reward3 = self.env3.get_badges_reward()

        self.assertEqual(0, badges_reward1)
        self.assertEqual(0, badges_reward2)
        self.assertEqual(0, badges_reward3)

    def test_get_money(self):
        """Tests the get_money() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        money1 = self.env1.get_money()
        money2 = self.env2.get_money()
        money3 = self.env3.get_money()

        self.assertEqual(3000, money1)
        self.assertEqual(3000, money2)
        self.assertEqual(3000, money3)

    def test_get_max_money(self):
        """Tests the get_max_money() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_money1 = self.env1.get_max_money()
        max_money2 = self.env2.get_max_money()
        max_money3 = self.env3.get_max_money()

        self.assertEqual(999999, max_money1)
        self.assertEqual(999999, max_money2)
        self.assertEqual(999999, max_money3)

    def test_get_money_reward(self):
        """Tests the get_money_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        money_reward1 = self.env1.get_money_reward()
        money_reward2 = self.env2.get_money_reward()
        money_reward3 = self.env3.get_money_reward()

        np.testing.assert_allclose(0.003000003000003, money_reward1)
        np.testing.assert_allclose(0.003000003000003, money_reward2)
        np.testing.assert_allclose(0.003000003000003, money_reward3)

    def test_get_team_size(self):
        """Tests the get_team_size() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        team_size1 = self.env1.get_team_size()
        team_size2 = self.env2.get_team_size()
        team_size3 = self.env3.get_team_size()

        self.assertEqual(0, team_size1)
        self.assertEqual(0, team_size2)
        self.assertEqual(0, team_size3)

    def test_get_max_team_size(self):
        """Tests the get_max_team_size() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_team_size1 = self.env1.get_max_team_size()
        max_team_size2 = self.env2.get_max_team_size()
        max_team_size3 = self.env3.get_max_team_size()

        self.assertEqual(6, max_team_size1)
        self.assertEqual(6, max_team_size2)
        self.assertEqual(6, max_team_size3)

    def test_get_team_size_reward(self):
        """Tests the get_team_size_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        team_size_reward1 = self.env1.get_team_size_reward()
        team_size_reward2 = self.env2.get_team_size_reward()
        team_size_reward3 = self.env3.get_team_size_reward()

        self.assertEqual(0, team_size_reward1)
        self.assertEqual(0, team_size_reward2)
        self.assertEqual(0, team_size_reward3)

    def test_get_levels(self):
        """Tests the get_levels() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        levels1 = self.env1.get_levels()
        levels2 = self.env2.get_levels()
        levels3 = self.env3.get_levels()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], levels1)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], levels2)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], levels3)

    def test_get_max_levels(self):
        """Tests the get_max_levels() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_levels1 = self.env1.get_max_levels()
        max_levels2 = self.env2.get_max_levels()
        max_levels3 = self.env3.get_max_levels()

        np.testing.assert_allclose([100, 100, 100, 100, 100, 100], max_levels1)
        np.testing.assert_allclose([100, 100, 100, 100, 100, 100], max_levels2)
        np.testing.assert_allclose([100, 100, 100, 100, 100, 100], max_levels3)

    def test_get_levels_reward(self):
        """Tests the get_levels_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        levels_reward1 = self.env1.get_levels_reward()
        levels_reward2 = self.env2.get_levels_reward()
        levels_reward3 = self.env3.get_levels_reward()

        self.assertEqual(0, levels_reward1)
        self.assertEqual(0, levels_reward2)
        self.assertEqual(0, levels_reward3)

    def test_get_hps(self):
        """Tests the get_hps() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        hps1 = self.env1.get_hps()
        hps2 = self.env2.get_hps()
        hps3 = self.env3.get_hps()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], hps1)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], hps2)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], hps3)

    def test_get_max_hps(self):
        """Tests the get_max_hps() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_hps1 = self.env1.get_max_hps()
        max_hps2 = self.env2.get_max_hps()
        max_hps3 = self.env3.get_max_hps()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], max_hps1)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], max_hps2)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], max_hps3)

    def test_get_hps_reward(self):
        """Tests the get_hps_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        hps_reward1 = self.env1.get_hps_reward()
        hps_reward2 = self.env2.get_hps_reward()
        hps_reward3 = self.env3.get_hps_reward()

        self.assertEqual(0, hps_reward1)
        self.assertEqual(0, hps_reward2)
        self.assertEqual(0, hps_reward3)

    def test_get_exps(self):
        """Tests the get_exps() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        exps1 = self.env1.get_exps()
        exps2 = self.env2.get_exps()
        exps3 = self.env3.get_exps()

        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], exps1)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], exps2)
        np.testing.assert_allclose([0, 0, 0, 0, 0, 0], exps3)

    def test_get_moves(self):
        """Tests the get_moves() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        moves1 = self.env1.get_moves()
        moves2 = self.env2.get_moves()
        moves3 = self.env3.get_moves()

        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            moves1,
        )
        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            moves2,
        )
        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            moves3,
        )

    def test_get_pps(self):
        """Tests the get_pps() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        pps1 = self.env1.get_pps()
        pps2 = self.env2.get_pps()
        pps3 = self.env3.get_pps()

        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            pps1,
        )
        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            pps2,
        )
        np.testing.assert_allclose(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            pps3,
        )

    def test_get_pps_reward(self):
        """Tests the get_pps_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        pps_reward1 = self.env1.get_pps_reward()
        pps_reward2 = self.env2.get_pps_reward()
        pps_reward3 = self.env3.get_pps_reward()

        self.assertEqual(0, pps_reward1)
        self.assertEqual(0, pps_reward2)
        self.assertEqual(0, pps_reward3)

    def test_get_seen_pokemons(self):
        """Tests the get_seen_pokemons() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        seen_pokemons1 = self.env1.get_seen_pokemons()
        seen_pokemons2 = self.env2.get_seen_pokemons()
        seen_pokemons3 = self.env3.get_seen_pokemons()

        self.assertEqual(0, seen_pokemons1)
        self.assertEqual(0, seen_pokemons2)
        self.assertEqual(0, seen_pokemons3)

    def test_get_max_seen_pokemons(self):
        """Tests the get_max_seen_pokemons() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_seen_pokemons1 = self.env1.get_max_seen_pokemons()
        max_seen_pokemons2 = self.env2.get_max_seen_pokemons()
        max_seen_pokemons3 = self.env3.get_max_seen_pokemons()

        self.assertEqual(151, max_seen_pokemons1)
        self.assertEqual(151, max_seen_pokemons2)
        self.assertEqual(151, max_seen_pokemons3)

    def test_get_seen_pokemons_reward(self):
        """Tests the get_seen_pokemons_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        seen_pokemons_reward1 = self.env1.get_seen_pokemons_reward()
        seen_pokemons_reward2 = self.env2.get_seen_pokemons_reward()
        seen_pokemons_reward3 = self.env3.get_seen_pokemons_reward()

        self.assertEqual(0, seen_pokemons_reward1)
        self.assertEqual(0, seen_pokemons_reward2)
        self.assertEqual(0, seen_pokemons_reward3)

    def test_get_events(self):
        """Tests the get_events() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        events1 = self.env1.get_events()
        events2 = self.env2.get_events()
        events3 = self.env3.get_events()

        self.assertEqual(0, events1)
        self.assertEqual(0, events2)
        self.assertEqual(0, events3)

    def test_get_max_events(self):
        """Tests the get_max_events() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        max_events1 = self.env1.get_max_events()
        max_events2 = self.env2.get_max_events()
        max_events3 = self.env3.get_max_events()

        self.assertEqual(2552, max_events1)
        self.assertEqual(2552, max_events2)
        self.assertEqual(2552, max_events3)

    def test_get_events_reward(self):
        """Tests the get_events_reward() method."""
        self.env1.reset()
        self.env2.reset()
        self.env3.reset()

        events_reward1 = self.env1.get_events_reward()
        events_reward2 = self.env2.get_events_reward()
        events_reward3 = self.env3.get_events_reward()

        self.assertEqual(0, events_reward1)
        self.assertEqual(0, events_reward2)
        self.assertEqual(0, events_reward3)


if __name__ == "__main__":
    unittest.main()
