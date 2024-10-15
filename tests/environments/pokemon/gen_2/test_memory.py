"""Tests pokemon/gen_2/_memory.py."""

import unittest

import numpy as np
from pyboy import PyBoy

from gymboy.environments.pokemon.gen_2._memory import (
    _badges,
    _exps,
    _game_area,
    _hps,
    _levels,
    _max_hps,
    _max_pps,
    _money,
    _mother_money,
    _moves,
    _own_money,
    _owned_pokemons,
    _pokemon_ids,
    _pps,
    _seen_pokemons,
    _team_size,
)


class TestMemory(unittest.TestCase):
    """Tests the methods under the pokemon/gen_2/_memory.py file."""

    def setUp(self):
        self.rom_path = "./gymboy/resources/roms/pokemon/gen_2/pokemon_gold.gbc"
        self.init_state_path1 = (
            "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_1.state"
        )
        self.init_state_path2 = (
            "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_2.state"
        )
        self.init_state_path3 = (
            "./gymboy/resources/states/pokemon/gen_2/pokemon_gold_test_3.state"
        )

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
        self.assertEqual(2, _badges(self.pyboy1))
        self.assertEqual(1, _badges(self.pyboy2))
        self.assertEqual(0, _badges(self.pyboy3))

    def test_own_money(self):
        """Tests the own_money() method."""
        self.assertEqual(12165, _own_money(self.pyboy1))
        self.assertEqual(6008, _own_money(self.pyboy2))
        self.assertEqual(3000, _own_money(self.pyboy3))

    def test_mother_money(self):
        """Tests the mother_money() method."""
        self.assertEqual(2355, _mother_money(self.pyboy1))
        self.assertEqual(0, _mother_money(self.pyboy2))
        self.assertEqual(0, _mother_money(self.pyboy3))

    def test_money(self):
        """Tests the money() method."""
        self.assertEqual(14520, _money(self.pyboy1))
        self.assertEqual(6008, _money(self.pyboy2))
        self.assertEqual(3000, _money(self.pyboy3))

    def test_pokemon_ids(self):
        """Tests the pokemon_ids() method."""
        np.testing.assert_allclose(
            [153, 17, 27, 180, 175, 79], _pokemon_ids(self.pyboy1)
        )
        np.testing.assert_allclose([156, 161, 74, 0, 0, 0], _pokemon_ids(self.pyboy2))
        np.testing.assert_allclose([158, 0, 0, 0, 0, 0], _pokemon_ids(self.pyboy3))

    def test_team_size(self):
        """Tests the team_size() method."""
        self.assertEqual(6, _team_size(self.pyboy1))
        self.assertEqual(3, _team_size(self.pyboy2))
        self.assertEqual(1, _team_size(self.pyboy3))

    def test_levels(self):
        """Tests the levels() method."""
        np.testing.assert_allclose([22, 19, 18, 15, 13, 8], _levels(self.pyboy1))
        np.testing.assert_allclose([15, 13, 8, 0, 0, 0], _levels(self.pyboy2))
        np.testing.assert_allclose([5, 0, 0, 0, 0, 0], _levels(self.pyboy3))

    def test_hps(self):
        """Tests the hps() method."""
        np.testing.assert_allclose([63, 57, 51, 49, 36, 32], _hps(self.pyboy1))
        np.testing.assert_allclose([48, 37, 26, 0, 0, 0], _hps(self.pyboy2))
        np.testing.assert_allclose([20, 0, 0, 0, 0, 0], _hps(self.pyboy3))

    def test_max_hps(self):
        """Tests the max_hps() method."""
        np.testing.assert_allclose([63, 57, 51, 49, 36, 32], _max_hps(self.pyboy1))
        np.testing.assert_allclose([48, 37, 26, 0, 0, 0], _max_hps(self.pyboy2))
        np.testing.assert_allclose([20, 0, 0, 0, 0, 0], _max_hps(self.pyboy3))

    def test_exps(self):
        """Tests the exps() method."""
        np.testing.assert_allclose(
            [8046, 5056, 6164, 2191, 2118, 593], _exps(self.pyboy1)
        )
        np.testing.assert_allclose([2343, 2503, 353, 0, 0, 0], _exps(self.pyboy2))
        np.testing.assert_allclose([135, 0, 0, 0, 0, 0], _exps(self.pyboy3))

    def test_moves(self):
        """Tests the moves() method."""
        np.testing.assert_allclose(
            [
                [33, 45, 75, 115],
                [33, 28, 16, 98],
                [10, 111, 28, 40],
                [33, 45, 84, 0],
                [45, 204, 118, 0],
                [174, 33, 45, 0],
            ],
            _moves(self.pyboy1),
        )
        np.testing.assert_allclose(
            [
                [33, 43, 108, 52],
                [33, 111, 98, 0],
                [33, 111, 0, 0],
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
                [35, 40, 25, 20],
                [35, 15, 35, 30],
                [35, 40, 15, 35],
                [35, 40, 30, 0],
                [40, 20, 10, 0],
                [10, 35, 40, 0],
            ],
            _pps(self.pyboy1),
        )
        np.testing.assert_allclose(
            [
                [35, 30, 20, 25],
                [35, 40, 30, 0],
                [35, 40, 0, 0],
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
                [35, 40, 25, 20],
                [35, 15, 35, 30],
                [35, 40, 15, 35],
                [35, 40, 30, 0],
                [40, 20, 10, 0],
                [10, 35, 40, 0],
            ],
            _max_pps(self.pyboy1),
        )
        np.testing.assert_allclose(
            [
                [35, 30, 20, 25],
                [35, 40, 30, 0],
                [35, 40, 0, 0],
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
        self.assertEqual(40, _seen_pokemons(self.pyboy1))
        self.assertEqual(15, _seen_pokemons(self.pyboy2))
        self.assertEqual(1, _seen_pokemons(self.pyboy3))

    def test_owned_pokemons(self):
        """Tests the owned_pokemons() method."""
        self.assertEqual(9, _owned_pokemons(self.pyboy1))
        self.assertEqual(4, _owned_pokemons(self.pyboy2))
        self.assertEqual(1, _owned_pokemons(self.pyboy3))

    def test_game_area(self):
        """Tests the game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy1),
            np.array([
                [261, 261, 286, 287, 286, 287, 272, 273, 273, 273, 273, 273, 273, 274, 286, 287, 286, 287, 262, 262],
                [261, 261, 275, 277, 275, 277, 269, 270, 270, 270, 270, 270, 270, 271, 275, 277, 275, 277,  16,  17],
                [261, 261, 275, 277, 275, 277, 269, 270, 270, 270, 270, 270, 270, 271, 275, 277, 275, 277,  18,  19],
                [332, 332, 318, 319, 318, 319, 266, 267, 267, 267, 267, 267, 267, 268, 318, 319, 318, 319, 262, 262],
                [261, 261, 286, 287, 286, 287, 282, 263, 263, 263, 263, 263, 263, 284, 261, 261, 261, 261, 262, 262],
                [261, 261, 275, 277, 275, 277, 282, 263, 263, 263, 263, 263, 263, 284, 124, 125, 261, 261, 262, 262],
                [261, 261, 275, 277, 275, 277, 282, 263, 311, 312, 264, 265, 263, 284, 126, 127, 334, 335, 262, 262],
                [261, 261, 318, 319, 318, 319, 257, 258,   0,   1, 279, 279, 258, 278, 261, 261, 350, 351, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262,   2,   3, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [273, 273, 273, 273, 273, 274, 261, 261, 261, 261, 262, 262, 262, 262, 261, 261, 261, 261, 272, 273],
                [270, 270, 270, 270, 270, 271, 261, 261,  76,  77, 262, 262, 262, 262, 261, 261, 261, 261, 266, 267],
                [270, 270, 270, 270, 270, 271, 261, 261,  78,  79, 262, 262, 262, 262, 261, 261, 334, 335, 282, 283],
                [267, 267, 267, 267, 267, 268, 261, 261, 261, 261, 262, 262, 262, 262, 261, 261, 350, 351, 257, 258],
                [283, 283, 283, 283, 283, 284, 261, 261, 261, 261, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [283, 283, 283, 294, 294, 284, 261, 261, 124, 125, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
            ])
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy2),
            np.array([
                [262, 262, 262, 262, 262, 262, 272, 273, 273, 273, 273, 273, 273, 274, 286, 287, 286, 287, 286, 287],
                [262, 262, 262, 262, 262, 262, 269, 270, 270, 270, 270, 270, 270, 271, 318, 319, 318, 319, 318, 319],
                [262, 262, 262, 262, 262, 262, 269, 270, 270, 270, 270, 270, 270, 271, 286, 287, 286, 287, 286, 287],
                [262, 262, 332, 332, 332, 332, 266, 267, 267, 267, 267, 267, 267, 268, 318, 319, 318, 319, 318, 319],
                [262, 262, 262, 262, 262, 262, 282, 263, 263, 263, 263, 263, 263, 284, 286, 287, 286, 287, 262, 262],
                [262, 262, 262, 262, 262, 262, 282, 263, 263, 263, 263, 263, 263, 284, 318, 319, 318, 319, 262, 262],
                [262, 262, 262, 262, 262, 262, 282, 263, 311, 312, 264, 265, 263, 284, 261, 261, 261, 261, 262, 262],
                [262, 262, 262, 262, 262, 262, 257, 258,   0,   1, 279, 279, 258, 278, 261, 261, 261, 261, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262,   2,   3, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262, 262],
                [262, 262, 262, 262, 262, 262, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261],
                [262, 262, 262, 262, 262, 262, 261, 259, 261, 259, 261, 261, 261, 261, 261, 259, 261, 259, 261, 261],
                [262, 262, 262, 262, 262, 262, 259, 261, 259, 261, 261, 261, 261, 261, 259, 261, 259, 261, 261, 261],
                [ 32,  33, 262, 262, 262, 262, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261, 261],
                [ 34,  35, 262, 262, 262, 262, 261, 261, 261, 261, 286, 287, 286, 287, 286, 287, 286, 287, 286, 287],
                [262, 262, 262, 262, 262, 262, 261, 261, 261, 261, 318, 319, 318, 319, 302, 303, 302, 303, 302, 303],
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
