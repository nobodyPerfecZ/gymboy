"""Tests utils/env.py."""

import unittest

import gymboy
from gymboy.utils import (
    check_action,
    check_cartridge_title,
    check_frameskip,
    check_rom_file,
    check_state_file,
)


class TestEnv(unittest.TestCase):
    """Tests the methods under utils/env.py."""

    def test_check_rom_file(self):
        """Tests the check_rom_file() method."""
        with self.assertRaises(ValueError):
            check_rom_file("gymboy/resources/roms/tetris/tetris/tetris.txt")

        with self.assertRaises(FileNotFoundError):
            check_rom_file("gymboy/resources/roms/tetris/tetris/invalid.gb")

        check_rom_file("gymboy/resources/roms/tetris/tetris/tetris.gb")

    def test_check_state_file(self):
        """Tests the check_state_file() method."""
        with self.assertRaises(ValueError):
            check_state_file("gymboy/resources/states/tetris/tetris/tetris_9.txt")

        with self.assertRaises(FileNotFoundError):
            check_state_file("gymboy/resources/states/tetris/tetris/invalid.state")

        check_state_file("gymboy/resources/states/tetris/tetris/tetris_9.state")

    def test_check_cartridge_title(self):
        """Tests the check_cartridge_title() method."""
        env = gymboy.make("Pokemon-Blue-flatten-v1")

        with self.assertRaises(ValueError):
            check_cartridge_title(env.pyboy, "POKEMON RED")

        with self.assertRaises(ValueError):
            check_cartridge_title(env.pyboy, "POKEMON YELLOW")

        check_cartridge_title(env.pyboy, "POKEMON BLUE")

    def test_check_frameskip(self):
        """Tests the check_frameskip() method."""
        with self.assertRaises(ValueError):
            check_frameskip(-1)

        with self.assertRaises(ValueError):
            check_frameskip(0)

        check_frameskip(1)

    def test_check_action(self):
        """Tests the check_action() method."""
        env = gymboy.make("Pokemon-Blue-flatten-v1")

        with self.assertRaises(ValueError):
            check_action(-1, env.action_space)

        with self.assertRaises(ValueError):
            check_action(9, env.action_space)

        check_action(0, env.action_space)


if __name__ == "__main__":
    unittest.main()
