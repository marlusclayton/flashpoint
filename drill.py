#!/usr/bin/python
from dispatcher import Dispatcher
import random

d = Dispatcher()
player1 = d.create_player("Player 1", "white")
player2 = d.create_player("Player 2", "blue")
player3 = d.create_player("Player 3", "red")

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

red = random.randint(1, 6)
black = random.randint(1, 8)
print "smoke at {} {}".format(red, black)
d.add_hazard("smoke", red, black)

red = random.randint(1, 6)
black = random.randint(1, 8)
print "fire at {} {}".format(red, black)
d.add_hazard("fire", red, black)

red = random.randint(1, 6)
black = random.randint(1, 8)
print "hazmat at {} {}".format(red, black)
d.add_hazard("hazmat", red, black)

red = random.randint(1, 6)
black = random.randint(1, 8)
print "hot_spot at {} {}".format(red, black)
d.add_hazard("hot_spot", red, black)

d.turn_order("driver", "rescue_dog", "paramedic")

d.show_board()


#367, 344
