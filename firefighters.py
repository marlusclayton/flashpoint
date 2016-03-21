#!/usr/bin/python
from __future__ import generators, unicode_literals
from entities import Entity

class Firefighter(Entity):

    # ROLES = ["cafs_firefighter", "driver", "fire_captain", "generalist", "hazmat_technician", "imaging_technician", "paramedic", "rescue_dog", "rescue_specialist", "structural_engineer", "veteran", "standard"]

    def __init__(self, role, player, red, black):
        Entity.__init__(self, role, red, black)
        self.set_player(player)
        self.role = role
        self.image_name = "assets/firefighters/{}_{}.png".format(self.role, self.player.color)

    @staticmethod
    def factory(role, player, red, black):
        if role == "cafs_firefighter": return CAFS(player, red, black)
        if role == "driver": return Driver(player, red, black)
        if role == "fire_captain": return Captain(player, red, black)
        if role == "generalist": return Generalist(player, red, black)
        if role == "hazmat_technician": return Hazmat(player, red, black)
        if role == "imaging_technician": return Imaging(player, red, black)
        if role == "paramedic": return Paramedic(player, red, black)
        if role == "rescue_dog": return Dog(player, red, black)
        if role == "rescue_specialist": return Rescue(player, red, black)
        if role == "structural_engineer": return Engineer(player, red, black)
        if role == "veteran": return Veteran(player, red, black)
        return Standard(player)

    def set_player(self, player):
        self.player = player

class CAFS(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "cafs_firefighter", player, red, black)

class Driver(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "driver", player, red, black)

class Captain(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "fire_captain", player, red, black)

class Generalist(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "generalist", player, red, black)

class Hazmat(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "hazmat_technician", player, red, black)

class Imaging(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "imaging_technician", player, red, black)

class Paramedic(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "paramedic", player, red, black)

class Dog(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "rescue_dog", player, red, black)

class Rescue(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "rescue_specialist", player, red, black)

class Standard(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "standard", player, red, black)

class Engineer(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "structural_engineer", player, red, black)

class Veteran(Firefighter):
    def __init__(self, player, red, black):
        Firefighter.__init__(self, "veteran", player, red, black)
