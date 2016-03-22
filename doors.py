#!/usr/bin/python
from __future__ import generators, unicode_literals
from entities import Entity

class Door(Entity):

    def __init__(self, door_type, red, black, red_link, black_link):
        Entity.__init__(self, door_type, red, black)
        self.red_link = red_link
        self.black_link = black_link
        self.key = "door-{}-{}-{}-{}".format(red, black, red_link, black_link)
        self.width = 100
        self.height = 100
        self.set_offset()
        self.close()

    def get_image_name(self):
        self.image_name = "assets/tokens/door_{}.png".format(self.status)
        return self.image_name

    def get_image(self):
        image = super(self.__class__, self).get_image()
        if (self.is_horizontal()):
            return image.rotate(90)
        return image

    def set_offset(self):
        if self.at_east():
            self.offsetRed = self.height/2
            self.offsetBlack = self.width/2+110
        if self.at_south():
            self.offsetRed = self.height/2+120
            self.offsetBlack = self.width/2
        if self.at_west():
            self.offsetRed = self.height/2
            self.offsetBlack = self.width/2-110
        if self.at_north():
            self.offsetRed = self.height/2-120
            self.offsetBlack = self.width/2

    def open(self):
        self.status = "opened"

    def close(self):
        self.status = "closed"

    def is_open(self):
        return self.status == "opened"

    def is_horizontal(self):
        return self.red == self.red_link

    def is_vertical(self):
        return self.black == self.black_link

    def at_west(self):
        return self.is_horizontal() & (self.black < self.black_link)

    def at_east(self):
        return self.is_horizontal() & (self.black > self.black_link)

    def at_north(self):
        return self.is_vertical() & (self.red < self.red_link)

    def at_south (self):
        return self.is_vertical() & (self.red > self.red_link)
