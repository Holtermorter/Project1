

from objects.objectsclss.entityclss import EntityNPC
from objects.objectsclss.foodsclss import Food
from objects.objectsclss.swordclss import Sword
inventoryFood = []
inventory = {'Food': inventoryFood,}

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


def eatHeal(food):
    if food in inventory:
        if food.status == True:
            player.heal(food.satiety)
            food.eaten = True
            food.durability -= 1
            food.change_status()
        else:
            print("You can't eat that!")
            
def addToInventory(item):
    if item is Food:
        inventoryFood.append(item)
        inventory['Food'] = inventoryFood
    elif item is Sword:
        inventory.append(item)
    else:
        print("Error in inventoryADD")


    






