#create a class for food with the atributes for the name, durability, satiety and the status of the object.



class Food:
    def __init__(self, name, durability, satiety):
        self.name = name
        self.durability = durability
        self.satiety = satiety
        self.status = True
        self.eaten = False
    #create a function to change the status of Food to False if the durability is 0 or eaten is True
    def change_status(self):
        if self.durability == 0 or self.eaten == True:
            self.status = False
    
    def eat():
        if self.status == True:
            self.eaten = True
            self.durability -= 1
            self.change_status()
        else:
            print("You can't eat that!")
            
    def foodInfo():
        print("Name: ", self.name)
        print("Durability: ", self.durability)
        print("Satiety: ", self.satiety)
        print("Status: ", self.status)
        print("Eaten: ", self.eaten)
