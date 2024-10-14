"""Tests utils/resource.py."""

import os
import unittest

from gymboy.utils import resource_path


class TestResource(unittest.TestCase):
    """Tests all methods under utils/resource.py."""

    def test_resource_path(self):
        """Tests the resource_path() method."""
        path1 = resource_path(
            "resources/states/mario/land_1/super_mario_land_1.state"
        )
        self.assertTrue(os.path.isfile(path1))

        path2 = resource_path(
            "resources/states/pokemon/gen_1/pokemon_blue_after_intro.state"
        )
        self.assertTrue(os.path.isfile(path2))

        path3 = resource_path("resources/states/tetris/tetris/tetris.state")
        self.assertTrue(os.path.isfile(path3))


if __name__ == "__main__":
    unittest.main()
