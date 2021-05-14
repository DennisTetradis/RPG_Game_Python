import sys
import random

from Mage import Mage
from Enemy import Enemy
from Enemy2 import Enemy2
from Warrior import Warrior
from Boss1 import Boss1
from Boss2 import Boss2


# Main menu screen!(Reads from MainMenu.txt)
# Breaks when you type play!
def mainMenu():
    with open("MainMenu.txt", "r") as f:
        print(f.read())
    while True:
        choice = input("-->")
        choice = choice.lower()
        if choice == "play":
            break
        elif choice == "help":
            print("Your objective is to defeat all bosses(kill some enemies first to sharpen your skills)")
        elif choice == "quit":
            exit()
        elif choice == "load":
            print("You can't save the game yet(coming soon)")


# Play button on main menu
def play():
    name = input('Type your name:')
    player_class = input("Type the class you want to choose:")
    return (name, player_class)


# Get's move input from player!
def moveInput():
    while True:
        print("Make a move(Up, right, left, down)")
        move = input("-->")
        move = move.lower()
        movation = ["up", "right", "left", "down"]
        if move in movation:
            print(move)
            break
        elif move == "mainmenu":
            mainMenu()
            break
        elif move == "exit":
            sys.exit(0)
        else:
            print("Invalid move!, please type again")

    return move


def buildMatrix(rows, cols, player, boss1):
    matrix = []
    potions = int(0.2 * rows)
    potion = 0
    enemies = int(0.4 * rows)
    enemy = 0
    bosses = int(0.1 * rows)
    boss = 0
    blocks = int(3.5 * rows)
    block = 0
    spikes = int(1 * rows)
    spike = 0
    player.setPosition([random.randrange(0, rows), random.randrange(0, cols)])

# Builds an empty 2D array
    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = " "
# Map generator
    while True:
        for i in range(rows):
            for j in range(cols):
                if random.randrange(0, (2 * rows)) == 0:
                    # Change the 20 to a higher value to make the map more random
                    if matrix[i][j] == " ":
                        if block < blocks:
                            matrix[i][j] = "ᛥ"
                            block += 1
                        elif spike < spikes:
                            matrix[i][j] = "˄"
                            spike += 1
                        elif enemy < enemies:
                            if boss1 == 1:
                                matrix[i][j] = "ௐ"
                            else:
                                matrix[i][j] = "ↁ"
                            enemy += 1
                        elif potion < potions:
                            matrix[i][j] = "⊕"
                            potion += 1
                        elif boss < bosses:
                            if boss1 == 1:
                                matrix[i][j] = "⏀"
                            else:
                                matrix[i][j] = "ↈ"
                            boss += 1
        if enemies == enemy and blocks == block and spikes == spike and potions == potion and bosses == boss:
            break
    return matrix, player


# Chose Class and Name (saves name in Mage class and Class in player variable)
def choseClass():
    print("Chose a class: Mage - Warrior")
    choice = input("-->")
    choice = choice.lower()
    while True:
        if choice == "mage":
            print("What's your name?")
            player = Mage([random.randrange(0, 30), random.randrange(0, 30)], input("-->"))
            power = Mage
            break
        elif choice == "warrior":
            print("What's your name?")
            player = Warrior([random.randrange(0, 30), random.randrange(0, 30)], input("-->"))
            power = Warrior
            break
    return (player, power)


# Prints Map on the screen
def printMapString(matrix):
    print("#|" * (len(matrix) + 3))
    for i in range(len(matrix)):
        print("#| ", end="")
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print(" |#")
    print("#|" * (len(matrix) + 3))


