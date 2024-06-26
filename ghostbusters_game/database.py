import sqlite3
import json
from .player import Player

class Database:
    def __init__(self, db_name="game_save.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS player (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    health INTEGER,
                    level INTEGER,
                    inventory TEXT
                   )"""
        self.conn.execute(query)
        self.conn.commit()

    def save_game(self, player):
        query = "INSERT INTO player (name, health, level, inventory) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (player.name, player.health, player.level, json.dumps(player.inventory)))
        self.conn.commit()

    def load_game(self, player_name):
        query = "SELECT * FROM player WHERE name = ? ORDER BY id DESC LIMIT 1"
        cursor = self.conn.execute(query, (player_name,))
        row = cursor.fetchone()
        if row:
            return Player(name=row[1], health=row[2], level=row[3], inventory=json.loads(row[4]))
        else:
            return None


""" 
Imports: The necessary modules and classes are imported.
[sqlite3: Provides the functionality to interact with an SQLite database, 
allowing you to create, read, update, and delete records.
json: Provides functionality to convert Python objects to JSON strings and vice versa, 
facilitating the storage and retrieval of complex data structures like lists in the database.
Player: Represents the player in the game, managing their state (name, health, level, and inventory). 
The import allows the Database class to create Player objects when loading game data from the database.]

Database Class: This class handles all database operations.

Constructor: Initializes the database connection and creates the table if it doesn't exist.

create_table: Ensures the player table exists in the database.

save_game: Saves the player's game data to the database.

load_game: Loads the player's most recent game data from the database.

This class allows the game to save and load player progress using a SQLite database, 
ensuring the player's progress is stored and can be retrieved later.
"""