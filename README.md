# Twilight Princess

## Installation & Usage

See the [setup guide](https://github.com/WritingHusky/Twilight_Princess_apworld/blob/main/docs/setup_en.md) for instructions.

## What does randomization do to this game?

Items get shuffled between the different locations in the game, so each playthrough is unique. Randomized locations might include chests, items received from NPCs, Golden Bugs, Poes. The randomizer also includes quality-of-life features such as a fully-opened world, removing many cutscenes, transform anywhere, and more.

## Which locations get shuffled?

Currently all possible locations get shuffled into the pool and get an item. New versions plan to expand this functionality

## What is the goal of Twilight Princess?

Reach and defeat Ganondorf in Hyrule Castle. This will require the Master Sword (Light filled is not needed), and any other items necessary to reach Ganondorf.

## What does another world's item look like in TP?

Currently all items are a green rupee, if the item is part of your world you will be given it after closing the text box.

## When the player receives an item, what happens?

When the player receives an item, it will be added to a queue, where link will get the items one by one. Like many other Zelda randomizers, Link **will** hold the item out causing him to pause so be ready.

## I need help! What do I do?

Refer to the [Base Randomizer Website](https://tprandomizer.com/) first. Then, try the troubleshooting steps in the [setup guide](https://github.com/WritingHusky/Twilight_Princess_apworld/blob/main/docs/setup_en.md). If you are still stuck, please ask in the Twilight Princess thread (under `future-game-design`) in the Archipelago server.

## Running from source

### Installing Git

Download and install git from here: https://git-scm.com/downloads  
Then clone this repository with git by running this in a command prompt:

```
git clone https://github.com/WritingHusky/Twilight_Princess_apworld.git
```

### Installing Python

You will need to install Python 3.12. We recommend using `pyenv` to manage different Python versions:

- For Windows, install `pyenv-win` by following
  [these steps](https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file#quick-start).
- For Linux, follow the instructions [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#automatic-installer) to
  install `pyenv` and then follow the instructions
  [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv) to set up your shell
  environment.

After installing `pyenv`, install and switch to Python 3.12 by running:

```sh
pyenv install 3.12
pyenv global 3.12
```

## Credits

This randomizer would not be possible without the help from:

- LunarSoap and the TPRandomizer community
- Tanjo3 and the Wind Waker AP (Heavy Inspriation code wise)
- Every one who has reported bugs and requested features
