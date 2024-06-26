import random
from .player import Player
from .level import Level

class Game:
    def __init__(self, player):
        self.player = player
        self.jokes = [
            "Why did the ghost go to the party? Because he heard it was going to be a boo-l!",
            "What do you call a ghost's true love? Their ghoul-friend!",
            "Why do ghosts like to ride in elevators? It raises their spirits!",
            "How do ghosts keep fit? By exorcising regularly!",
            "Why are ghosts bad at lying? Because you can see right through them!"
        ]
        self.supplies = [
            "Proton Pack",
            "Ghost Trap",
            "PKE Meter",
            "Ecto Goggles",
            "Ghost Snare"
        ]

    def play(self):
        while self.player.level <= 15 and self.player.is_alive():
            current_level = Level(self.player.level)
            choice = current_level.present_choices()
            self.process_choice(choice)
            if not self.player.is_alive():
                print("Oops! The ghosts got you. Game Over!")
                break
        if self.player.level > 15:
            print("Congratulations! You've busted all the ghosts and completed all levels!")

    def process_choice(self, choice):
        if choice == 1:
            self.player.take_damage(20)
            print(f"Fought a ghost and took some ectoplasmic damage. Health is now {self.player.health}.")
            if self.player.is_alive():
                self.player.next_level()
        elif choice == 2:
            self.search_for_supplies()
        elif choice == 3:
            print("Resting... Don't let the bedbugs (or ghosts) bite!")
        elif choice == 4:
            self.tell_joke()
        elif choice == 5:
            self.player.show_inventory()
        elif choice == 6:
            self.player.use_item()
        else:
            print("Invalid choice. Try again.")

    def search_for_supplies(self):
        supply = random.choice(self.supplies)
        self.player.add_to_inventory(supply)
        self.player.heal(10)
        print(f"Found a {supply}. Health is now {self.player.health}.")

    def tell_joke(self):
        joke = random.choice(self.jokes)
        print(joke)

"""
Imports: The random module is used for random selections, 
and the Player and Level classes are imported from their respective modules(within the ghostbusters_game folder).

Game Class: Manages the main game logic, including player actions and level progression.

Initialization: Sets up the player, jokes, and supplies.

Play Method: Runs the main game loop, presenting choices and processing actions.

Process Choice Method: Handles the logic for each player choice.

Search for Supplies Method: Adds a random supply to the player's inventory and heals the player.

Tell Joke Method: Tells a random joke to the player.

This Game class ties everything together, managing the flow of the game and the interactions 
between the player and the levels.
"""
