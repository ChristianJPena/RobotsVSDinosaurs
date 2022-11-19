class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):   # reminder of what is happening here
        robot.health -= self.attack_power
        print(f'{robot.name} health remaning {robot.health}')
    