def moveInMap(matrix, move, player, power, xp, boss1):
    position = player.getPosition()
    i = position[0]
    j = position[1]
    if move == "up":
        i -= 1
    elif move == "down":
        i += 1
    elif move == "right":
        j += 1
    elif move == "left":
        j -= 1
    if matrix[i][j] == "ᛥ":
        print("You can't go that way")
    elif matrix[i][j] == " ":
        matrix[i][j] = player.character
        matrix[position[0]][position[1]] = " "
        player.setPosition([i, j])
    elif matrix[i][j] == "˄":
        player.takeDamage(15)
        print(player.getName(), ':', player.getHealth())
        matrix[i][j] = player.character
        matrix[position[0]][position[1]] = " "
        player.setPosition([i, j])
    elif matrix[i][j] == "ௐ":
        enemy = Enemy()
        player, xp= battle(player, enemy, power, xp)
        matrix[i][j] = player.character
        matrix[position[0]][position[1]] = " "
        player.setPosition([i, j])
    elif matrix[i][j] == "ↁ":
        enemy = Enemy2()
        player, xp= battle(player, enemy, power, xp)
        matrix[i][j] = player.character
        matrix[position[0]][position[1]] = " "
        player.setPosition([i, j])
    elif matrix[i][j] == "⊕":
        player.health = player.health + 20
        print(player.getName(), ':', player.getHealth())
        matrix[i][j] = player.character
        matrix[position[0]][position[1]] = " "
        player.setPosition([i, j])
    elif matrix[i][j] == "⏀":
        enemy = Boss1()
        player, xp = battle(player, enemy, power, xp)
        matrix[i][j] = player.character
        matrix[position[0]][position[1]] = " "
        player.setPosition([i, j])
        boss1 = 0
    elif matrix[i][j] == "ↈ":
        enemy = Boss2()
        player, xp = battle(player, enemy, power, xp)
        matrix[i][j] = player.character
        matrix[position[0]][position[1]] = " "
        player.setPosition([i, j])
        print('Good job you have beat this game!')
        exit()

    return matrix, player, xp, boss1

def printAttacks(power):
    print(power[26])
    print(power[30])

# There is no problem this shit works! Thank you programing. Fuck you
def battle(player, enemy, power, xp):
    while True:
        print("'Attacks:'")
        printAttacks(power)
        move = input("-->").lower()
        if move == "fireball":
            player.takeDamage(enemy.simpleAttack()/xp)
            enemy.takeDamage(player.fireBall()*xp)
        elif move == "icefire":
            player.takeDamage(enemy.simpleAttack()/xp)
            enemy.takeDamage(player.iceFire()*xp)
        elif move == "swordslash":
            player.takeDamage(enemy.simpleAttack()/xp)
            enemy.takeDamage(player.swordSlash()*xp)
        elif move == "firesword":
            player.takeDamage(enemy.simpleAttack()/xp)
            enemy.takeDamage(player.fireSword()*xp)
        else:
            print("Invalid attack")
        if enemy.getHealth() <= 0:
            enemy.resetEnemy()
            print("He dead, hohoho")
            xp += 0.2
            print('XP:', xp)
            break

        print(player.getName(), ':', player.getHealth())
        print(enemy.getName(), ':', enemy.getHealth(), '\n')
        if player.getHealth() <= 0:
            print('YOU ARE DEAD!')
            exit()
    return player, xp


# Sets player in the map(Runs only once at the start)
def setStartingPosition(matrix, player):
    position = player.getPosition()
    matrix[position[0]][position[1]] = player.character

def setMapSize():
    print('Choose map size(Small, Medium or Big:')
    choice = input("-->")
    choice = choice.lower()
    if choice == 'small':
        x = 14
        y = 14
    elif choice == 'medium':
        x = 17
        y = 17
    elif choice == 'big':
        x = 24
        y = 24
    return x, y

#choise = input('Choose a size: ex. 17X17 ')
xp = 1

boss1 = 1

mainMenu()

player, power = choseClass()

x, y = setMapSize()

matrix, player = buildMatrix(x, y, player, boss1)

power = dir(power)

setStartingPosition(matrix, player)

printMapString(matrix)

print("Welcome", player.getName(), ",to this RPG game!")

while True:
    matrix, player, xp, boss1 = moveInMap(matrix, moveInput(), player, power, xp, boss1)
    printMapString(matrix)
    if boss1 == 0:
        break

matrix, player = buildMatrix(x, y, player, boss1)

setStartingPosition(matrix, player)

printMapString(matrix)

while True:
    matrix, player, xp, boss1 = moveInMap(matrix, moveInput(), player, power, xp, boss1)
    printMapString(matrix)