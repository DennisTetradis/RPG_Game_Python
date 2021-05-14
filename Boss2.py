from Actor import Actor
import random


class Boss2(Actor):
    def __init__(self, position=0, name="Death Eater", health=300, character="ↈ"):
        super().__init__(position, health, character, name)

    def simpleAttack(self):
        return random.randrange(60, 100)

    def resetEnemy(self):
        self.health = 100
