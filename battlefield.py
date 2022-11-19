from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot1 = Robot('The Terminator')
        self.dinosaur1 = Dinosaur('Rex', 45)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nLets settle this once and for all\n🦖!ROBOTS VS DINOSAURS!🤖\n')
    
    def battle_phase(self):
        while self.dinosaur1.health > 0 and self.robot1.health > 0:
            self.robot1.attack(self.dinosaur1)
            if self.dinosaur1.health > 0:
                self.dinosaur1.attack(self.robot1)
        
    def display_winner(self):
        if self.robot1.health <= 0:
            print(f'{self.dinosaur1.name} deactivated {self.robot1.name}\n🦖')
        elif self.dinosaur1.health <= 0:
            print(f'{self.robot1.name} mauled {self.dinosaur1.name}\n🤖')
