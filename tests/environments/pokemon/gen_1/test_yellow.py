"""Tests pokemon/gen_1/yellow.py."""

from typing import Dict

import numpy as np

import gymboy


class TestPokemonYellowFullImage:
    """Tests the PokemonYellowFullImage class."""

    env_id = "Pokemon-Yellow-full-image-v1"
    rom_path = "./resources/roms/pokemon/gen_1/pokemon_yellow.gbc"
    init_state_path = (
        "./resources/tests/pokemon/gen_1/pokemon_yellow_after_first_pokemon.state"
    )
    num_envs = 3
    vectorization_mode = "sync"

    @classmethod
    def setup_class(cls):
        cls.env = gymboy.make(
            env_id=cls.env_id,
            rom_path=cls.rom_path,
            init_state_path=cls.init_state_path,
        )
        cls.env.reset()

    @classmethod
    def teardown_class(cls):
        cls.env.close()

    def test_step(self):
        """Tests the step() method."""
        obs, reward, terminated, truncated, info = self.env.step(0)
        assert isinstance(obs, Dict)

        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        assert isinstance(obs, Dict)

        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        assert isinstance(obs, Dict)

    def test_observation(self):
        """Tests the observation() method."""
        obs = self.env.observation()
        assert isinstance(obs, Dict)

    def test_reward(self):
        """Tests the reward() method."""
        assert isinstance(self.env.reward(), float)

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        vectorized_env = gymboy.make_vec(
            env_id=self.env_id,
            num_envs=self.num_envs,
            vectorization_mode=self.vectorization_mode,
            rom_path=self.rom_path,
            init_state_path=self.init_state_path,
        )

        obs, info = vectorized_env.reset()
        assert isinstance(obs, Dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        assert isinstance(obs, Dict)

        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, Dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [1] * self.num_envs
        )
        assert isinstance(obs, Dict)

        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, Dict)

        vectorized_env.close()


class TestPokemonYellowMinimalImage:
    """Tests the PokemonYellowMinimalImage class."""

    env_id = "Pokemon-Yellow-minimal-image-v1"
    rom_path = "./resources/roms/pokemon/gen_1/pokemon_yellow.gbc"
    init_state_path = (
        "./resources/tests/pokemon/gen_1/pokemon_yellow_after_first_pokemon.state"
    )
    num_envs = 3
    vectorization_mode = "sync"

    @classmethod
    def setup_class(cls):
        cls.env = gymboy.make(
            env_id=cls.env_id,
            rom_path=cls.rom_path,
            init_state_path=cls.init_state_path,
        )
        cls.env.reset()

    @classmethod
    def teardown_class(cls):
        cls.env.close()

    def test_step(self):
        """Tests the step() method."""
        obs, reward, terminated, truncated, info = self.env.step(0)
        assert isinstance(obs, Dict)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        assert isinstance(obs, Dict)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        assert isinstance(obs, Dict)

    def test_observation(self):
        """Tests the observation() method."""
        obs = self.env.observation()
        assert isinstance(obs, Dict)

    def test_reward(self):
        """Tests the reward() method."""
        assert isinstance(self.env.reward(), float)

    def test_vectorized_env(self):
        """Tests the vectorized environment."""
        vectorized_env = gymboy.make_vec(
            env_id=self.env_id,
            num_envs=self.num_envs,
            vectorization_mode=self.vectorization_mode,
            rom_path=self.rom_path,
            init_state_path=self.init_state_path,
        )

        obs, info = vectorized_env.reset()
        assert isinstance(obs, Dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        assert isinstance(obs, Dict)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, Dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [1] * self.num_envs
        )
        assert isinstance(obs, Dict)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, Dict)

        vectorized_env.close()
