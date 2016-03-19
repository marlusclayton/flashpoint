#!/usr/bin/python
from characters import *
from maps import StandardMap
from players import Player
import random

class Dispatcher:

    players = {}
    board = [[0 for x in range(8)] for x in range(10)]

    def __init__(self):
        self.map = StandardMap()

    def addPlayer(self, username, role, color):
        player = Player(username, role, color)
        self.setPlayer(player)

    def setPlayer(self, player):
        self.players[player.username.lower()] = player

    def getPlayer(self, username):
        return self.players[username.lower()]

    def showmap(self):
        self.map.save()

    def moveto(self, username, red, black):
        character = self.getPlayer(username).character
        character.red = red
        character.black = black
        self.map.position(character)

# admin
# playerorder(players...), showmap, role(role), color(color), admin(user, command),
# addhazard(smoke/fire/hotspot/hazmat, red, black), removehazard(smoke/fire/hotspot/hazmat, red, black),
# addlink(damage/door, red, black, direction), removelink(damage/door, red, black, direction), flashover(), explode(red, black), bank(damage/hotspot, quantity)

# general
# move(direction), movevictim(direction), move2victim(direction), movehazmat(direction),
# moveto(red, black), movevictimto(red, black), movehazmatto(red, black)
# close(direction), open(direction), reveal, extinguish(direction), extinguishall(direction), chop(direction), ambulance(direction), firetruck(direction),
# drive(direction, riders...), deckgun, rescue, updatepois, advancefire, advancefire stop, adcanveturn, clearoutside, saveap(quantity), removeap(quantity), role(role)

# specialists
# dispose, identity(red, black), treat, movesmoke(red,black,direction), movepoi(red,black,direction), doorpoi(red,black,direction),
# command(username, commandline), repair(direction), clear, sit, heel

# maps
# getladder, dropladder, erectladder, collapseladder

d = Dispatcher()
d.addPlayer("Marlus", "paramedic", "white")
d.moveto("Marlus", 0, 0)
d.showmap()


#367, 344
