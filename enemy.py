import random

class Enemy():
    """
    This is our goblin blueprint 
    
    """
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.attack_power = random.randint(5, 10)

    def attack(self):
        return random.randint(5, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

    