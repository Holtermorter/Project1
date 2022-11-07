from gameDependencies.imports import *

print("Wellcome to the game!!")

inventory = EntityInventory()

inventory.addFood(Food("Apple", 1, 1))
print("You have an inventory with the following items: ", inventory.getInventory())

