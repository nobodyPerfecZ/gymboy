"""Utility functions for checking the environment inputs."""

import os

import gymnasium as gym
from gymnasium.core import ActType
from pyboy import PyBoy


def check_rom_file(path: str):
    """
    Checks if path is referring to a ROM (.gb or .gbc) file that exists.

    Args:
        path (str):
            The path to the ROM file
    """
    if not path.endswith(".gb") and not path.endswith(".gbc"):
        raise ValueError(f"'{path}' is not referring to a ROM file.")
    if not os.path.exists(path):
        raise FileNotFoundError(f"ROM file '{path}' not found.")


def check_state_file(path: str):
    """
    Checks if path is referring to a state (.state) file that exists.

    Args:
        path (str):
            The path to the state file
    """
    if not path.endswith(".state"):
        raise ValueError(f"'{path}' is not referring to a state file.")
    if not os.path.exists(path):
        raise FileNotFoundError(f"State file '{path}' not found.")


def check_cartridge_title(pyboy: PyBoy, expected_cartridge_title: str):
    """
    Checks if cartridge title of the PyBoy instance matches the expected cartridge title.

    Args:
        pyboy (PyBoy):
            The game boy instance

        expected_cartridge_title (str):
            The expected cartridge title
    """
    if pyboy.cartridge_title != expected_cartridge_title:
        raise ValueError(
            f"Cartridge mismatch, got '{pyboy.cartridge_title}', expected '{expected_cartridge_title}'."
        )


def check_frameskip(n_frameskip: int):
    """
    Checks if n_frameskip is a valid value.

    Args:
        n_frameskip (int):
            The number of frames to skip
    """
    if n_frameskip <= 0:
        raise ValueError(f"n_frameskip must be greater than 0, got {n_frameskip}.")


def check_action(action: ActType, action_space: gym.spaces.Discrete):
    """
    Checks if the action space contains action.

    Args:
        action (ActType):
            The action

        action_space (gym.spaces.Discrete):
            The action space
    """
    if not action_space.contains(action):
        raise ValueError(f"{action} ({type(action)}) invalid.")
