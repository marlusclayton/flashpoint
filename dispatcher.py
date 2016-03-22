#!/usr/bin/python
import random
from boards import StandardBoard
from players import Player
from firefighters import *
from hazards import *
from pois import POI
from doors import Door

class Dispatcher:

    def __init__(self):
        self.board = StandardBoard("A")

    def create_firefighter(self, role, player):
        firefighter = Firefighter.factory(role, player, 0, 0)
        self.board.add_firefighter(firefighter)
        print "firefighter: {} created for player {} ({})".format(role, player.name, player.color)
        return firefighter

    def create_player(self, name, color):
        return Player(name, color)
        print "player {} ({})".format(name, color)

    def turn_order(self, *firefighters):
        self.turn_order = firefighters
        print "turn order: {}".format(self.turn_order)

    def show_board(self):
        self.board.draw()
        print "board image created"

    def move_to(self, role, red, black):
        print "{} moving to {} {}".format(role, red, black)
        firefighter = self.board.firefighters[role]
        firefighter.set_position(red, black)
        self.board.firefighters[role] = firefighter

    def add_hazard(self, hazard_type, red, black):
        print "{} at {} {}".format(hazard_type, red, black)
        hazard = Hazard.factory(hazard_type, red, black)
        self.board.add_hazard(hazard)

    def add_poi(self, red, black):
        poi_list = []
        for poi_type, remaning in self.board.available_pois.iteritems():
            for i in range(remaning):
                poi_list.append(poi_type)

        rand = random.randint(0, len(poi_list)-1)
        poi_type = poi_list.pop(rand)
        poi = POI.factory(poi_type, red, black)
        print "POI at {} {}".format(red, black)
        self.board.add_poi(poi)

    def add_link(self, red, black, red_link, black_link):
        door = Door("closed", red, black, red_link, black_link)
        self.board.add_link(door)

    def setup(self, game_difficulty, number_of_players):
        print "setup {} game for {} players".format(game_difficulty, number_of_players)
        if game_difficulty == "family": self.family_setup(number_of_players)
        if game_difficulty == "recruit": self.family_setup(number_of_players)
        if game_difficulty == "veteran": self.family_setup(number_of_players)
        if game_difficulty == "heroic": self.family_setup(number_of_players)

    def family_setup(self, number_of_players):
        print "setting up Fire"
        for red, black in [(2,2), (2,3), (3,2), (3,3), (3,4), (3,5), (4,4), (5,6), (5,7), (6,6)]:
            self.add_hazard("fire", red, black)

        print "setting up POIs"
        for red, black in [(2,4), (5,1), (5,8)]:
            self.add_poi(red, black)

        print "setting up Closed Doors"
        for entrance_red, entrance_black, exit_red, exit_black in [(1,3,1,4), (2,5,2,6), (2,8,3,8), (3,2,3,3), (4,4,5,4), (4,6,4,7), (6,5,6,6), (6,7,6,8)]:
            self.add_link(entrance_red, entrance_black, exit_red, exit_black)

    def random_coords(self):
        return (self.rollD6(), self.rollD8())

    def rollD6(self):
        return random.randint(1, 6)

    def rollD8(self):
        return random.randint(1, 8)


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
