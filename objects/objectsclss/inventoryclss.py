class EntityInventory(object):
    inventoryFood = []
    inventorySwords = []
    inventoryPotions = []
    inventoryMaterials = []
    inventory = {'Food': inventoryFood, 'Swords': inventorySwords, 'Potions': inventoryPotions, 'Materials': inventoryMaterials}
    def __init__(self):
        pass
    
    def addFood(self, food):
        self.inventoryFood.append(food)
        
    def addSword(self, sword):
        self.inventorySwords.append(sword)
        
    def addPotion(self, potion):
        self.inventoryPotions.append(potion)
    
    def addMaterial(self, material):
        self.inventoryMaterials.append(material)
        
    def removeFood(self, food):
        self.inventoryFood.remove(food)
        
    def removeSword(self, sword):
        self.inventorySwords.remove(sword)
        
    def removePotion(self, potion):
        self.inventoryPotions.remove(potion)
        
    def removeMaterial(self, material):
        self.inventoryMaterials.remove(material)
        
    def getInventory(self):
        return self.inventory
            



