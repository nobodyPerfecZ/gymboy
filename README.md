<p align="center"><img src="docs/logo_curved.png" alt="Logo"></p>

<h1 align="center">Gameboy (Color) Environments in Gymnasium 🤖</h1>

Gymboy supports a range of different RL environments from the Game Boy Color using the Gymnasium API.

To use these environments, you need to manually install the specific game ROMs listed under `ROM Version`.

## Implemented Environments 🌍
| Environment Name                | ROM Version                          | Source                                                                                                                   |
|---------------------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `Pokemon-Blue-flatten-v1`       | Pokemon - Blue Version (UE)[!]       | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/blue/blue.py#L26)          |
| `Pokemon-Blue-image-v1`         | Pokemon - Blue Version (UE)[!]       | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/blue/blue.py#L189)         |
| `Pokemon-Red-flatten-v1`        | Pokemon - Red Version (UE)[!]        | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/red/red.py#L26)            |
| `Pokemon-Red-image-v1`          | Pokemon - Red Version (UE)[!]        | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/red/red.py#L187)           |
| `Pokemon-Yellow-flatten-v1`     | Pokemon - Yellow Version (UE) [C][!] | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/yellow/yellow.py#L26)      |
| `Pokemon-Yellow-image-v1`       | Pokemon - Yellow Version (UE) [C][!] | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/yellow/yellow.py#L196)     |
| `Pokemon-Gold-flatten-v1`       | Pokemon - Gold Version (UE) [C][!]   | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/gold/gold.py#L24)          |
| `Pokemon-Gold-image-v1`         | Pokemon - Gold Version (UE) [C][!]   | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/gold/gold.py#L179)         |
| `Pokemon-Silver-flatten-v1`     | Pokemon - Silver Version (UE) [C][!] | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/silver/silver.py#L24)      |
| `Pokemon-Silver-image-v1`       | Pokemon - Silver Version (UE) [C][!] | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/silver/silver.py#L179)     |
| `Tetris-flatten-v1`             | Tetris (JUE) (V1.1) [!]              | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/tetris/tetris/tetris.py#L14)             |
| `Tetris-image-v1`               | Tetris (JUE) (V1.1) [!]              | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/tetris/tetris/tetris.py#L155)            |
| `Super-Mario-Land-1-flatten-v1` | Super Mario Land (JUE) (V1.1) [!]    | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/mario/land_1/super_mario_land_1.py#L24)  |
| `Super-Mario-Land-1-image-v1`   | Super Mario Land (JUE) (V1.1) [!]    | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/mario/land_1/super_mario_land_1.py#L183) |

## Installation ⚙️
TODO: Add text here

## TODOs ⛏
- Add an environment version to handle JAX (with gymnax)

## Development 🔧
Contributions are welcome! Please fork the repository and submit a pull request. Make sure to follow the coding standards and write tests for any new features or bug fixes.