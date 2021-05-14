from Actor import Actor
import random


class Warrior(Actor):
    def __init__(self, position, name, health=150, character="֎"):
        super().__init__(position, health, character, name)

    def swordSlash(self):
        return random.randrange(10, 25)

    def fireSword(self):
        return random.randrange(40, 55)