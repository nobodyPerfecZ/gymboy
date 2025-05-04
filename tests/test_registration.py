"""Tests registration.py."""

from typing import Type

import gymnasium as gym
import pytest

import gymboy
from gymboy.environments.kirby.dream_land_1.kirby_dream_land_1 import (
    KirbyDreamLand1Flatten,
    KirbyDreamLand1FullImage,
    KirbyDreamLand1MinimalImage,
)
from gymboy.environments.mario.land_1.super_mario_land_1 import (
    SuperMarioLand1Flatten,
    SuperMarioLand1FullImage,
    SuperMarioLand1MinimalImage,
)
from gymboy.environments.pokemon.gen_1.blue import (
    PokemonBlueFlatten,
    PokemonBlueFullImage,
    PokemonBlueMinimalImage,
)
from gymboy.environments.pokemon.gen_1.red import (
    PokemonRedFlatten,
    PokemonRedFullImage,
    PokemonRedMinimalImage,
)
from gymboy.environments.pokemon.gen_1.yellow import (
    PokemonYellowFlatten,
    PokemonYellowFullImage,
    PokemonYellowMinimalImage,
)
from gymboy.environments.pokemon.gen_2.gold import (
    PokemonGoldFlatten,
    PokemonGoldFullImage,
    PokemonGoldMinimalImage,
)
from gymboy.environments.pokemon.gen_2.silver import (
    PokemonSilverFlatten,
    PokemonSilverFullImage,
    PokemonSilverMinimalImage,
)
from gymboy.environments.tetris.tetris.tetris import (
    TetrisFlatten,
    TetrisFullImage,
    TetrisMinimalImage,
)


