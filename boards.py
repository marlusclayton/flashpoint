#!/usr/bin/python
from __future__ import generators, unicode_literals
from PIL import Image

class Board(object):

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
        if not self.hazards.has_key(hazard.key):
            self.hazards[hazard.key] = hazard

    def get_hazard(self, key):
        return self.hazards[key]

    def add_poi(self, poi):
        remaining = self.available_pois[poi.entity_type]
        if remaining > 0:
            self.available_pois[poi.entity_type] = remaining - 1
            self.pois[poi.key] = poi

    def add_link(self, link):
        self.links[link.key] = link

    def get_entities_at(self, red, black, *args):
        result = []

        for link in self.links.itervalues():
            if link.red == red and link.black == black:
                if link.red_link == args[0] and link.black_link == args[1]:
                    result.append(link)

        for hazard in self.hazards.itervalues():
            if hazard.red == red and hazard.black == black:
                result.append(hazard)

        for poi in self.pois.itervalues():
            if poi.red == red and poi.black == black:
                result.append(poi)

        for firefighter in self.firefighters.itervalues():
            if firefighter.red == red and firefighter.black == black:
                result.append(firefighter)

        return result

    # def add_vehicle(self, vehicle):
    #     self.vehicles[vehicle.key] = vehicle

    def move_firefighter(self, role, direction):
        firefighter = self.get_firefighter(role)
        red, black = self.get_new_coord(firefighter.red, firefighter.black, direction)
        firefighter.red = red
        firefighter.black = black

    def get_new_coord(self, red, black, direction):
        return (red, black) if direction else (black, red)

    def draw(self):
        image = Image.open("assets/maps/{}_{}.jpg".format(self.name, self.side))

        for link in self.links.itervalues():
            link.draw(self)

        for hazard in self.hazards.itervalues():
            hazard.draw(self)

        for poi in self.pois.itervalues():
            poi.draw(self)

        for firefighter in self.firefighters.itervalues():
            firefighter.draw(self)

        image.save('output/output.jpg', 'JPEG')

    def translate_red(self, red):
        return red

    def translate_black(self, black):
        return black

class StandardBoard(Board):

    ORIGIN_RED = 0
    ORIGIN_BLACK = 252
    TILE_WIDTH = 220
    TILE_HEIGHT = 220
    TILE_BORDER = 4

    def __init__(self, side):
        Board.__init__(self, "standard", side)

    def translate_red(self, red):
        red = self.ORIGIN_RED
        red += (red * (self.TILE_BORDER + self.TILE_HEIGHT))
        red += (self.TILE_HEIGHT/2)
        return Board.translate_red(self, red)

    def translate_black(self, black):
        black = self.ORIGIN_BLACK
        black += (black * (self.TILE_BORDER + self.TILE_HEIGHT))
        black += (self.TILE_HEIGHT/2)
        return Board.translate_black(self, black)
