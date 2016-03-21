#!/usr/bin/python
from dispatcher import Dispatcher
import random

def random_coords():
    return (random.randint(1, 6), random.randint(1, 8))

d = Dispatcher()
player1 = d.create_player("Player 1", "white")
player2 = d.create_player("Player 2", "blue")
player3 = d.create_player("Player 3", "red")

d.create_firefighter("paramedic", player1)
d.create_firefighter("driver", player2)
d.create_firefighter("rescue_dog", player3)

red, black = random_coords()
print "move to {} {}".format(red, black)
d.move_to("paramedic", red, black)

red, black = random_coords()
print "move to {} {}".format(red, black)
d.move_to("driver", red, black)

red, black = random_coords()
print "move to {} {}".format(red, black)
d.move_to("rescue_dog", red, black)

red, black = random_coords()
print "smoke at {} {}".format(red, black)
d.add_hazard("smoke", red, black)

red, black = random_coords()
print "fire at {} {}".format(red, black)
d.add_hazard("fire", red, black)

red, black = random_coords()
print "hazmat at {} {}".format(red, black)
d.add_hazard("hazmat", red, black)

red, black = random_coords()
print "hot_spot at {} {}".format(red, black)
d.add_hazard("hot_spot", red, black)

d.turn_order("driver", "rescue_dog", "paramedic")

d.show_board()


#367, 344
