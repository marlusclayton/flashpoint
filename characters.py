#!/usr/bin/python
from __future__ import generators
from PIL import Image, ImageFilter

class Character(object):

    roles = ["cafs_firefighter", "driver", "fire_captain", "generalist", "hazmat_technician", "imaging_technician", "paramedic", "rescue_dog", "rescue_specialist", "structural_engineer", "veteran", "standard"]
    colors = ["blue", "green", "orange", "red", "white", "yellow"]

    def __init__(self, role, color):
        self.role = role
        self.color = color
        self.width = 120
        self.height = 120
        self.red = 0
        self.offsetRed = self.height/2
        self.black = 0
        self.offsetBlack = self.width/2
        self.image = Image.open("assets/characters/{}_{}.png".format(self.role, self.color)).resize((self.width,self.height))

    def factory(type, color):
        if type == "cafs_firefighter": return CAFS(color)
        if type == "driver": return Driver(color)
        if type == "fire_captain": return Captain(color)
        if type == "generalist": return Generalist(color)
        if type == "hazmat_technician": return Hazmat(color)
        if type == "imaging_technician": return Imaging(color)
        if type == "paramedic": return Paramedic(color)
        if type == "rescue_dog": return Dog(color)
        if type == "rescue_specialist": return Rescue(color)
        if type == "structural_engineer": return Engineer(color)
        if type == "veteran": return Veteran(color)
        return Standard(color)
        assert 0, "Bad creation: " + type
    factory = staticmethod(factory)

class CAFS(Character):
    def __init__(self, color):
        Character.__init__(self, "cafs_firefighter", color)

class Driver(Character):
    def __init__(self, color):
        Character.__init__(self, "driver", color)

class Captain(Character):
    def __init__(self, color):
        Character.__init__(self, "fire_captain", color)

class Generalist(Character):
    def __init__(self, color):
        Character.__init__(self, "generalist", color)

class Hazmat(Character):
    def __init__(self, color):
        Character.__init__(self, "hazmat_technician", color)

class Imaging(Character):
    def __init__(self, color):
        Character.__init__(self, "imaging_technician", color)

class Paramedic(Character):
    def __init__(self, color):
        Character.__init__(self, "paramedic", color)

class Dog(Character):
    def __init__(self, color):
        Character.__init__(self, "rescue_dog", color)

class Rescue(Character):
    def __init__(self, color):
        Character.__init__(self, "rescue_specialist", color)

class Standard(Character):
    def __init__(self, color):
        Character.__init__(self, "standard", color)

class Engineer(Character):
    def __init__(self, color):
        Character.__init__(self, "structural_engineer", color)

class Veteran(Character):
    def __init__(self, color):
        Character.__init__(self, "veteran", color)
