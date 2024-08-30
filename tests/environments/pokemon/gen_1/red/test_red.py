import unittest

import numpy as np

import gymboy


class TestPokemonRed(unittest.TestCase):
    """Tests the PokemonRed class."""

    def setUp(self):
        self.env = gymboy.make(
            env_id="Pokemon-Red-v1",
            init_state_path="./tests/resources/states/pokemon/gen_1/red/pokemon_red_first_pokemon.state",
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
        np.testing.assert_allclose(2.195437800132936, self.env.get_reward())

    def test_get_obs(self):
        """Tests the get_obs() method."""
        obs = self.env.get_obs()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        num_envs = 3
        vectorized_env = gymboy.make_vec(
            env_id="Pokemon-Red-v1",
            num_envs=num_envs,
            vectorization_mode="sync",
            init_state_path="./tests/resources/states/pokemon/gen_1/red/pokemon_red_first_pokemon.state",
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

    def test_get_badges_reward(self):
        """Tests the get_badges_reward() method."""
        self.assertEqual(0, self.env.get_badges_reward())

    def test_get_money_reward(self):
        """Tests the get_money_reward() method."""
        np.testing.assert_allclose(0.003175003175003175, self.env.get_money_reward())

    def test_get_team_size_reward(self):
        """Tests the get_team_size_reward() method."""
        np.testing.assert_allclose(0.16666666666666666, self.env.get_team_size_reward())

    def test_get_levels_reward(self):
        """Tests the get_levels_reward() method."""
        np.testing.assert_allclose(0.01, self.env.get_levels_reward())

    def test_get_hps_reward(self):
        """Tests the get_hps_reward() method."""
        np.testing.assert_allclose(1.0, self.env.get_hps_reward())

    def test_get_pps_reward(self):
        """Tests the get_pps_reward() method."""
        np.testing.assert_allclose(1.0, self.env.get_pps_reward())

    def test_get_seen_pokemons_reward(self):
        """Tests the get_seen_pokemons_reward() method."""
        np.testing.assert_allclose(
            0.013245033112582781, self.env.get_seen_pokemons_reward()
        )

    def test_get_events_reward(self):
        """Tests the get_events_reward() method."""
        np.testing.assert_allclose(0.0023510971786833857, self.env.get_events_reward())


if __name__ == "__main__":
    unittest.main()
