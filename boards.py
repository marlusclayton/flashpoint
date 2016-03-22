#!/usr/bin/python
from __future__ import generators, unicode_literals
from PIL import Image, ImageFilter

class Board:

    available_pois = {"victim":10, "false_alarm":5}
    firefighters = {}
    hazards = {}
    pois = {}
    links = {}
    # vehicles = {}

    def __init__(self, name, side):
        self.name = name
        self.side = side

    def add_firefighter(self, firefighter):
        self.firefighters[firefighter.role.lower()] = firefighter

    def get_firefighter(self, role):
        return self.firefighters[role.lower()]

    def add_hazard(self, hazard):
        if not (self.hazards.has_key(hazard.key)):
            self.hazards[hazard.key] = hazard

    def get_hazard(self, id):
        return self.hazards[id]

    def add_poi(self, poi):
        remaining = self.available_pois[poi.entity_type]
        if (remaining > 0):
            self.available_pois[poi.entity_type] = remaining - 1
            self.pois[poi.key] = poi

    def add_link(self, link):
        self.links[link.key] = link

    # def add_vehicle(self, vehicle):
    #     self.vehicles[vehicle.key] = vehicle

    def move_firefighter(self, role, direction):
        firefighter = get_firefighter(role)

#    def get_new_coord(self, red, black, direction):


    def draw(self):
        self.image = Image.open( "assets/maps/{}_{}.jpg".format(self.name, self.side) )

        for link in self.links.itervalues():
            link.draw(self)

        for hazard in self.hazards.itervalues():
            hazard.draw(self)

        for poi in self.pois.itervalues():
            poi.draw(self)

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

    def __init__(self, side):
        Board.__init__(self, "standard", side)

    def translateRed(self, red):
        red = self.ORIGIN_RED + (red * (self.TILE_BORDER + self.TILE_HEIGHT)) + (self.TILE_HEIGHT/2)
        return Board.translateRed(self, red)

    def translateBlack(self, black):
        black = self.ORIGIN_BLACK + (black * (self.TILE_BORDER + self.TILE_HEIGHT)) + (self.TILE_HEIGHT/2)
        return Board.translateBlack(self, black)
