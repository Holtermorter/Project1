from gameDependencies.imports import *
from objects.objectsclss.inventoryclss import EntityInventory
from objects.objectsclss.entityclss import EntityNPC
from objects.objectsclss.foodclss import Food
print("Wellcome to the game!!")

inventory = EntityInventory()

inventory.addFood(Food("Apple", 1, 1))
print("You have an inventory with the following items: ", inventory.getInventory())

