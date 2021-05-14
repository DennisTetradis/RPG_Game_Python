from Actor import Actor
import random


class Mage(Actor):
    def __init__(self, position, name, health=100, character="Ⓜ"):
        super().__init__(position, health, character, name)

    def fireBall(self):
        return random.randrange(20, 29)

    def iceFire(self):
        return random.randrange(60, 80)
