class Player:
    def __init__(self, name, health=100, level=1, inventory=None):
        self.name = name
        self.health = health
        self.level = level
        self.inventory = inventory if inventory is not None else []

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def next_level(self):
        self.level += 1

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"Picked up {item}. Inventory: {self.inventory}")

    def use_item(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return
        print("Select an item to use:")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}: {item}")
        while True:
            try:
                choice = int(input("Enter the number of the item to use: ")) - 1
                if 0 <= choice < len(self.inventory):
                    item = self.inventory.pop(choice)
                    self.heal(30)
                    print(f"Used {item}. Health is now {self.health}. Inventory: {self.inventory}")
                    break
                else:
                    print("Invalid choice. Please select a valid item.")
            except ValueError:
                print("Invalid input. Please enter the number corresponding to the item.")

    def show_inventory(self):
        print(f"Inventory: {self.inventory}")

    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'level': self.level,
            'inventory': self.inventory
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['name'], health=data['health'], level=data['level'], inventory=data['inventory'])

"""
Initialization: Sets up the player's name, health, level, and inventory.

Take Damage: Reduces the player's health.

Check if Alive: Checks if the player is still alive.

Heal: Increases the player's health.

Next Level: Increases the player's level.

Add to Inventory: Adds an item to the player's inventory.

Use Item: Allows the player to use an item from their inventory to heal.

Show Inventory: Displays the player's inventory.

Convert to Dictionary: Converts the player's state to a dictionary.

Create from Dictionary: Creates a Player object from a dictionary.

The Player class manages everything about the player, from their health 
and level to the items they collect and use.

"""