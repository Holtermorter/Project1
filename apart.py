from gameDatas.objects import *
from gameDatas.objects.objectsclss.entityclss import EntityNPC


def playerCreation():
    name = input("Indique un nombre para su personaje: ")

    raze = input("Indique una raza para su personaje: ")

    if raze:
        if raze == "Human":
            player = EntityNPC(name, raze, 100, 200, 50, 10)
        elif raze == "Orc":
            player = EntityNPC(name, raze, 200, 100, 10, 10)
        elif raze == "Elf":
            player = EntityNPC(name, raze, 100, 200, 75, 50)
        elif raze == "Dwarf":
            player = EntityNPC(name, raze, 400, 100, 0, 5)
        else:
            print("Raza incorrecta")







