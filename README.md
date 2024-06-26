# 👻 Ghostbusters Game

## 📜 Overview

The Ghostbusters Game is a text-based adventure where you play as a ghostbuster. You fight ghosts, collect supplies, and level up. The game saves your progress, allowing you to continue from where you left off.

## 📑 Table of Contents

- [📜 Overview](#overview)
- [🔧 Installation](#installation)
- [🚀 Usage](#usage)
- [🧍 Player Class](#player-class)
- [📊 Level Class](#level-class)
- [🎮 Game Class](#game-class)
- [💾 Database Class](#database-class)
- [📝 Main Script](#main-script)

## 🔧 Installation

### 📋 Prerequisites

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### 📝 Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/Schadre/ghostbusters-game.git
    ```

2. Navigate to the project directory:

    ```sh
    cd ghostbusters-game
    ```

## 🚀 Usage

1. Navigate to the project directory (if not already there):

    ```sh
    cd ghostbusters-game
    ```

2. Run the game:

    ```sh
    python main.py
    ```

3. Follow the on-screen instructions to play the game.

## 🧍 Player Class

### `player.py`

The `Player` class manages the player's state, including health, level, and inventory.

### Methods

- `__init__(self, name, health=100, level=1, inventory=None)`: Initializes a new Player object.
- `take_damage(self, amount)`: Reduces player's health by the specified amount.
- `is_alive(self)`: Checks if the player is still alive (health > 0).
- `heal(self, amount)`: Increases player's health by the specified amount, up to a maximum of 100.
- `next_level(self)`: Moves the player to the next level.
- `add_to_inventory(self, item)`: Adds an item to the player's inventory.
- `use_item(self)`: Uses an item from the inventory, which heals the player.
- `show_inventory(self)`: Displays the player's inventory.
- `to_dict(self)`: Converts the player's state to a dictionary.
- `from_dict(cls, data)`: Creates a Player object from a dictionary.

## 📊 Level Class

### `level.py`

The `Level` class handles the choices presented to the player at each level.

### Methods

- `__init__(self, level_number)`: Initializes a new Level object with the specified level number.
- `present_choices(self)`: Presents choices to the player at this level and returns the chosen action.

## 🎮 Game Class

### `game.py`

The `Game` class runs the main game loop, processes player choices, and updates the player's state.

### Methods

- `__init__(self, player)`: Initializes a new Game object with the player and predefined jokes and supplies.
- `play(self)`: Starts and runs the game.
- `process_choice(self, choice)`: Processes the player's choice.
- `search_for_supplies(self)`: Handles searching for supplies.
- `tell_joke(self)`: Tells a random ghost joke.

## 💾 Database Class

### `database.py`

The `Database` class saves and loads the player's progress using SQLite.

### Methods

- `__init__(self, db_name="game_save.db")`: Initializes a new Database object and connects to the SQLite database.
- `create_table(self)`: Creates the player table if it doesn't already exist.
- `save_game(self, player)`: Saves the player's state to the database.
- `load_game(self, player_name)`: Loads the most recent saved game for a player.

## 📝 Main Script

### `main.py`

The main script starts the game and handles player input for saving/loading.

### Functions

- `display_logo()`: Displays the game logo.
- `main()`: The main function to start the game.

### Usage

1. The script initializes the database and displays the game logo.
2. It asks the user to enter their name.
3. The user can choose to continue from their last save or start a new game.
4. Based on the user's choice, the script either loads the saved game or creates a new player.
5. The game loop starts, allowing the player to make choices and progress through levels.
6. After the game loop ends, the user can choose to save their game.