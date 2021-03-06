#!/usr/bin/python
from __future__ import generators, unicode_literals
from PIL import Image, ImageFilter

class Entity(object):

    def __init__(self, entity_type, red, black):
        self.entity_type = entity_type
        self.key = "{}-{}-{}".format(entity_type, red, black)
        self.set_position(red, black)
        self.width = 120
        self.height = 120
        self.offsetRed = self.height/2
        self.offsetBlack = self.width/2

    def set_position(self, red, black):
        self.red = red
        self.black = black

    def get_image_name(self):
        return self.image_name

    def get_image(self):
        return Image.open(self.get_image_name()).resize((self.width,self.height))


    def draw(self, board):
        self.entity_image = self.get_image()

        board_image = board.image
        mixed_image = Image.new(board_image.mode, board_image.size)
        mixed_image.paste(board_image)

        translated_red = board.translate_red(self.red)
        translated_black = board.translate_black(self.black)
        left   = translated_black - self.offsetBlack
        top    = translated_red - self.offsetRed
        right  = left + self.width
        bottom = top + self.height

        alpha = self.entity_image.split()[-1]
        mixed_image.paste(self.entity_image, (left, top, right, bottom), mask=alpha)

        board.image = mixed_image
