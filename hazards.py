#!/usr/bin/python
from __future__ import generators, unicode_literals
from PIL import Image, ImageFilter

class Hazard(object):

    width = 120
    height = 120
    offsetRed = height/2
    offsetBlack = width/2

    def __init__(self, hazard_type, red, black):
        self.hazard_type = hazard_type
        self.set_position(red, black)
        self.key = "{}-{}-{}".format(hazard_type, red, black)

        self.image = Image.open("assets/tokens/{}.png".format(self.hazard_type)).resize((self.width,self.height))

    @staticmethod
    def factory(hazard_type, red, black):
        if hazard_type == "smoke": return Smoke(red, black)
        if hazard_type == "fire": return Fire(red, black)
        if hazard_type == "hazmat": return Hazmat(red, black)
        if hazard_type == "hot_spot": return HotSpot(red, black)

    def set_position(self, red, black):
        self.red = red
        self.black = black

    def draw(self, map):
        image = map.image
        new_image = Image.new(image.mode, image.size)
        new_image.paste(image)

        translatedRed = map.translateRed(self.red)
        translatedBlack = map.translateBlack(self.black)
        left   = translatedBlack - self.offsetBlack
        top    = translatedRed - self.offsetRed
        right  = left + self.width
        bottom = top + self.height

        alpha = self.image.split()[-1]
        new_image.paste(self.image, (left, top, right, bottom), mask=alpha)

        map.image = new_image


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
        self.width = 60
        self.height = 60
        self.offsetRed = self.height+40
        self.offsetBlack = self.width+40
        Hazard.__init__(self, "hot_spot", red, black)
