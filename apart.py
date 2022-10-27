import objects

atributes = {'health': 0, 'stamina': 0, 'name': 0}

def entityName():
    atributes['name'] = input("Username: ")

def raze():
    entityRaze = input()
    if entityRaze:
        if entityRaze == "Orc":
            atributes['health'] = 100
            atributes['stamina'] = 200
        
        elif entityRaze == "Human":
            atributes['health'] = 150
            atributes['stamina'] = 100
        elif
        else:
            print("ERROR")
