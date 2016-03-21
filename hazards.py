#!/usr/bin/python
from __future__ import generators, unicode_literals
from entities import Entity

class Hazard(Entity):

    def __init__(self, hazard_type, red, black):
        Entity.__init__(self, hazard_type, red, black)
        self.image_name = "assets/tokens/{}.png".format(self.entity_type)

    @staticmethod
    def factory(hazard_type, red, black):
        if hazard_type == "smoke":    return Smoke(red, black)
        if hazard_type == "fire":     return Fire(red, black)
        if hazard_type == "hazmat":   return Hazmat(red, black)
        if hazard_type == "hot_spot": return HotSpot(red, black)

class Smoke(Hazard):
    def __init__(self, red, black):
        Hazard.__init__(self, "smoke", red, black)

class Fire(Hazard):
    def __init__(self, red, black):
        Hazard.__init__(self, "fire", red, black)

class Hazmat(Hazard):
    def __init__(self, red, black):
        Hazard.__init__(self, "hazmat", red, black)

class HotSpot(Hazard):
    def __init__(self, red, black):
        Hazard.__init__(self, "hot_spot", red, black)
        self.width = 60
        self.height = 60
        self.offsetRed = self.height+40
        self.offsetBlack = self.width+40
