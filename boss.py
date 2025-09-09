from enemy import Enemy
import random

class BossMan(Enemy):
    """
    This is our goblin blueprint 
    """
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.attack_power = random.randint(20, 25)
    
    def attack(self):
        self.attack_power =  random.randint(25, 35)

    def Special(self):
        if self.health < 60:
            roll = random.randint(1,5)
            if roll == 3:
                self.attack_power = 25

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0



