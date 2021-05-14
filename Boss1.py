from Actor import Actor
import random


class Boss1(Actor):
    def __init__(self, position=0, name="Viper", health=150, character="⏀"):
        super().__init__(position, health, character, name)

    def simpleAttack(self):
        return random.randrange(30, 50)

    def resetEnemy(self):
        self.health = 100