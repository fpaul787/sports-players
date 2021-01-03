sports-players
===================================

This is project created by Frantz Paul.

``sports-players`` a fun way to represent sports players as objects.

# Installation

pip install sports_players

.. code:: python

    from sports_players import BasketballPlayer

    import pandas as pd

    player = BasketballPlayer(full_name="Lebron James")
    data = {'points': [20, 10, 10, 10], 'rebounds': [4, 3, 2, 10], 'assists': [2, 4, 7, 2]}

    games = pd.DataFrame(data=data)
    player.games = games

    print(player.ppg()) # returns player points per game
    print(player.apg()) # returns player assists per game

Instantiaion
a player can be instantiated with either their full_name, first_name, or last_name

.. code:: python

    BasketballPlayer(full_name="Lebron James", first_name="Lebron", last_name="James")

Properties:
full_name: full name of player. None if not specified.
first_name: first name of player. None if not specified
last_name: last name of player. None if not specified
games: All player games. None if not specified

Methods:
player.ppg(): average of points per game for player
player.apg(): average of assists per game of player
player.rbg(): average of rebounds per game of player
player.points_max(): maximum points a player has gotten in a game
player.rebounds_max(): maximum rebounds a player has gotten in a game 
player.assists_max(): maximum assists a player has gotten in a game
player.avg_through(start, finish): player average from a beginning point to an end point

``sports-players`` requires the pandas library and is installed
when you install the package.