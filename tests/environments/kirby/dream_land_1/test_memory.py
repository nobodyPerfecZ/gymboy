"""Tests kirby/dream_land_1/_memory.py."""

import unittest

import numpy as np
from pyboy import PyBoy

from gymboy.environments.kirby.dream_land_1._memory import (
    _boss_health,
    _game_area,
    _game_over,
    _kirby_health,
    _lives,
    _score,
)


class TestMemory(unittest.TestCase):
    """Tests the methods under kirby/dream_land_1/_memory.py."""

    def setUp(self):
        self.rom_path = "./resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb"
        self.init_state_path1 = (
            "./resources/states/kirby/dream_land_1/kirby_dream_land_1_after_intro.state"
        )
        self.init_state_path2 = (
            "./resources/states/kirby/dream_land_1/kirby_dream_land_1_stage_1.state"
        )
        self.init_state_path3 = (
            "./resources/states/kirby/dream_land_1/kirby_dream_land_1_stage_2.state"
        )

        self.pyboy1 = PyBoy(self.rom_path, sound_emulated=False)
        with open(self.init_state_path1, "rb") as f:
            self.pyboy1.load_state(f)
        self.pyboy1.tick(1)

        self.pyboy2 = PyBoy(self.rom_path, sound_emulated=False)
        with open(self.init_state_path2, "rb") as f:
            self.pyboy2.load_state(f)
        self.pyboy2.tick(1)

        self.pyboy3 = PyBoy(self.rom_path, sound_emulated=False)
        with open(self.init_state_path3, "rb") as f:
            self.pyboy3.load_state(f)
        self.pyboy3.tick(1)

    def tearDown(self):
        self.pyboy1.stop()
        self.pyboy2.stop()
        self.pyboy3.stop()

    def test_score(self):
        """Tests the _score() method."""
        self.assertEqual(0, _score(self.pyboy1))
        self.assertEqual(2600, _score(self.pyboy2))
        self.assertEqual(47510, _score(self.pyboy3))

    def test_kirby_health(self):
        """Tests the _kirby_health() method."""
        self.assertEqual(6, _kirby_health(self.pyboy1))
        self.assertEqual(5, _kirby_health(self.pyboy2))
        self.assertEqual(6, _kirby_health(self.pyboy3))

    def test_boss_health(self):
        """Tests the _boss_health() method."""
        self.assertEqual(0, _boss_health(self.pyboy1))
        self.assertEqual(0, _boss_health(self.pyboy2))
        self.assertEqual(0, _boss_health(self.pyboy3))

    def test_lives(self):
        """Tests the _lives() method."""
        self.assertEqual(5, _lives(self.pyboy1))
        self.assertEqual(5, _lives(self.pyboy2))
        self.assertEqual(4, _lives(self.pyboy3))

    def test_game_over(self):
        """Tests the _game_over() method."""
        self.assertFalse(_game_over(self.pyboy1))
        self.assertFalse(_game_over(self.pyboy2))
        self.assertFalse(_game_over(self.pyboy3))

    def test_game_area(self):
        """Tests the _game_area() method."""
        np.testing.assert_allclose(
            _game_area(self.pyboy1),
            np.array(
                [
                    [
                        383,
                        383,
                        383,
                        383,
                        293,
                        292,
                        383,
                        383,
                        383,
                        383,
                        301,
                        383,
                        383,
                        383,
                        297,
                        383,
                        383,
                        313,
                        312,
                        311,
                    ],
                    [
                        383,
                        383,
                        383,
                        299,
                        383,
                        383,
                        298,
                        383,
                        383,
                        383,
                        383,
                        300,
                        294,
                        295,
                        296,
                        383,
                        315,
                        314,
                        383,
                        383,
                    ],
                    [
                        383,
                        383,
                        301,
                        383,
                        383,
                        383,
                        297,
                        383,
                        383,
                        383,
                        290,
                        291,
                        383,
                        383,
                        383,
                        383,
                        316,
                        383,
                        383,
                        383,
                    ],
                    [
                        298,
                        383,
                        383,
                        300,
                        294,
                        295,
                        296,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        317,
                        383,
                        383,
                        383,
                    ],
                    [
                        297,
                        383,
                        290,
                        291,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        293,
                        292,
                        383,
                        383,
                        290,
                        291,
                        317,
                        383,
                        383,
                        383,
                    ],
                    [
                        296,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        299,
                        383,
                        383,
                        298,
                        383,
                        383,
                        383,
                        317,
                        383,
                        383,
                        383,
                    ],
                    [
                        293,
                        292,
                        383,
                        383,
                        383,
                        307,
                        308,
                        383,
                        301,
                        383,
                        383,
                        383,
                        297,
                        383,
                        383,
                        383,
                        317,
                        383,
                        383,
                        307,
                    ],
                    [
                        383,
                        383,
                        298,
                        383,
                        383,
                        309,
                        310,
                        383,
                        383,
                        300,
                        294,
                        295,
                        296,
                        383,
                        383,
                        299,
                        317,
                        383,
                        383,
                        309,
                    ],
                    [
                        383,
                        383,
                        297,
                        383,
                        383,
                        309,
                        307,
                        308,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        383,
                        317,
                        383,
                        383,
                        309,
                    ],
                    [
                        294,
                        295,
                        296,
                        383,
                        383,
                        309,
                        309,
                        310,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        300,
                        325,
                        383,
                        383,
                        309,
                    ],
                    [
                        272,
                        274,
                        383,
                        383,
                        2,
                        18,
                        309,
                        310,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        307,
                        308,
                    ],
                    [
                        275,
                        276,
                        272,
                        274,
                        3,
                        19,
                        309,
                        310,
                        272,
                        274,
                        383,
                        383,
                        383,
                        383,
                        272,
                        274,
                        272,
                        274,
                        309,
                        310,
                    ],
                    [
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        332,
                        331,
                        331,
                        331,
                        331,
                    ],
                    [
                        328,
                        328,
                        277,
                        278,
                        277,
                        278,
                        277,
                        278,
                        328,
                        328,
                        328,
                        328,
                        328,
                        328,
                        328,
                        333,
                        328,
                        328,
                        328,
                        328,
                    ],
                    [
                        277,
                        278,
                        279,
                        281,
                        279,
                        281,
                        279,
                        281,
                        277,
                        278,
                        328,
                        328,
                        277,
                        278,
                        328,
                        333,
                        328,
                        328,
                        277,
                        278,
                    ],
                    [
                        279,
                        281,
                        280,
                        282,
                        280,
                        282,
                        280,
                        282,
                        279,
                        281,
                        277,
                        278,
                        279,
                        281,
                        328,
                        333,
                        277,
                        278,
                        279,
                        281,
                    ],
                ]
            ),
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy2),
            np.array(
                [
                    [
                        383,
                        383,
                        383,
                        293,
                        292,
                        293,
                        292,
                        383,
                        383,
                        156,
                        158,
                        383,
                        383,
                        297,
                        383,
                        383,
                        383,
                        383,
                        383,
                        293,
                    ],
                    [
                        383,
                        383,
                        299,
                        383,
                        383,
                        383,
                        383,
                        298,
                        383,
                        157,
                        159,
                        294,
                        156,
                        158,
                        383,
                        383,
                        383,
                        383,
                        299,
                        383,
                    ],
                    [
                        383,
                        301,
                        383,
                        383,
                        383,
                        383,
                        383,
                        297,
                        383,
                        383,
                        383,
                        383,
                        157,
                        159,
                        291,
                        383,
                        383,
                        301,
                        383,
                        383,
                    ],
                    [
                        383,
                        383,
                        300,
                        294,
                        295,
                        294,
                        295,
                        296,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        300,
                        294,
                    ],
                    [
                        383,
                        293,
                        292,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        313,
                        312,
                        311,
                        318,
                        319,
                        320,
                        383,
                        383,
                        383,
                        383,
                    ],
                    [
                        299,
                        383,
                        383,
                        298,
                        383,
                        383,
                        383,
                        383,
                        383,
                        315,
                        314,
                        383,
                        383,
                        383,
                        383,
                        321,
                        322,
                        383,
                        383,
                        383,
                    ],
                    [
                        383,
                        383,
                        383,
                        297,
                        383,
                        383,
                        383,
                        383,
                        383,
                        316,
                        383,
                        352,
                        383,
                        383,
                        383,
                        383,
                        323,
                        383,
                        383,
                        301,
                    ],
                    [
                        300,
                        294,
                        295,
                        296,
                        383,
                        383,
                        383,
                        383,
                        383,
                        317,
                        383,
                        353,
                        354,
                        383,
                        383,
                        383,
                        324,
                        383,
                        383,
                        383,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        307,
                        308,
                        383,
                        317,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        324,
                        307,
                        308,
                        383,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        309,
                        310,
                        383,
                        317,
                        383,
                        357,
                        358,
                        383,
                        383,
                        383,
                        324,
                        309,
                        310,
                        216,
                    ],
                    [
                        274,
                        383,
                        383,
                        383,
                        383,
                        307,
                        308,
                        307,
                        2,
                        18,
                        383,
                        380,
                        380,
                        383,
                        383,
                        383,
                        324,
                        309,
                        310,
                        217,
                    ],
                    [
                        276,
                        272,
                        274,
                        272,
                        274,
                        309,
                        310,
                        309,
                        3,
                        19,
                        383,
                        380,
                        380,
                        383,
                        383,
                        383,
                        324,
                        309,
                        310,
                        310,
                    ],
                    [
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                    ],
                    [
                        278,
                        277,
                        278,
                        277,
                        278,
                        277,
                        278,
                        328,
                        328,
                        277,
                        278,
                        277,
                        278,
                        277,
                        278,
                        277,
                        278,
                        277,
                        278,
                        277,
                    ],
                    [
                        281,
                        279,
                        281,
                        279,
                        281,
                        279,
                        281,
                        277,
                        278,
                        279,
                        281,
                        279,
                        281,
                        279,
                        281,
                        279,
                        281,
                        279,
                        281,
                        279,
                    ],
                    [
                        282,
                        280,
                        282,
                        280,
                        282,
                        280,
                        282,
                        279,
                        281,
                        280,
                        282,
                        280,
                        282,
                        280,
                        282,
                        280,
                        282,
                        280,
                        282,
                        280,
                    ],
                ]
            ),
        )
        np.testing.assert_allclose(
            _game_area(self.pyboy3),
            np.array(
                [
                    [
                        383,
                        383,
                        292,
                        293,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        299,
                        297,
                        299,
                        297,
                        299,
                    ],
                    [
                        383,
                        383,
                        294,
                        295,
                        296,
                        383,
                        383,
                        383,
                        292,
                        293,
                        383,
                        383,
                        383,
                        383,
                        301,
                        297,
                        299,
                        298,
                        300,
                        297,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        292,
                        293,
                        383,
                        383,
                        294,
                        295,
                        296,
                        383,
                        383,
                        383,
                        302,
                        218,
                        216,
                        299,
                        297,
                        299,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        294,
                        295,
                        296,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        219,
                        217,
                        297,
                        299,
                        298,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        324,
                        325,
                        324,
                        325,
                        324,
                        325,
                        324,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        305,
                        309,
                        383,
                        383,
                        305,
                        301,
                        299,
                        299,
                        299,
                        299,
                        299,
                        299,
                        299,
                    ],
                    [
                        307,
                        383,
                        383,
                        383,
                        307,
                        383,
                        306,
                        382,
                        382,
                        309,
                        306,
                        382,
                        302,
                        300,
                        297,
                        299,
                        297,
                        299,
                        297,
                        299,
                    ],
                    [
                        382,
                        308,
                        309,
                        305,
                        382,
                        308,
                        382,
                        382,
                        382,
                        382,
                        382,
                        382,
                        301,
                        297,
                        299,
                        297,
                        299,
                        298,
                        300,
                        297,
                    ],
                    [
                        319,
                        319,
                        319,
                        319,
                        319,
                        319,
                        319,
                        319,
                        319,
                        319,
                        319,
                        319,
                        301,
                        299,
                        297,
                        299,
                        297,
                        299,
                        297,
                        299,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        297,
                        299,
                        298,
                        300,
                        297,
                        299,
                        298,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        302,
                        300,
                        297,
                        299,
                        298,
                        300,
                        297,
                        299,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        297,
                        357,
                        358,
                        299,
                        297,
                        299,
                        297,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        2,
                        18,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        299,
                        380,
                        380,
                        298,
                        300,
                        297,
                        299,
                    ],
                    [
                        383,
                        383,
                        383,
                        383,
                        3,
                        19,
                        383,
                        383,
                        383,
                        383,
                        383,
                        383,
                        301,
                        298,
                        380,
                        380,
                        299,
                        297,
                        299,
                        298,
                    ],
                    [
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                        330,
                    ],
                    [
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                        331,
                    ],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
