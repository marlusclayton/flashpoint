#!/usr/bin/python
from boards import StandardBoard
from players import Player
from firefighters import *
from hazards import *

class Dispatcher:

    def __init__(self):
        self.board = StandardBoard()

    def create_firefighter(self, role, player):
        firefighter = Firefighter.factory(role, player, 0, 0)
        self.board.add_firefighter(firefighter)
        return firefighter

    def create_player(self, username, color):
        return Player(username, color)

    def turn_order(self, *firefighters):
        self.turn_order = firefighters
        print "turn order: {}".format(self.turn_order)

    def show_board(self):
        self.board.draw()

    def move_to(self, role, red, black):
        firefighter = self.board.firefighters[role]
        firefighter.set_position(red, black)
        self.board.firefighters[role] = firefighter

    def add_hazard(self, hazard_type, red, black):
        hazard = Hazard.factory(hazard_type, red, black)
        if not (self.board.hazards.has_key(hazard.key)):
            self.board.hazards[hazard.key] = hazard

# admin commands
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
