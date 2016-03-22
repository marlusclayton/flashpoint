#!/usr/bin/python
from __future__ import generators, unicode_literals
from entities import Entity

class POI(Entity):

    def __init__(self, poi_type, red, black):
        Entity.__init__(self, poi_type, red, black)
        self.width = 90
        self.height = 90
        self.offsetRed = self.height/2
        self.offsetBlack = self.width/2

        self.conceal()

    @staticmethod
    def factory(poi_type, red, black):
        if poi_type == "victim":      return Victim(red, black)
        if poi_type == "false_alarm": return FalseAlarm(red, black)

    def reveal(self):
        self.revealed = True

    def conceal(self):
        self.revealed = False

    def get_image_name(self):
        self.image_name = "assets/POIs/{}.png".format(self.entity_type) if self.revealed else "assets/POIs/poi.png"
        return self.image_name

class Victim(POI):
    def __init__(self, red, black):
        POI.__init__(self, "victim", red, black)

class FalseAlarm(POI):
    def __init__(self, red, black):
        POI.__init__(self, "false_alarm", red, black)
