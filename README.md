<div align="middle">
  <h1>
    <p>
      <img src="docs/images/logo.png" alt="Logo" height="300" />
    </p>
    Gymboy 🤖
    <br>
    <span style="font-size: large">
      Gameboy (Color) Environments in Gymnasium 
    </span>
    <br>
      <a href="https://github.com/psf/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg">
      </a>
      <a>
        <img src="https://img.shields.io/badge/python-3.10-blue">
      </a>
      <a>
        <img src="https://img.shields.io/badge/tests-passed-brightgreen">
      </a>
      <a>
        <img src="https://img.shields.io/badge/coverage-99%25-brightgreen">
      </a>
  </h1>
  <img src="docs/gifs/kirby_dream_land_1.gif" alt="Kirby Dream Land 1" width="200" />
  <img src="docs/gifs/pokemon_blue.gif" alt="Pokemon Blue" width="200" />
  <img src="docs/gifs/pokemon_gold.gif" alt="Pokemon Gold" width="200" />
  <img src="docs/gifs/super_mario_land_1.gif" alt="Super Mario Land 1" width="200" />
</div>

Gymboy supports a range of different RL environments from the Game Boy Color using the Gymnasium API.

## Implemented Environments 🌍

| Environment Name                      | Python Source                                                                                                             |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `Kirby-Dream-Land-1-flatten-v1`       | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/kirby/dream_land_1/kirby_dream_land_1.py) |
| `Kirby-Dream-Land-1-minimal-image-v1` | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/kirby/dream_land_1/kirby_dream_land_1.py) |
| `Kirby-Dream-Land-1-full-image-v1`    | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/kirby/dream_land_1/kirby_dream_land_1.py) |
| `Pokemon-Blue-flatten-v1`             | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/blue.py)                    |
| `Pokemon-Blue-minimal-image-v1`       | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/blue.py)                    |
| `Pokemon-Blue-full-image-v1`          | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/blue.py)                    |
| `Pokemon-Gold-flatten-v1`             | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/gold.py)                    |
| `Pokemon-Gold-minimal-image-v1`       | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/gold.py)                    |
| `Pokemon-Gold-full-image-v1`          | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/gold.py)                    |
| `Pokemon-Red-flatten-v1`              | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/red.py)                     |
| `Pokemon-Red-minimal-image-v1`        | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/red.py)                     |
| `Pokemon-Red-full-image-v1`           | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/red.py)                     |
| `Pokemon-Silver-flatten-v1`           | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/silver.py)                  |
| `Pokemon-Silver-minimal-image-v1`     | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/silver.py)                  |
| `Pokemon-Silver-full-image-v1`        | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_2/silver.py)                  |
| `Pokemon-Yellow-flatten-v1`           | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/yellow.py)                  |
| `Pokemon-Yellow-minimal-image-v1`     | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/yellow.py)                  |
| `Pokemon-Yellow-full-image-v1`        | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/pokemon/gen_1/yellow.py)                  |
| `Super-Mario-Land-1-flatten-v1`       | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/mario/land_1/super_mario_land_1.py)       |
| `Super-Mario-Land-1-minimal-image-v1` | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/mario/land_1/super_mario_land_1.py)       |
| `Super-Mario-Land-1-full-image-v1`    | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/mario/land_1/super_mario_land_1.py)       |
| `Tetris-flatten-v1`                   | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/tetris/tetris/tetris.py)                  |
| `Tetris-minimal-image-v1`             | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/tetris/tetris/tetris.py)                  |
| `Tetris-full-image-v1`                | [Click](https://github.com/nobodyPerfecZ/gymboy/blob/master/gymboy/environments/tetris/tetris/tetris.py)                  |

## Installation ⚙️

Install the package via `pip`:

```bash
pip install gymboy
```

> ⚠️ **Important**: Gymboy requires specific ROM files to function properly. Make sure you have the necessary ROMs available before using any of the environments.

## Usage 🚀

Here's a quick example of how to use a gymboy environment:

```python
import gymboy

# Create the environment
env = gymboy.make(
    env_id="Pokemon-Blue-full-image-v1",
    rom_path="./resources/roms/pokemon/gen_1/pokemon_blue.gb",
    init_state_path="./resources/states/pokemon/gen_1/pokemon_blue_after_intro.state",
)
num_steps = 1000

# Reset the environment
obs, info = env.reset()
for i in range(num_steps):
    # Sample a random action
    action = env.action_space.sample()

    # Perform the action
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

    # Render the environment (not necessary for gymboy)
    env.render()

    if done:
        # Case: Environment has terminated
        break
# Close the environment
env.close()
```

## Development 🔧

Contributions are welcome!

Please fork the repository and submit a pull request.

Make sure to follow the coding standards and write tests for any new features or bug fixes.
