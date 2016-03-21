#!/usr/bin/python
from __future__ import generators, unicode_literals
from PIL import Image, ImageFilter

class Board:

    def __init__(self, name):
        self.name = name
        self.load()

    def load(self):
        self.image = Image.open( "assets/maps/{}.jpg".format(self.name) )

    def save(self):
        self.image.save('output/output.jpg', 'JPEG')

    def position(self, entity):
        red = entity.red
        black = entity.black
        translatedRed = self.translateRed(red)
        translatedBlack = self.translateBlack(black)
        left   = translatedBlack - entity.offsetBlack
        top    = translatedRed - entity.offsetRed
        right  = left + entity.width
        bottom = top + entity.height

        image = self.image
        alpha = image.split()[-1]

        newImage = Image.new(image.mode, image.size)
        newImage.paste(image)

        alpha = entity.image.split()[-1]

        newImage.paste(entity.image, (left, top, right, bottom), mask=alpha)

        self.image = newImage

    def translateRed(self, red):
        return red

    def translateBlack(self, black):
        return black
        
class StandardBoard(Board):

    BLACK = { 0:368, 1:595, 2:821, 3:1040, 4:1263, 5:1483, 6:1704, 7:1927, 8:2147, 9:2371 }
    RED = { 0:115, 1:344, 2:572, 3:795,  4:1010, 5:1231, 6:1451, 7:1676 }

    def __init__(self):
        Board.__init__(self, "standard")

    def translateRed(self, red):
        return Board.translateRed(self, self.RED[red])

    def translateBlack(self, black):
        return Board.translateBlack(self, self.BLACK[black])
