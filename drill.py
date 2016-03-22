#!/usr/bin/python
from dispatcher import Dispatcher

d = Dispatcher()

d.setup("family", 3)

player1 = d.create_player("Player 1", "white")
player2 = d.create_player("Player 2", "blue")
player3 = d.create_player("Player 3", "red")

d.create_firefighter("paramedic", player1)
d.create_firefighter("driver", player2)
d.create_firefighter("rescue_dog", player3)

d.move_to("paramedic", 0, 0)
d.move_to("driver", 0, 0)
d.move_to("rescue_dog", 0, 0)

d.turn_order("driver", "rescue_dog", "paramedic")

d.show_board()
