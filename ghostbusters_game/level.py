class Level:
    def __init__(self, level_number):
        self.level_number = level_number

    def present_choices(self):
        print(f"\nWelcome to Level {self.level_number}! Prepare for ghostly encounters!")
        choices = {
            1: "Fight a ghost (costs 20 health)",
            2: "Search for supplies (gain 10 health)",
            3: "Rest (no effect)",
            4: "Tell a ghost joke (might confuse the ghost!)",
            5: "Check inventory",
            6: "Use item from inventory (gain 30 health)"
        }
        for key, value in choices.items():
            print(f"{key}: {value}")
        
        while True:
            try:
                choice = int(input("Choose an action: "))
                if choice in choices:
                    return choice
                else:
                    print("Invalid choice. Please choose a valid action.")
            except ValueError:
                print("Invalid input. Please enter a number corresponding to your choice.")

"""
Sets Up the Level: Remembers which level you’re on.

Shows a Welcome Message: Tells you the level you’re on.

Lists the Actions: Shows you what actions you can take, like fighting a ghost or resting.

Gets Your Choice: Asks you to pick an action and keeps asking until you choose a valid one.

This Level class helps make the game interactive by presenting choices to the player and 
processing their input to determine what happens next.
"""
