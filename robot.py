from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_weapon = Weapon('CannonBlaster', 35)

    def attack(self, dinosaur):
        dinosaur.health -= self.attack_weapon.attack_power
        print(f'{self.name} is attacking {dinosaur.name} with {self.attack_weapon.name} for {self.attack_weapon.attack_power} damage leaving {dinosaur.name} with {dinosaur.health} health remaining')
