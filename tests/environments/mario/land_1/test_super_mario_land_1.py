"""Tests mario/land_1/super_mario_land_1.py."""

import numpy as np

import gymboy


class TestSuperMarioLand1FullImage:
    """Tests the SuperMarioLand1FullImage class."""

    env_id = "Super-Mario-Land-1-full-image-v1"
    rom_path = "./resources/roms/mario/land_1/super_mario_land_1.gb"
    init_state_path = "./resources/tests/mario/land_1/super_mario_land_1_lvl_1_2.state"
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
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
        assert obs["img"].shape == (144, 160, 3)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
        assert obs["img"].shape == (144, 160, 3)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
        assert obs["img"].shape == (144, 160, 3)

    def test_observation(self):
        """Tests the observation() method."""
        obs = self.env.observation()
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
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
        assert isinstance(obs, dict)
        assert obs["world"].shape == (self.num_envs, 1)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["lives"].shape == (self.num_envs, 1)
        assert obs["coins"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["time"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 144, 160, 3)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        assert isinstance(obs, dict)
        assert obs["world"].shape == (self.num_envs, 1)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["lives"].shape == (self.num_envs, 1)
        assert obs["coins"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["time"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 144, 160, 3)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [1] * self.num_envs
        )
        assert isinstance(obs, dict)
        assert obs["world"].shape == (self.num_envs, 1)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["lives"].shape == (self.num_envs, 1)
        assert obs["coins"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["time"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 144, 160, 3)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, dict)

        vectorized_env.close()


class TestSuperMarioLand1MinimalImage:
    """Tests the SuperMarioLand1MinimalImage class."""

    env_id = "Super-Mario-Land-1-minimal-image-v1"
    rom_path = "./resources/roms/mario/land_1/super_mario_land_1.gb"
    init_state_path = "./resources/tests/mario/land_1/super_mario_land_1_lvl_1_2.state"
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
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
        assert obs["img"].shape == (16, 20)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, dict)

        obs, reward, terminated, truncated, info = self.env.step(1)
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
        assert obs["img"].shape == (16, 20)
        assert isinstance(reward, float)
        assert isinstance(terminated, bool)
        assert isinstance(truncated, bool)
        assert isinstance(info, dict)

    def test_reset(self):
        """Tests the reset() method."""
        obs, _ = self.env.reset()
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
        assert obs["img"].shape == (16, 20)

    def test_observation(self):
        """Tests the observation() method."""
        obs = self.env.observation()
        assert isinstance(obs, dict)
        assert obs["world"].shape == (1,)
        assert obs["level"].shape == (1,)
        assert obs["lives"].shape == (1,)
        assert obs["coins"].shape == (1,)
        assert obs["score"].shape == (1,)
        assert obs["time"].shape == (1,)
        assert obs["img"].shape == (16, 20)

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
        assert isinstance(obs, dict)
        assert obs["world"].shape == (self.num_envs, 1)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["lives"].shape == (self.num_envs, 1)
        assert obs["coins"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["time"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 16, 20)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [0] * self.num_envs
        )
        assert isinstance(obs, dict)
        assert obs["world"].shape == (self.num_envs, 1)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["lives"].shape == (self.num_envs, 1)
        assert obs["coins"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["time"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 16, 20)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, dict)

        obs, reward, terminated, truncated, info = vectorized_env.step(
            [1] * self.num_envs
        )
        assert isinstance(obs, dict)
        assert obs["world"].shape == (self.num_envs, 1)
        assert obs["level"].shape == (self.num_envs, 1)
        assert obs["lives"].shape == (self.num_envs, 1)
        assert obs["coins"].shape == (self.num_envs, 1)
        assert obs["score"].shape == (self.num_envs, 1)
        assert obs["time"].shape == (self.num_envs, 1)
        assert obs["img"].shape == (self.num_envs, 16, 20)
        assert isinstance(reward, np.ndarray)
        assert reward.shape == (self.num_envs,)
        assert isinstance(terminated, np.ndarray)
        assert terminated.shape == (self.num_envs,)
        assert isinstance(truncated, np.ndarray)
        assert truncated.shape == (self.num_envs,)
        assert isinstance(info, dict)

        vectorized_env.close()
