#!/usr/bin/python
from dispatcher import Dispatcher

@given("I have a new dispatcher")
def no_game_running(context):
    context.dispatcher = Dispatcher()

@when("I setup a {difficulty} game for {number_of_players} players")
def setup_game(context, difficulty, number_of_players):
    dispatcher = context.dispatcher
    dispatcher.setup(difficulty, number_of_players)

@then ("I have {entity} at {coords}")
def I_have_entity_at(context, entity, coords):
    dispatcher = context.dispatcher
    entity = dispatcher.board.get_entities_at(2, 2)

    assert isinstance(entity, Fire) is True
