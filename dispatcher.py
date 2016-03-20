#!/usr/bin/python
from firefighters import *
from hazards import *
from maps import StandardMap
from players import Player
import random

class Dispatcher:

    players = {}

    def __init__(self):
        self.map = StandardMap()

    def create_firefighter(self, role, player):
        firefighter = Firefighter.factory(role, player)
        self.map.add_firefighter(firefighter)
        return firefighter

    def create_player(self, username, color):
        player = Player(username, color)
        return player

# admin commands
# playerorder(players...), showmap, role(role), color(color), admin(user, command),
# addhazard(smoke/fire/hotspot/hazmat, red, black), removehazard(smoke/fire/hotspot/hazmat, red, black),
# addlink(damage/door, red, black, direction), removelink(damage/door, red, black, direction), flashover(), explode(red, black), bank(damage/hotspot, quantity)
    def turn_order(self, *firefighters):
        self.turn_order = firefighters
        print "turn order: {}".format(self.turn_order)

    def show_map(self):
        self.map.draw_map()

    def role(self, username, role):
        player = self.getPlayer(username)
        character = player.character
        red = character.red
        black = character.black
        player.role(role)
        player.position(red, black)

    def color(self, username, color):
        player = self.getPlayer(username)
        character = player.character
        red = character.red
        black = character.black
        player.color(color)
        player.position(red, black)

    def move_to(self, role, red, black):
        firefighter = self.map.firefighters[role]
        firefighter.set_position(red, black)
        self.map.firefighters[role] = firefighter

    def add_hazard(self, hazard_type, red, black):
        hazard = Hazard.factory(hazard_type, red, black)
        if not (self.map.hazards.has_key(hazard.key)):
            self.map.hazards[hazard.key] = hazard


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
marlus = d.create_player("Marlus", "white")
danilo = d.create_player("Danilo", "blue")
ricardo = d.create_player("Ricardo", "red")

d.create_firefighter("paramedic", marlus)
d.create_firefighter("driver", danilo)
d.create_firefighter("rescue_dog", ricardo)

red = random.randint(0, 7)
black = random.randint(0, 9)
print "move to {} {}".format(red, black)
d.move_to("paramedic", red, black)

red = random.randint(0, 7)
black = random.randint(0, 9)
print "move to {} {}".format(red, black)
d.move_to("driver", red, black)

red = random.randint(0, 7)
black = random.randint(0, 9)
print "move to {} {}".format(red, black)
d.move_to("rescue_dog", red, black)

red = random.randint(0, 7)
black = random.randint(0, 9)
print "smoke at {} {}".format(red, black)
d.add_hazard("smoke", red, black)

red = random.randint(0, 7)
black = random.randint(0, 9)
print "fire at {} {}".format(red, black)
d.add_hazard("fire", red, black)

red = random.randint(0, 7)
black = random.randint(0, 9)
print "hazmat at {} {}".format(red, black)
d.add_hazard("hazmat", red, black)

red = random.randint(0, 7)
black = random.randint(0, 9)
print "hot_spot at {} {}".format(red, black)
d.add_hazard("hot_spot", red, black)

d.turn_order("driver", "rescue_dog", "paramedic")

d.show_map()


#367, 344
