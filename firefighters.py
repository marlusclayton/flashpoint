#!/usr/bin/python
from __future__ import generators, unicode_literals
from PIL import Image, ImageFilter

class Firefighter(object):

    ROLES = ["cafs_firefighter", "driver", "fire_captain", "generalist", "hazmat_technician", "imaging_technician", "paramedic", "rescue_dog", "rescue_specialist", "structural_engineer", "veteran", "standard"]
    COLORS = ["blue", "green", "orange", "red", "white", "yellow"]

    def __init__(self, role, player):
        self.set_player(player)

        self.role = role
        self.width = 120
        self.height = 120
        self.offsetRed = self.height/2
        self.offsetBlack = self.width/2
        self.image = Image.open("assets/firefighters/{}_{}.png".format(self.role, self.player.color)).resize((self.width,self.height))

    @staticmethod
    def factory(role, player):
        if role == "cafs_firefighter": return CAFS(player)
        if role == "driver": return Driver(player)
        if role == "fire_captain": return Captain(player)
        if role == "generalist": return Generalist(player)
        if role == "hazmat_technician": return Hazmat(player)
        if role == "imaging_technician": return Imaging(player)
        if role == "paramedic": return Paramedic(player)
        if role == "rescue_dog": return Dog(player)
        if role == "rescue_specialist": return Rescue(player)
        if role == "structural_engineer": return Engineer(player)
        if role == "veteran": return Veteran(player)
        return Standard(player)

    def set_position(self, red, black):
        self.red = red
        self.black = black

    def set_player(self, player):
        self.player = player

class CAFS(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "cafs_firefighter", player)

class Driver(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "driver", player)

class Captain(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "fire_captain", player)

class Generalist(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "generalist", player)

class Hazmat(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "hazmat_technician", player)

class Imaging(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "imaging_technician", player)

class Paramedic(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "paramedic", player)

class Dog(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "rescue_dog", player)

class Rescue(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "rescue_specialist", player)

class Standard(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "standard", player)

class Engineer(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "structural_engineer", player)

class Veteran(Firefighter):
    def __init__(self, player):
        Firefighter.__init__(self, "veteran", player)
