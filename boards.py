#!/usr/bin/python
from __future__ import generators, unicode_literals
from PIL import Image, ImageFilter

class Board:

    firefighters = {}
    hazards = {}
    # pois = {}
    # links = {}
    # vehicles = {}

    def __init__(self, name):
        self.name = name

    def add_firefighter(self, firefighter):
        self.firefighters[firefighter.role.lower()] = firefighter

    def get_firefighter(self, role):
        return self.firefighters[role.lower()]

    def add_hazard(self, hazard):
        self.hazards[hazard.id] = hazard

    def get_hazard(self, id):
        return self.hazards[id]

    # def add_poi(self, poi):
    #     self.pois[poi.id] = poi
    #
    # def add_link(self, link):
    #     self.links[link.id] = link
    #
    # def add_vehicle(self, vehicle):
    #     self.vehicles[vehicle.id] = vehicle

    def draw(self):
        self.image = Image.open( "assets/maps/{}.jpg".format(self.name) )

        for hazard in self.hazards.itervalues():
            hazard.draw(self)

        for firefighter in self.firefighters.itervalues():
            firefighter.draw(self)

        self.image.save('output/output.jpg', 'JPEG')

    def translateRed(self, red):
        return red

    def translateBlack(self, black):
        return black

class StandardBoard(Board):

    ORIGIN_RED = 0
    ORIGIN_BLACK = 252
    TILE_WIDTH = 220
    TILE_HEIGHT = 220
    TILE_BORDER = 4

    def __init__(self):
        Board.__init__(self, "standard")

    def translateRed(self, red):
        red = self.ORIGIN_RED + (red * (self.TILE_BORDER + self.TILE_HEIGHT)) + (self.TILE_HEIGHT/2)
        return Board.translateRed(self, red)

    def translateBlack(self, black):
        black = self.ORIGIN_BLACK + (black * (self.TILE_BORDER + self.TILE_HEIGHT)) + (self.TILE_HEIGHT/2)
        return Board.translateBlack(self, black)
