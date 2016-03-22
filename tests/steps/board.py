#!/usr/bin/python
from dispatcher import Dispatcher

@given("I have a new dispatcher")
def no_game_running(context):
    context.dispatcher = Dispatcher()

@when("I setup a {\d{1,6}} players {\w+} game")
def setup_game(number_of_players, difficulty):
    dispatcher = context.dispatcher
    dispatcher.setup(difficulty, number_of_players)

@then ("I have {\w+} at\s{\d:\d}+")
def I_have_fire_at(entity, coords):
    assert True is True
