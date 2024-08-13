from pyboy import PyBoy


if __name__ == "__main__":
    pyboy = PyBoy("./gymboy/resources/roms/pokemon_silver.gbc")
    with open("./gymboy/resources/states/pokemon_silver_after_intro.state", "rb") as f:
        pyboy.load_state(f)
    while pyboy.tick():
        pass
    pyboy.stop()
