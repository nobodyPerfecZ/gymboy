"""Tests gen_2/_memory.py."""

import unittest

import numpy as np
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_2._memory import (
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
    _game_area,
)


class TestMemory(unittest.TestCase):
    """Tests the methods under the pokemon/gen_2/memory.py file."""

    def setUp(self):
        self.pyboy = PyBoy(
            gamerom="./gymboy/resources/roms/pokemon/gen_2/pokemon_gold.gbc"
        )
        with open(
            "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_after_first_pokemon.state",
            "rb",
        ) as f:
            self.pyboy.load_state(f)
        self.pyboy.tick(1)

    def tearDown(self):
        self.pyboy.stop()

    def test_badges(self):
        """Tests the badges() method."""
        self.assertEqual(0, _badges(self.pyboy))

    def test_money(self):
        """Tests the money() method."""
        self.assertEqual(3000, _money(self.pyboy))

    def test_pokemon_ids(self):
        """Tests the pokemon_ids() method."""
        np.testing.assert_allclose([152, 0, 0, 0, 0, 0], _pokemon_ids(self.pyboy))

    def test_team_size(self):
        """Tests the team_size() method."""
        self.assertEqual(1, _team_size(self.pyboy))

    def test_levels(self):
        """Tests the levels() method."""
        np.testing.assert_allclose([5, 0, 0, 0, 0, 0], _levels(self.pyboy))

    def test_hps(self):
        """Tests the hps() method."""
        np.testing.assert_allclose([19, 0, 0, 0, 0, 0], _hps(self.pyboy))

    def test_max_hps(self):
        """Tests the max_hps() method."""
        np.testing.assert_allclose([19, 0, 0, 0, 0, 0], _max_hps(self.pyboy))

    def test_exps(self):
        """Tests the exps() method."""
        np.testing.assert_allclose([135, 0, 0, 0, 0, 0], _exps(self.pyboy))

    def test_moves(self):
        """Tests the moves() method."""
        np.testing.assert_allclose(
            [
                [33, 45, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _moves(self.pyboy),
        )

    def test_pps(self):
        """Tests the pps() method."""
        np.testing.assert_allclose(
            [
                [35, 40, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _pps(self.pyboy),
        )

    def test_max_pps(self):
        """Tests the max_pps() method."""
        np.testing.assert_allclose(
            [
                [35, 40, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _max_pps(self.pyboy),
        )

    def test_seen_pokemons(self):
        """Tests the seen_pokemons() method."""
        self.assertEqual(2, _seen_pokemons(self.pyboy))

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy),
            np.array([
                [286, 287, 286, 287, 272, 273, 273, 273, 273, 273, 273, 273, 273, 273, 273, 274, 286, 287, 286, 287],
                [302, 303, 302, 303, 269, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 271, 302, 303, 302, 303],
                [302, 303, 302, 303, 269, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 271, 302, 303, 302, 303],
                [318, 319,  21,  20, 266, 267, 267, 267, 267, 267, 267, 267, 267, 267, 267, 268, 318, 319, 318, 319],
                [261, 261,  23,  22, 282, 283, 283, 283, 283, 283, 283, 283, 283, 283, 283, 284, 286, 287, 286, 287],
                [261, 261, 261, 261, 282, 294, 294, 283, 283, 283, 283, 283, 283, 294, 294, 284, 302, 303, 302, 303],
                [261, 261, 334, 335, 282, 283, 283, 283, 311, 312, 283, 283, 283, 283, 283, 284, 302, 303, 302, 303],
                [261, 261, 350, 351, 257, 258, 258, 258,   0,   1, 258, 258, 258, 258, 258, 278, 318, 319, 318, 319],
                [261, 261, 261, 261, 262, 262, 262, 262,   2,   3, 262, 262, 262, 262, 262, 262, 261, 261, 261, 261],
                [261, 261, 261, 261, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 261, 261, 261, 261],
                [261, 261, 261, 261, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 261, 261, 334, 335],
                [261, 261, 261, 261, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 261, 261, 350, 351],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262,  32,  33, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262,  34,  35, 262, 262, 334, 335, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 350, 351, 262, 262, 262, 262, 262, 262],
            ])
        )


if __name__ == "__main__":
    unittest.main()
