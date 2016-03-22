Feature: Game setup
  In order to start a new game
  I want to be able to setup a family, recruit, veteran or heroic game

  Scenario: Family game setup
    Given I have a new dispatcher
    When I setup a family game for 6 players
    Then I have fire at 2:2 2:3 3:2 3:3 3:4 3:5 4:4 5:6 5:7 6:6
    And I have poi at 2:4 5:1 5:8
    And I have closed doors at 1:3:1:4 2:5:2:6 2:8:3:8 3:2:3:3 4:4:5:4 4:6:4:7 6:5:6:6 6:7:6:8
