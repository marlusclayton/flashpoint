#!/usr/bin/python
from PIL import Image, ImageFilter

class Map:

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

    def draw_map(self):
        self.image = Image.open( "assets/maps/{}.jpg".format(self.name) )

        self.draw_entities(self.firefighters)

        self.draw_entities(self.hazards)

        self.image.save('output/output.jpg', 'JPEG')

    def draw_entities(self, entities):
        image = self.image
        new_image = Image.new(image.mode, image.size)
        new_image.paste(image)

        for entity in entities.itervalues():
            red = entity.red
            black = entity.black
            translatedRed = self.translateRed(red)
            translatedBlack = self.translateBlack(black)
            left   = translatedBlack - entity.offsetBlack
            top    = translatedRed - entity.offsetRed
            right  = left + entity.width
            bottom = top + entity.height

            alpha = entity.image.split()[-1]
            new_image.paste(entity.image, (left, top, right, bottom), mask=alpha)

        self.image = new_image

    def translateRed(self, red):
        return red

    def translateBlack(self, black):
        return black


class StandardMap(Map):

    # black = { 0:368, 1:595, 2:821, 3:1040, 4:1263, 5:1483, 6:1704, 7:1927, 8:2147, 9:2371 }
    # red = { 0:115, 1:344, 2:572, 3:795,  4:1010, 5:1231, 6:1451, 7:1676 }
    ORIGIN_RED = 0
    ORIGIN_BLACK = 252
    TILE_WIDTH = 220
    TILE_HEIGHT = 220
    TILE_BORDER = 4

    def __init__(self):
        Map.__init__(self, "standard")

    def translateRed(self, red):
        red = self.ORIGIN_RED + (red * (self.TILE_BORDER + self.TILE_HEIGHT)) + (self.TILE_HEIGHT/2)
        return Map.translateRed(self, red)

    def translateBlack(self, black):
        black = self.ORIGIN_BLACK + (black * (self.TILE_BORDER + self.TILE_HEIGHT)) + (self.TILE_HEIGHT/2)
        return Map.translateBlack(self, black)
