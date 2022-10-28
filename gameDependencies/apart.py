

from objects.objectsclss.entityclss import EntityNPC
from objects.objectsclss.swordclss import Sword


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


javi = EntityNPC("j", "a", 2, 2, 2, 2,)
ebano = Sword(30, "Hoja de ebano", 100)






