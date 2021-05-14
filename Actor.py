class Actor:
    # format: [x, y]
    position = []

    def __init__(self, position, health, character, name):
        self.name = name
        self.character = character
        self.health = health
        self.position = position

    def takeDamage(self, damage):
        self.health -= damage

    def getHealth(self):
        return self.health

    def getPosition(self):
        return self.position

    def setPosition(self, new_position):
        self.position = new_position

    def getName(self):
        return self.name

