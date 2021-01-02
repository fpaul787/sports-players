from .General_Player import Player
import pandas
class BasketballPlayer(Player):
    """
    Basketball player class that tracks all information
    regrading a basketball player.

    Attributes:
        full_name (str) representing the full name of the player
        first_name (str) representing the the first name of the player
        last_name (str) representing the last name of the player
    """
    def __init__(self, full_name=None, first_name=None, last_name=None):
        super().__init__(full_name=full_name, first_name=first_name, last_name=last_name)
        self._games = None

    @property
    def games(self):
        """       
        Return the games of the player 
        """
        return self._games

    @games.setter
    def games(self, value):
        """ 
        The games of the player represented as a pandas dataframe.
        
        games (pandas.Dataframe) representing the games of the player in form of
        {'points': [], 'rebounds': [], assists: []},
        points: int
        rebounds: int
        assists: int
        Example:
        {'points': [20, 15], 'rebounds': [5, 9], assists: [3, 4]}
        
        """
        if isinstance(value, pandas.DataFrame):
            if 'points' not in value.columns: # if there isn't a points column
                raise ValueError("Missing 'points' column")
            elif 'rebounds' not in value.columns: # if there isn't a rebounds column
                raise ValueError("Missing 'rebounds' column")
            elif 'assist' not in value.columns: # if there isn't a assist column
                raise ValueError("Missing 'assist' column")
        elif value is None:
            self._games = None
        else:
            raise TypeError("games must be a dataframe")

    def ppg(self):
        """
        Return points per game average
        """
        pass
    
    def apg(self):
        """ 
        Return assist per game average 
        """
        pass

    def rpg(self):
        """
        Return rebounds per game average
        """
        pass

    def points_max(self):
        """ 
        Return game with highest points sby player
        """
        pass

    def assist_max(self):
        """ 
        Return game with highest assist by player
        """
        pass

    def rebounds_max(self):
        """ 
        Return game with highest rebounds by player
        """
        pass

    def avg_through(self, number_games):
        """ 
        Return averages by player through number of games
        """
        pass
