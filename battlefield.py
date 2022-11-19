from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot1 = Robot('Terminator')
        self.dinosaur1 = Dinosaur('Rex', 35)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):

        print('\nWelcome to an epic battle for the ages!\nOnly one side can win!\n')
    
    def battle_phase(self):
        while self.dinosaur1.health > 0 and self.robot1.health > 0:
            self.robot1.attack(self.dinosaur1)
            if self.dinosaur1.health > 0:
                self.dinosaur1.attack(self.robot1)
        
    def display_winner(self):
        if self.robot1.health <= 0:
            print(f'{self.dinosaur1.name} deactivated {self.robot1.name}')
        elif self.dinosaur1.health <= 0:
            print(f'{self.robot1.name} mauled {self.dinosaur1.name}')
