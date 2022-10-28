# -*- coding: utf-8 *-*
from os import name
from turtle import stamp


class EntityNPC:
    entityEstatus = True
    def __init__(self, _name, _raze, _health, _stamina, _magic, _inteligence):
        self.name = _name
        self.raze = _raze
        self.healht = _health
        self.stamina = _stamina
        self.magic = _magic
        self.inteligence = _inteligence

    def hit(self, _damage):
        self.healht -= _damage
        Entity.check()

    def heal(self, _ammount):
        self.healht += _ammount
        Entity.check()

    def check(self):
        if self.healht <= 0:
            self.healht = 0
            entityEstatus = False

        if self.stamina <= 0:
            self.stamina = 0
            print("Sin estamina")

        if self.magic <= 0:
            self.magic = 0
            print("Sin magia")

    def info(self):
        print("\n--------------------------------------------------------------\n")
        print("Datos de", self.name + ":")
        print("Vida:", self.healht)
        print("Stamina:", self.stamina)
        print("Magia:", self.magic)
        print("Inteligencia:", self.inteligence)
        print("\n______________________________________________________________\n")




