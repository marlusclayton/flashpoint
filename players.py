#!/usr/bin/python
from characters import *

class Player:

    def __init__(self, username, role, color):
        self.username = username
        self.config(role, color)

    def config(self, role, color):
        self.role = role
        self.color = color
        self.character = Character.factory(role, color)

    def role(self, role):
        self.config(role, self.color)

    def color(self, color):
        self.config(self.role, color)

    def position(self, red, black):
        self.character.position(red, black)