@pytest.mark.parametrize(
    argnames=["env_id", "rom_path", "init_state_path", "expected"],
    argvalues=[
        (
            "Kirby-Dream-Land-1-flatten-v1",
            "resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb",
            "resources/states/kirby/dream_land_1/kirby_dream_land_1_after_intro.state",
            KirbyDreamLand1Flatten,
        ),
        (
            "Kirby-Dream-Land-1-full-image-v1",
            "resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb",
            "resources/states/kirby/dream_land_1/kirby_dream_land_1_after_intro.state",
            KirbyDreamLand1FullImage,
        ),
        (
            "Kirby-Dream-Land-1-minimal-image-v1",
            "resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb",
            "resources/states/kirby/dream_land_1/kirby_dream_land_1_after_intro.state",
            KirbyDreamLand1MinimalImage,
        ),
        (
            "Pokemon-Blue-flatten-v1",
            "resources/roms/pokemon/gen_1/pokemon_blue.gb",
            "resources/states/pokemon/gen_1/pokemon_blue_after_intro.state",
            PokemonBlueFlatten,
        ),
        (
            "Pokemon-Blue-full-image-v1",
            "resources/roms/pokemon/gen_1/pokemon_blue.gb",
            "resources/states/pokemon/gen_1/pokemon_blue_after_intro.state",
            PokemonBlueFullImage,
        ),
        (
            "Pokemon-Blue-minimal-image-v1",
            "resources/roms/pokemon/gen_1/pokemon_blue.gb",
            "resources/states/pokemon/gen_1/pokemon_blue_after_intro.state",
            PokemonBlueMinimalImage,
        ),
        (
            "Pokemon-Gold-flatten-v1",
            "resources/roms/pokemon/gen_2/pokemon_gold.gbc",
            "resources/states/pokemon/gen_2/pokemon_gold_after_intro.state",
            PokemonGoldFlatten,
        ),
        (
            "Pokemon-Gold-full-image-v1",
            "resources/roms/pokemon/gen_2/pokemon_gold.gbc",
            "resources/states/pokemon/gen_2/pokemon_gold_after_intro.state",
            PokemonGoldFullImage,
        ),
        (
            "Pokemon-Gold-minimal-image-v1",
            "resources/roms/pokemon/gen_2/pokemon_gold.gbc",
            "resources/states/pokemon/gen_2/pokemon_gold_after_intro.state",
            PokemonGoldMinimalImage,
        ),
        (
            "Pokemon-Red-flatten-v1",
            "resources/roms/pokemon/gen_1/pokemon_red.gb",
            "resources/states/pokemon/gen_1/pokemon_red_after_intro.state",
            PokemonRedFlatten,
        ),
        (
            "Pokemon-Red-full-image-v1",
            "resources/roms/pokemon/gen_1/pokemon_red.gb",
            "resources/states/pokemon/gen_1/pokemon_red_after_intro.state",
            PokemonRedFullImage,
        ),
        (
            "Pokemon-Red-minimal-image-v1",
            "resources/roms/pokemon/gen_1/pokemon_red.gb",
            "resources/states/pokemon/gen_1/pokemon_red_after_intro.state",
            PokemonRedMinimalImage,
        ),
        (
            "Pokemon-Silver-flatten-v1",
            "resources/roms/pokemon/gen_2/pokemon_silver.gbc",
            "resources/states/pokemon/gen_2/pokemon_silver_after_intro.state",
            PokemonSilverFlatten,
        ),
        (
            "Pokemon-Silver-full-image-v1",
            "resources/roms/pokemon/gen_2/pokemon_silver.gbc",
            "resources/states/pokemon/gen_2/pokemon_silver_after_intro.state",
            PokemonSilverFullImage,
        ),
        (
            "Pokemon-Silver-minimal-image-v1",
            "resources/roms/pokemon/gen_2/pokemon_silver.gbc",
            "resources/states/pokemon/gen_2/pokemon_silver_after_intro.state",
            PokemonSilverMinimalImage,
        ),
        (
            "Pokemon-Yellow-flatten-v1",
            "resources/roms/pokemon/gen_1/pokemon_yellow.gbc",
            "resources/states/pokemon/gen_1/pokemon_yellow_after_intro.state",
            PokemonYellowFlatten,
        ),
        (
            "Pokemon-Yellow-full-image-v1",
            "resources/roms/pokemon/gen_1/pokemon_yellow.gbc",
            "resources/states/pokemon/gen_1/pokemon_yellow_after_intro.state",
            PokemonYellowFullImage,
        ),
        (
            "Pokemon-Yellow-minimal-image-v1",
            "resources/roms/pokemon/gen_1/pokemon_yellow.gbc",
            "resources/states/pokemon/gen_1/pokemon_yellow_after_intro.state",
            PokemonYellowMinimalImage,
        ),
        (
            "Super-Mario-Land-1-flatten-v1",
            "resources/roms/mario/land_1/super_mario_land_1.gb",
            "resources/states/mario/land_1/super_mario_land_1_after_intro.state",
            SuperMarioLand1Flatten,
        ),
        (
            "Super-Mario-Land-1-full-image-v1",
            "resources/roms/mario/land_1/super_mario_land_1.gb",
            "resources/states/mario/land_1/super_mario_land_1_after_intro.state",
            SuperMarioLand1FullImage,
        ),
        (
            "Super-Mario-Land-1-minimal-image-v1",
            "resources/roms/mario/land_1/super_mario_land_1.gb",
            "resources/states/mario/land_1/super_mario_land_1_after_intro.state",
            SuperMarioLand1MinimalImage,
        ),
        (
            "Tetris-flatten-v1",
            "resources/roms/tetris/tetris/tetris.gb",
            "resources/states/tetris/tetris/tetris_after_intro.state",
            TetrisFlatten,
        ),
        (
            "Tetris-full-image-v1",
            "resources/roms/tetris/tetris/tetris.gb",
            "resources/states/tetris/tetris/tetris_after_intro.state",
            TetrisFullImage,
        ),
        (
            "Tetris-minimal-image-v1",
            "resources/roms/tetris/tetris/tetris.gb",
            "resources/states/tetris/tetris/tetris_after_intro.state",
            TetrisMinimalImage,
        ),
    ],
)
def test_make(
    env_id: str,
    rom_path: str,
    init_state_path: str,
    expected: Type[gym.Env],
):
    """Tests the make() method."""
    env = gymboy.make(env_id=env_id, rom_path=rom_path, init_state_path=init_state_path)
    assert isinstance(env, expected)


