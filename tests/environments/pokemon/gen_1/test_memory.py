"""Tests gen_1/_memory.py."""

import unittest

import numpy as np
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_1._memory import (
    _badges,
    _money,
    _pokemon_ids,
    _team_size,
    _levels,
    _hps,
    _max_hps,
    _exps,
    _moves,
    _pps,
    _max_pps,
    _seen_pokemons,
    _events,
    _game_area,
)


class TestMemory(unittest.TestCase):
    """Tests the methods under the pokemon/gen_1/memory.py file."""

    def setUp(self):
        self.pyboy = PyBoy(
            gamerom="./gymboy/resources/roms/pokemon/gen_1/pokemon_blue.gb"
        )
        with open(
            "./gymboy/resources/states/pokemon/gen_1/pokemon_blue_after_first_pokemon.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_badges(self):
        """Tests the badges() method."""
        self.assertEqual(0, _badges(self.pyboy, yellow=False))

    def test_money(self):
        """Tests the money() method."""
        self.assertEqual(3175, _money(self.pyboy, yellow=False))

    def test_pokemon_ids(self):
        """Tests the pokemon_ids() method."""
        np.testing.assert_allclose(
            [177, 0, 0, 0, 0, 0], _pokemon_ids(self.pyboy, yellow=False)
        )

    def test_team_size(self):
        """Tests the team_size() method."""
        self.assertEqual(1, _team_size(self.pyboy, yellow=False))

    def test_levels(self):
        """Tests the levels() method."""
        np.testing.assert_allclose(
            [6, 0, 0, 0, 0, 0], _levels(self.pyboy, yellow=False)
        )

    def test_hps(self):
        """Tests the hps() method."""
        np.testing.assert_allclose([21, 0, 0, 0, 0, 0], _hps(self.pyboy, yellow=False))

    def test_max_hps(self):
        """Tests the max_hps() method."""
        np.testing.assert_allclose(
            [21, 0, 0, 0, 0, 0], _max_hps(self.pyboy, yellow=False)
        )

    def test_exps(self):
        """Tests the exps() method."""
        np.testing.assert_allclose(
            [202, 0, 0, 0, 0, 0], _exps(self.pyboy, yellow=False)
        )

    def test_moves(self):
        """Tests the moves() method."""
        np.testing.assert_allclose(
            [
                [33, 39, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _moves(self.pyboy, yellow=False),
        )

    def test_pps(self):
        """Tests the pps() method."""
        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _pps(self.pyboy, yellow=False),
        )

    def test_max_pps(self):
        """Tests the max_pps() method."""
        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _max_pps(self.pyboy, yellow=False),
        )

    def test_seen_pokemons(self):
        """Tests the seen_pokemons() method."""
        self.assertEqual(2, _seen_pokemons(self.pyboy, yellow=False))

    def test_events(self):
        """Tests the events() method."""
        self.assertEqual(7, _events(self.pyboy, yellow=False))

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy),
            np.array([
                [300, 300, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291],
                [300, 300, 313, 291, 291, 291, 313, 291, 291, 291, 313, 291, 291, 291, 313, 291, 291, 291, 313, 291],
                [300, 300, 291, 291, 291, 291, 261, 262, 263, 263, 263, 263, 264, 265, 291, 291, 291, 291, 291, 291],
                [300, 300, 291, 291, 313, 291, 277, 278, 279, 279, 279, 279, 280, 281, 291, 291, 313, 291, 291, 291],
                [300, 300, 313, 313, 313, 313, 293, 294, 266, 290, 266, 266, 296, 297, 291, 291, 291, 291, 313, 313],
                [300, 300, 313, 313, 313, 313, 348, 279, 279, 279, 279, 279, 279, 349, 313, 291, 291, 291, 313, 313],
                [300, 300, 313, 313, 326, 327, 271, 290, 267, 268, 266, 266, 290, 287, 291, 291, 291, 291, 313, 313],
                [300, 300, 313, 313, 342, 343, 334, 282,   0,   1, 282, 282, 282, 335, 291, 291, 313, 291, 313, 313],
                [300, 300, 291, 291, 291, 291, 291, 291,   2,   3, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291],
                [300, 300, 313, 291, 291, 291, 313, 291, 291, 291, 313, 291, 291, 291, 313, 291, 291, 291, 313, 291],
                [300, 300, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291, 291],
                [300, 300, 291, 291, 313, 291, 291, 291, 313, 291,  45,  44, 313, 291, 291, 291, 313, 291, 291, 291],
                [300, 300, 291, 291, 291, 291, 313, 313, 313, 313,  47,  46, 313, 313, 291, 291, 291, 291, 261, 262],
                [300, 300, 313, 291, 291, 291, 313, 313, 313, 313, 313, 313, 313, 313, 313, 291, 291, 291, 277, 312],
                [300, 300, 291, 291, 291, 291, 270, 270, 270, 270, 270, 270, 326, 327, 291, 291, 291, 291, 277, 312],
                [300, 300, 291, 291, 313, 291, 341, 341, 341, 341, 341, 341, 342, 343, 291, 291, 313, 291, 277, 278],
                [300, 300, 291, 291, 291, 291, 300, 300, 300, 300, 300, 300, 300, 300, 291, 291, 291, 291, 293, 294],
                [300, 300, 313, 291, 291, 291, 300, 259, 300, 259, 300, 259, 300, 259, 313, 291, 291, 291, 271, 290],
            ])
        )


if __name__ == "__main__":
    unittest.main()
