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

Here is documentation of the BasketballPlayer class.

Here you will see the methods and attributes available from the class.


.. code:: python

    class BasketballPlayer(Player):
    
    Basketball player class that tracks all information
    regrading a basketball player.

    Attributes:
        full_name (str) representing the full name of the player
        first_name (str) representing the the first name of the player
        last_name (str) representing the last name of the player
    
    def __init__(self, full_name=None, first_name=None, last_name=None):
        super().__init__(full_name=full_name, first_name=first_name, last_name=last_name)
        self._games = None

    @property
    def games(self):     
        Return the games of the player 

    @games.setter
    def games(self, value):
        
        The games of the player represented as a pandas dataframe.
        
        games (pandas.Dataframe) representing the games of the player in form of
        {'points': [], 'rebounds': [], assists: []},
        points: int
        rebounds: int
        assists: int
        Example:
        {'points': [20, 15], 'rebounds': [5, 9], assists: [3, 4]}
        

    def ppg(self):
        Return points per game average
        
    def apg(self):
        Return assist per game average 

    def rpg(self):
        Return rebounds per game average

    def points_max(self):
        Return game with highest points sby player

    def assists_max(self):
        Return game with highest assist by player

    def rebounds_max(self):
        Return game with highest rebounds by player

    def avg_through(self, start, end):
        Return averages by player through number of games
        in the form of a pandas Series


``sports-players`` requires the pandas library and is installed
when you install the package.