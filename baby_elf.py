from enemy import Enemy

class baby_elf(Enemy):
    def cry():
        print("grrrrr whhhhh")

def take_damage(self, damage):
    print("Why? Monster...")
    return super().take_damage(damage)