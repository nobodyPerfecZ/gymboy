"""Tests tetris/tetris/tetris.py."""

from typing import Dict

import numpy as np

import gymboy


class TestTetrisFullImage:
    """Tests the TetrisFullImage class."""

    env_id = "Tetris-full-image-v1"
    rom_path = "./resources/roms/tetris/tetris/tetris.gb"
    init_state_path = "./resources/tests/tetris/tetris/tetris_lvl_5.state"
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
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (144, 160, 3)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (144, 160, 3)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (144, 160, 3)

    def test_observation(self):
        """Tests the observation() method."""
        obs = self.env.observation()
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (144, 160, 3)

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
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["next_block"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 144, 160, 3)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["next_block"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 144, 160, 3)
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
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["next_block"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 144, 160, 3)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, Dict)

        vectorized_env.close()


class TestTetrisMinimalImage:
    """Tests the TetrisMinimalImage class."""

    env_id = "Tetris-minimal-image-v1"
    rom_path = "./resources/roms/tetris/tetris/tetris.gb"
    init_state_path = "./resources/tests/tetris/tetris/tetris_lvl_5.state"
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
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (18, 10)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (18, 10)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, Dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (18, 10)

    def test_observation(self):
        """Tests the observation() method."""
        obs = self.env.observation()
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (1,)
        assert obs["next_block"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["img"].shape == (18, 10)

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
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["next_block"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 18, 10)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        assert isinstance(obs, Dict)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["next_block"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 18, 10)
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
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["next_block"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 18, 10)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, Dict)

        vectorized_env.close()