@pytest.mark.parametrize(
    argnames=["env_id", "num_envs", "rom_path", "init_state_path", "expected"],
    argvalues=[
        (
            "Kirby-Dream-Land-1-flatten-v1",
            1,
            "resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb",
            "resources/states/kirby/dream_land_1/kirby_dream_land_1_after_intro.state",
            KirbyDreamLand1Flatten,
        ),
        (
            "Kirby-Dream-Land-1-full-image-v1",
            1,
            "resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb",
            "resources/states/kirby/dream_land_1/kirby_dream_land_1_after_intro.state",
            KirbyDreamLand1FullImage,
        ),
        (
            "Kirby-Dream-Land-1-minimal-image-v1",
            1,
            "resources/roms/kirby/dream_land_1/kirby_dream_land_1.gb",
            "resources/states/kirby/dream_land_1/kirby_dream_land_1_after_intro.state",
            KirbyDreamLand1MinimalImage,
        ),
        (
            "Pokemon-Blue-flatten-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_blue.gb",
            "resources/states/pokemon/gen_1/pokemon_blue_after_intro.state",
            PokemonBlueFlatten,
        ),
        (
            "Pokemon-Blue-full-image-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_blue.gb",
            "resources/states/pokemon/gen_1/pokemon_blue_after_intro.state",
            PokemonBlueFullImage,
        ),
        (
            "Pokemon-Blue-minimal-image-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_blue.gb",
            "resources/states/pokemon/gen_1/pokemon_blue_after_intro.state",
            PokemonBlueMinimalImage,
        ),
        (
            "Pokemon-Gold-flatten-v1",
            1,
            "resources/roms/pokemon/gen_2/pokemon_gold.gbc",
            "resources/states/pokemon/gen_2/pokemon_gold_after_intro.state",
            PokemonGoldFlatten,
        ),
        (
            "Pokemon-Gold-full-image-v1",
            1,
            "resources/roms/pokemon/gen_2/pokemon_gold.gbc",
            "resources/states/pokemon/gen_2/pokemon_gold_after_intro.state",
            PokemonGoldFullImage,
        ),
        (
            "Pokemon-Gold-minimal-image-v1",
            1,
            "resources/roms/pokemon/gen_2/pokemon_gold.gbc",
            "resources/states/pokemon/gen_2/pokemon_gold_after_intro.state",
            PokemonGoldMinimalImage,
        ),
        (
            "Pokemon-Red-flatten-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_red.gb",
            "resources/states/pokemon/gen_1/pokemon_red_after_intro.state",
            PokemonRedFlatten,
        ),
        (
            "Pokemon-Red-full-image-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_red.gb",
            "resources/states/pokemon/gen_1/pokemon_red_after_intro.state",
            PokemonRedFullImage,
        ),
        (
            "Pokemon-Red-minimal-image-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_red.gb",
            "resources/states/pokemon/gen_1/pokemon_red_after_intro.state",
            PokemonRedMinimalImage,
        ),
        (
            "Pokemon-Silver-flatten-v1",
            1,
            "resources/roms/pokemon/gen_2/pokemon_silver.gbc",
            "resources/states/pokemon/gen_2/pokemon_silver_after_intro.state",
            PokemonSilverFlatten,
        ),
        (
            "Pokemon-Silver-full-image-v1",
            1,
            "resources/roms/pokemon/gen_2/pokemon_silver.gbc",
            "resources/states/pokemon/gen_2/pokemon_silver_after_intro.state",
            PokemonSilverFullImage,
        ),
        (
            "Pokemon-Silver-minimal-image-v1",
            1,
            "resources/roms/pokemon/gen_2/pokemon_silver.gbc",
            "resources/states/pokemon/gen_2/pokemon_silver_after_intro.state",
            PokemonSilverMinimalImage,
        ),
        (
            "Pokemon-Yellow-flatten-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_yellow.gbc",
            "resources/states/pokemon/gen_1/pokemon_yellow_after_intro.state",
            PokemonYellowFlatten,
        ),
        (
            "Pokemon-Yellow-full-image-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_yellow.gbc",
            "resources/states/pokemon/gen_1/pokemon_yellow_after_intro.state",
            PokemonYellowFullImage,
        ),
        (
            "Pokemon-Yellow-minimal-image-v1",
            1,
            "resources/roms/pokemon/gen_1/pokemon_yellow.gbc",
            "resources/states/pokemon/gen_1/pokemon_yellow_after_intro.state",
            PokemonYellowMinimalImage,
        ),
        (
            "Super-Mario-Land-1-flatten-v1",
            1,
            "resources/roms/mario/land_1/super_mario_land_1.gb",
            "resources/states/mario/land_1/super_mario_land_1_after_intro.state",
            SuperMarioLand1Flatten,
        ),
        (
            "Super-Mario-Land-1-full-image-v1",
            1,
            "resources/roms/mario/land_1/super_mario_land_1.gb",
            "resources/states/mario/land_1/super_mario_land_1_after_intro.state",
            SuperMarioLand1FullImage,
        ),
        (
            "Super-Mario-Land-1-minimal-image-v1",
            1,
            "resources/roms/mario/land_1/super_mario_land_1.gb",
            "resources/states/mario/land_1/super_mario_land_1_after_intro.state",
            SuperMarioLand1MinimalImage,
        ),
        (
            "Tetris-flatten-v1",
            1,
            "resources/roms/tetris/tetris/tetris.gb",
            "resources/states/tetris/tetris/tetris_after_intro.state",
            TetrisFlatten,
        ),
        (
            "Tetris-full-image-v1",
            1,
            "resources/roms/tetris/tetris/tetris.gb",
            "resources/states/tetris/tetris/tetris_after_intro.state",
            TetrisFullImage,
        ),
        (
            "Tetris-minimal-image-v1",
            1,
            "resources/roms/tetris/tetris/tetris.gb",
            "resources/states/tetris/tetris/tetris_after_intro.state",
            TetrisMinimalImage,
        ),
    ],
)
def test_make_vec(
    env_id: str,
    num_envs: int,
    rom_path: str,
    init_state_path: str,
    expected: Type[gym.Env],
):
    """Tests the make_vec() method."""
    envs = gymboy.make_vec(
        env_id=env_id,
        num_envs=num_envs,
        rom_path=rom_path,
        init_state_path=init_state_path,
    )
    assert isinstance(envs.envs[0], expected)
