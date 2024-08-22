import unittest

import numpy as np
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_1.memory import *


class TestMemory(unittest.TestCase):
    """Tests the methods under the memory.py file."""

    def setUp(self):
        self.pyboy = PyBoy(
            gamerom="./gymboy/resources/roms/pokemon/gen_1/blue/pokemon_blue.gb"
        )
        with open(
            "./tests/resources/states/pokemon/gen_1/blue/pokemon_blue_first_pokemon.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_get_badges(self):
        """Tests the get_badges() method."""
        badges = get_badges(self.pyboy, yellow=False)
        self.assertEqual(0, badges)

    def test_get_money(self):
        """Tests the get_money() method."""
        money = get_money(self.pyboy, yellow=False)
        self.assertEqual(3175, money)

    def test_get_team_size(self):
        """Tests the get_team_size() method."""
        team_size = get_team_size(self.pyboy, yellow=False)
        self.assertEqual(1, team_size)

    def test_get_levels(self):
        """Tests the get_levels() method."""
        levels = get_levels(self.pyboy, yellow=False)
        np.testing.assert_allclose([6, 0, 0, 0, 0, 0], levels)

    def test_get_hps(self):
        """Tests the get_hps() method."""
        hps = get_hps(self.pyboy, yellow=False)
        np.testing.assert_allclose([21, 0, 0, 0, 0, 0], hps)

    def test_get_max_hps(self):
        """Tests the get_max_hps() method."""
        max_hps = get_max_hps(self.pyboy, yellow=False)
        np.testing.assert_allclose([21, 0, 0, 0, 0, 0], max_hps)

    def test_get_exps(self):
        """Tests the get_exps() method."""
        exps = get_exps(self.pyboy, yellow=False)
        np.testing.assert_allclose([202, 0, 0, 0, 0, 0], exps)

    def test_get_moves(self):
        """Tests the get_moves() method."""
        moves = get_moves(self.pyboy, yellow=False)
        np.testing.assert_allclose(
            [
                [33, 39, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            moves,
        )

    def test_get_pps(self):
        """Tests the get_pps() method."""
        pps = get_pps(self.pyboy, yellow=False)
        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            pps,
        )

    def test_get_max_pps(self):
        """Tests the max_pps() method."""
        max_pps = get_max_pps(self.pyboy, yellow=False)

        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            max_pps,
        )

    def test_get_seen_pokemons(self):
        """Tests the get_seen_pokemons() method."""
        seen_pokemons = get_seen_pokemons(self.pyboy, yellow=False)
        self.assertEqual(2, seen_pokemons)

    def test_get_events(self):
        """Tests the get_events() method."""
        events = get_events(self.pyboy, yellow=False)
        self.assertEqual(7, events)


if __name__ == "__main__":
    unittest.main()
