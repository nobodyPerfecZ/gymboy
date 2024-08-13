import unittest

import numpy as np

import gymboy


class TestPokemonBlue(unittest.TestCase):
    """Tests the PokemonBlue class."""

    def setUp(self):
        self.env1 = gymboy.make("Pokemon-Blue-v1", render_mode=None)
        self.env2 = gymboy.make("Pokemon-Blue-v1", render_mode="human")
        self.env3 = gymboy.make("Pokemon-Blue-v1", render_mode="rgb_array")

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


if __name__ == "__main__":
    unittest.main()
