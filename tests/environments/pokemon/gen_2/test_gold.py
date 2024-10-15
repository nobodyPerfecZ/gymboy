"""Tests pokemon/gen_2/gold.py."""

import unittest

import numpy as np

import gymboy


class TestPokemonGoldFlatten(unittest.TestCase):
    """Tests the PokemonGoldFlatten class."""

    def setUp(self):
        self.env_id = "Pokemon-Gold-flatten-v1"
        self.init_state_path = "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_1.state"
        self.num_envs = 3
        self.vectorization_mode = "sync"
        self.env = gymboy.make(
            env_id=self.env_id,
            init_state_path=self.init_state_path,
        )
        self.env.reset()

    def tearDown(self):
        self.env.close()

    def test_step(self):
        """Tests the step() method."""
        obs, reward, terminated, truncated, info = self.env.step(0)
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((426,), obs.shape)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(terminated, bool)
        self.assertIsInstance(truncated, bool)
        self.assertIsInstance(info, dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((426,), obs.shape)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(terminated, bool)
        self.assertIsInstance(truncated, bool)
        self.assertIsInstance(info, dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((426,), obs.shape)

    def test_get_obs(self):
        """Tests the get_obs() method."""
        obs = self.env.get_obs()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((426,), obs.shape)

    def test_get_reward(self):
        """Tests the get_reward() method."""
        np.testing.assert_allclose(0.4572158976541446, self.env.get_reward())

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        vectorized_env = gymboy.make_vec(
            env_id=self.env_id,
            num_envs=self.num_envs,
            vectorization_mode=self.vectorization_mode,
            init_state_path=self.init_state_path,
        )

        obs, info = vectorized_env.reset()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 426), obs.shape)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 426), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((self.num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((self.num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((self.num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [1] * self.num_envs
        )
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 426), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((self.num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((self.num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((self.num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        vectorized_env.close()


class TestPokemonGoldFullImage(unittest.TestCase):
    """Tests the PokemonGoldFullImage class."""

    def setUp(self):
        self.env_id = "Pokemon-Gold-full-image-v1"
        self.init_state_path = "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_1.state"
        self.num_envs = 3
        self.vectorization_mode = "sync"
        self.env = gymboy.make(
            env_id=self.env_id,
            init_state_path=self.init_state_path,
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

    def test_get_obs(self):
        """Tests the get_obs() method."""
        obs = self.env.get_obs()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((144, 160, 3), obs.shape)

    def test_get_reward(self):
        """Tests the get_reward() method."""
        np.testing.assert_allclose(0.4572158976541446, self.env.get_reward())

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        vectorized_env = gymboy.make_vec(
            env_id=self.env_id,
            num_envs=self.num_envs,
            vectorization_mode=self.vectorization_mode,
            init_state_path=self.init_state_path,
        )

        obs, info = vectorized_env.reset()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 144, 160, 3), obs.shape)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 144, 160, 3), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((self.num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((self.num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((self.num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [1] * self.num_envs
        )
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 144, 160, 3), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((self.num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((self.num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((self.num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        vectorized_env.close()


class TestPokemonGoldMinimalImage(unittest.TestCase):
    """Tests the PokemonGoldMinimalImage class."""

    def setUp(self):
        self.env_id = "Pokemon-Gold-minimal-image-v1"
        self.init_state_path = "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_1.state"
        self.num_envs = 3
        self.vectorization_mode = "sync"
        self.env = gymboy.make(
            env_id=self.env_id,
            init_state_path=self.init_state_path,
        )
        self.env.reset()

    def tearDown(self):
        self.env.close()

    def test_step(self):
        """Tests the step() method."""
        obs, reward, terminated, truncated, info = self.env.step(0)
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((18, 20), obs.shape)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(terminated, bool)
        self.assertIsInstance(truncated, bool)
        self.assertIsInstance(info, dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((18, 20), obs.shape)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(terminated, bool)
        self.assertIsInstance(truncated, bool)
        self.assertIsInstance(info, dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((18, 20), obs.shape)

    def test_get_obs(self):
        """Tests the get_obs() method."""
        obs = self.env.get_obs()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((18, 20), obs.shape)

    def test_get_reward(self):
        """Tests the get_reward() method."""
        np.testing.assert_allclose(0.4572158976541446, self.env.get_reward())

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        vectorized_env = gymboy.make_vec(
            env_id=self.env_id,
            num_envs=self.num_envs,
            vectorization_mode=self.vectorization_mode,
            init_state_path=self.init_state_path,
        )

        obs, info = vectorized_env.reset()
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 18, 20), obs.shape)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 18, 20), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((self.num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((self.num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((self.num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [1] * self.num_envs
        )
        self.assertIsInstance(obs, np.ndarray)
        self.assertEqual((self.num_envs, 18, 20), obs.shape)
        self.assertIsInstance(reward, np.ndarray)
        self.assertEqual((self.num_envs,), reward.shape)
        self.assertIsInstance(terminated, np.ndarray)
        self.assertEqual((self.num_envs,), terminated.shape)
        self.assertIsInstance(truncated, np.ndarray)
        self.assertEqual((self.num_envs,), truncated.shape)
        self.assertIsInstance(info, dict)

        vectorized_env.close()


if __name__ == "__main__":
    unittest.main()
