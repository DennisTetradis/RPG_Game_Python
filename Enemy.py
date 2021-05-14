from Actor import Actor
import random


class Enemy(Actor):
    def __init__(self, position=0, name="minion", health=100, character="ௐ"):
        super().__init__(position, health, character, name)

    def simpleAttack(self):
        return random.randrange(10, 15)

    def resetEnemy(self):
        self.health = 100
