"""Tests pokemon/gen_2/_memory.py."""

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
    """Tests the methods under the pokemon/gen_2/_memory.py file."""

    def setUp(self):
        self.rom_path = "./gymboy/resources/roms/pokemon/gen_2/pokemon_gold.gbc"
        self.init_state_path1 = "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_1.state"
        self.init_state_path2 = "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_2.state"
        self.init_state_path3 = "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_3.state"

        self.pyboy1 = PyBoy(self.rom_path)
        with open(self.init_state_path1, "rb") as f:
            self.pyboy1.load_state(f)
        self.pyboy1.tick(1)

        self.pyboy2 = PyBoy(self.rom_path)
        with open(self.init_state_path2, "rb") as f:
            self.pyboy2.load_state(f)
        self.pyboy2.tick(1)

        self.pyboy3 = PyBoy(self.rom_path)
        with open(self.init_state_path3, "rb") as f:
            self.pyboy3.load_state(f)
        self.pyboy3.tick(1)

    def tearDown(self):
        self.pyboy1.stop()
        self.pyboy2.stop()
        self.pyboy3.stop()

    def test_badges(self):
        """Tests the badges() method."""
        self.assertEqual(0, _badges(self.pyboy1))
        self.assertEqual(0, _badges(self.pyboy2))
        self.assertEqual(0, _badges(self.pyboy3))

    def test_money(self):
        """Tests the money() method."""
        self.assertEqual(3000, _money(self.pyboy1))
        self.assertEqual(3000, _money(self.pyboy2))
        self.assertEqual(3000, _money(self.pyboy3))

    def test_pokemon_ids(self):
        """Tests the pokemon_ids() method."""
        np.testing.assert_allclose([152, 0, 0, 0, 0, 0], _pokemon_ids(self.pyboy1))
        np.testing.assert_allclose([155, 0, 0, 0, 0, 0], _pokemon_ids(self.pyboy2))
        np.testing.assert_allclose([158, 0, 0, 0, 0, 0], _pokemon_ids(self.pyboy3))

    def test_team_size(self):
        """Tests the team_size() method."""
        self.assertEqual(1, _team_size(self.pyboy1))
        self.assertEqual(1, _team_size(self.pyboy2))
        self.assertEqual(1, _team_size(self.pyboy3))

    def test_levels(self):
        """Tests the levels() method."""
        np.testing.assert_allclose([5, 0, 0, 0, 0, 0], _levels(self.pyboy1))
        np.testing.assert_allclose([5, 0, 0, 0, 0, 0], _levels(self.pyboy2))
        np.testing.assert_allclose([5, 0, 0, 0, 0, 0], _levels(self.pyboy3))

    def test_hps(self):
        """Tests the hps() method."""
        np.testing.assert_allclose([19, 0, 0, 0, 0, 0], _hps(self.pyboy1))
        np.testing.assert_allclose([20, 0, 0, 0, 0, 0], _hps(self.pyboy2))
        np.testing.assert_allclose([20, 0, 0, 0, 0, 0], _hps(self.pyboy3))

    def test_max_hps(self):
        """Tests the max_hps() method."""
        np.testing.assert_allclose([19, 0, 0, 0, 0, 0], _max_hps(self.pyboy1))
        np.testing.assert_allclose([20, 0, 0, 0, 0, 0], _max_hps(self.pyboy2))
        np.testing.assert_allclose([20, 0, 0, 0, 0, 0], _max_hps(self.pyboy3))

    def test_exps(self):
        """Tests the exps() method."""
        np.testing.assert_allclose([135, 0, 0, 0, 0, 0], _exps(self.pyboy1))
        np.testing.assert_allclose([135, 0, 0, 0, 0, 0], _exps(self.pyboy2))
        np.testing.assert_allclose([135, 0, 0, 0, 0, 0], _exps(self.pyboy3))

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
            _moves(self.pyboy1),
        )
        np.testing.assert_allclose(
            [
                [33, 43, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _moves(self.pyboy2),
        )
        np.testing.assert_allclose(
            [
                [10, 43, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _moves(self.pyboy3),
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
            _pps(self.pyboy1),
        )
        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _pps(self.pyboy2),
        )
        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _pps(self.pyboy3),
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
            _max_pps(self.pyboy1),
        )
        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _max_pps(self.pyboy2),
        )
        np.testing.assert_allclose(
            [
                [35, 30, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            _max_pps(self.pyboy3),
        )

    def test_seen_pokemons(self):
        """Tests the seen_pokemons() method."""
        self.assertEqual(2, _seen_pokemons(self.pyboy1))
        self.assertEqual(2, _seen_pokemons(self.pyboy2))
        self.assertEqual(2, _seen_pokemons(self.pyboy3))

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy1),
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
        np.testing.assert_allclose(
            _game_area(self.pyboy2),
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
                [262, 262, 262, 262, 262, 262, 262, 262,  33,  32, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262,  35,  34, 262, 262, 334, 335, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 350, 351, 262, 262, 262, 262, 262, 262],
            ])
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy3),
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
                [262, 262, 262, 262, 262, 262, 262, 262,  33,  32, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262,  35,  34, 262, 262, 334, 335, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 350, 351, 262, 262, 262, 262, 262, 262],
            ])
        )


if __name__ == "__main__":
    unittest.main()
