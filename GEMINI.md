# GEMINI.md

This file provides guidance to Gemini CLI when working with code in this repository.

## Project Overview

`gymboy` is a Python library that wraps the
[PyBoy](https://github.com/Baekalfen/PyBoy) Gameboy (Color) emulator to expose
standard [Gymnasium](https://gymnasium.farama.org/) reinforcement learning
environments. It supports games such as Kirby's Dream Land 1, Super Mario Land
1, Tetris, and Pokemon (Red, Blue, Yellow, Gold, Silver), providing both minimal
state representations (e.g., memory/simplified tiles) and full image
observations.

## Project Structure

- `gymboy/`: Main library package source code.
  - `environments/`: Game-specific environment implementations.
    - `kirby/`: Kirby's Dream Land 1 environments (`KirbyDreamLand1FullImage`, `KirbyDreamLand1MinimalImage`).
    - `mario/`: Super Mario Land 1 environments (`SuperMarioLand1FullImage`, `SuperMarioLand1MinimalImage`).
    - `pokemon/`: Generation 1 (Red, Blue, Yellow) and Generation 2 (Gold, Silver) Pokemon environments.
    - `tetris/`: Tetris environments (`TetrisFullImage`, `TetrisMinimalImage`).
    - `env.py`: Defines the `PyBoyEnv` base class (subclass of `gym.Env` and `ABC`).
  - `utils/`: Utility and helper modules.
    - `binary.py`: Byte manipulation and memory reading utilities.
  - `registration.py`: Environment registration and creation helpers (`make`, `make_vec`, `registered_envs`).
  - `__init__.py`: Package interface exposing `make`, `make_vec`, and `registered_envs`.
- `tests/`: Comprehensive test suite mirroring the library structure.
  - `environments/`: Environment-specific test cases.
  - `utils/`: Utility function tests.
  - `test_registration.py`: Tests for `make` and `make_vec` factory methods.
- `docs/`: Asset files and media used in documentation.
  - `gifs/`: Demonstration GIFs of the environments.
  - `images/`: Logos and other image assets.

## Commands

All commands are run using [uv](https://docs.astral.sh/uv/):

- Run tests: `uv run pytest tests`
- Run all checks (linting, tests, etc.): `uv run tox`
- Lint code: `uv run ruff check gymboy tests`
- Format code: `uv run ruff format gymboy tests`
- Type check: `uv run ty check gymboy tests`
- Dependency check: `uv run deptry gymboy tests`
- Security scan: `uv run bandit -r gymboy tests`
- Lint markdown: `uv run rumdl check README.md`
- Build package: `uv build`
- Publish to TestPyPI (CI only): `uv publish --index testpypi --token ...`

## CI/CD Pipelines

- [Check Format](.github/workflows/lint.yml): Verifies code formatting and checks linting rules with Ruff.
- [Run Unittests](.github/workflows/test.yml): Automatically downloads ROM assets and runs the test suite using pytest.
- [Publish TestPyPI](.github/workflows/release.yml): Builds and publishes package releases to TestPyPI.

## Coding Standards

- **Type Hints:** All functions, methods, and classes MUST include complete type annotations.
- **Docstrings:** Public classes, methods, and functions MUST include descriptive docstrings, detailing Action Space, Observation Space, and Rewards where applicable.
- **Ruff Guidelines:** Adhere to Ruff configuration specified in `pyproject.toml` (target Python 3.10+, line length 88, select E, F, B, I).
- **Environment Interface:** Implement environments by inheriting from `PyBoyEnv` and overriding the abstract methods: `observation_space`, `observation`, `reward`, `terminated`, and `truncated`.

## Resources

### Core Stack

- [Gymnasium](https://gymnasium.farama.org/)
- [PyBoy](https://github.com/Baekalfen/PyBoy)
- [scikit-image](https://scikit-image.org/)
- [Python 3.10](https://docs.python.org/3.10/)
- [uv](https://docs.astral.sh/uv/)

### Testing & Code Quality

- [bandit](https://bandit.readthedocs.io/en/latest/)
- [deptry](https://deptry.com/)
- [pytest](https://docs.pytest.org/en/stable/)
- [ruff](https://docs.astral.sh/ruff/)
- [rumdl](https://rumdl.dev/)
- [tox-uv](https://github.com/tox-dev/tox-uv)
- [ty](https://docs.astral.sh/ty/)
