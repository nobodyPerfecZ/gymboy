## Storing State files

In order to use a specific state as the starting point for the environments in Gymboy, you need to store the state files (`*.state`) in your file system.
This directory can be used to store the state files of GameBoy games.

### An example: After Intro State in Pokémon Blue
To use the after intro state in Pokémon Blue, place the state file in the directory `pokemon/gen_1/blue` and name it `pokemon_blue_after_intro.state`.
This is the default value for `init_state_path`.

If you are using custom paths for your state files, ensure that these paths are correctly specified in `init_state_path`!