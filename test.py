from sports_players import BasketballPlayer
import pandas as pd
import unittest

class TestBasketballPlayerClass(unittest.TestCase):
    def setUp(self):
        self.player = BasketballPlayer(full_name="Frantz Paul")
        self.data = {'points': [20, 10, 10, 10], 'rebounds': [4, 3, 2, 10], 'assists': [2, 4, 7, 2]}
        self.games = pd.DataFrame(data=self.data)
        self.player.games = self.games
        return super().setUp()

    def test_initialization(self):
        self.assertEqual(self.player.full_name, "Frantz Paul", 'incorrect full name')
        self.assertNotEqual(self.player.full_name, 'Alexander Coffee', 'player name is equal to wrong value')

    def test_ppg(self):
        self.assertEqual(self.player.ppg(), self.games['points'].mean())

    def test_apg(self):
        self.assertEqual(self.player.apg(), self.games['assists'].mean())

    def test_rpg(self):
        self.assertEqual(self.player.rpg(), self.games['rebounds'].mean())

    def test_max_points(self):
        self.assertEqual(self.player.points_max(), self.games['points'].max())

    def test_max_assist(self):
        self.assertEqual(self.player.assists_max(), self.games['assists'].max())

    def test_max_rebounds(self):
        self.assertEqual(self.player.rebounds_max(), self.games['rebounds'].max())
    
    def test_avg_through_points(self):
        self.assertEqual(self.player.avg_through(0, 2)['points'], self.games.loc[0:2].mean()['points'])
if __name__ == '__main__':
    unittest.main()