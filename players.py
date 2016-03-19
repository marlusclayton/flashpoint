#!/usr/bin/python
from characters import *

class Player:

    def __init__(self, username, role, color):
        self.username = username
        self.role = role
        self.color = color
        self.character = Character.factory(role, color)
