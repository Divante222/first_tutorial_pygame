import random

# Player class
class Player:
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.damage = damage

    def attack(self, target):
        damage = random.randint(1, self.damage)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def heal(self):
        heal_amount = random.randint(1, 10)
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount} health.")

# Enemy class
class Enemy:
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.damage = damage

    def attack(self, target):
        damage = random.randint(1, self.damage)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

# Game loop
def game_loop():
    player = Player("Player", 20, 5)
    enemy = Enemy("Goblin", 10, 3)

    print("Welcome to the RPG game! You will battle a goblin!")
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name}: {player.health} health")
        print(f"{enemy.name}: {enemy.health} health")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.attack(enemy)
            if not enemy.is_alive():
                print("You have defeated the goblin!")
        elif choice == "2":
            player.heal()
        else:
            print("Invalid choice.")

        if enemy.is_alive():
            enemy.attack(player)
            if not player.is_alive():
                print("You have been defeated!")

    print("Game over.")

# Start the game
game_loop()