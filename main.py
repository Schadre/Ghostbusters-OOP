from ghostbusters_game.database import Database
from ghostbusters_game.player import Player
from ghostbusters_game.game import Game

def display_logo():
    logo = """
                       __---__
                    _-       _--______
               __--( /     \\ )XXXXXXXXXXXXX_
             --XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\\
          /XXXXX(              )--_  XXXXXXXXXXX\\
         /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\
         XXXXX/   /            XXXXXX   \\__ \\XXXXX----
         XXXXXX__/          XXXXXX         \\__----  -
 ---___  XXX__/          XXXXXX      \\__         ---
   --  --__/   ___/\\  XXXXXX            /  ___---=
     -_    ___/    XXXXXX              '--- XXXXXX
       --\\/XXX\\ XXXXXX                      /XXXXX
         \\XXXXXXXXX                        /XXXXX/
          \\XXXXXX                        _/XXXXX/
            \\XXXXX--__/              __-- XXXX/
             --XXXXXXX---------------  XXXXX--
                \\XXXXXXXXXXXXXXXXXXXXXXXX-
                  --XXXXXXXXXXXXXXXXXX-
    """
    print(logo)

def main():
    db = Database()
    display_logo()
    player_name = input("Enter your name, brave Ghostbuster: ")
    
    while True:
        choice = input("Do you want to (1) continue from your last save or (2) start a new game? Enter 1 or 2: ")
        if choice == "1":
            saved_player = db.load_game(player_name)
            if saved_player:
                player = saved_player
                print(f"Welcome back, {player.name}! Let's continue busting ghosts.")
                break
            else:
                print("No saved game found. Starting a new game.")
                player = Player(player_name)
                break
        elif choice == "2":
            player = Player(player_name)
            print(f"Get ready, {player.name}, your ghostbusting adventure begins now!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    game = Game(player)
    game.play()

    save = input("Do you want to save your game? (yes/no): ")
    if save.lower() == "yes":
        db.save_game(player)
        print("Your progress has been saved. See you next time!")

if __name__ == "__main__":
    main()


"""
Imports: Brings in necessary classes from the ghostbusters_game package.

Display Logo: Prints the game logo.

Main Function:
Initializes the database.
Displays the logo.
Ask the player for their name.
Asks the player if they want to continue from their last save or start a new game.
Loads the saved game or creates a new player based on the player's choice.
Starts the game loop.
Ask the player to save their game after playing.


Entry Point: Ensures the main function runs when the script is executed directly.
This script ties everything together, managing the overall flow of the game, handling user input,
and ensuring the player's progress can be saved and loaded.
"""