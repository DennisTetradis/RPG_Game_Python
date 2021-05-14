from Actor import Actor
import random


class Enemy2(Actor):
    def __init__(self, position=0, name="minion", health=130, character="ௐ"):
        super().__init__(position, health, character, name)

    def simpleAttack(self):
        return random.randrange(30, 50)

    def resetEnemy(self):
        self.health = 100
