import unittest
import numpy as np
from montecarlo import Die

class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Die(np.array([1, 2, 3, 4, 5, 6]))

    def test_roll_die_once(self):
        result = self.die.roll()
        self.assertIn(result, [1, 2, 3, 4, 5, 6])

    def test_change_weight(self):
        self.die.alter_weight(1, 2.0)
        self.assertEqual(self.die.weights[1], 2.0)


class TestGame(unittest.TestCase):
    def setUp(self):
        self.dice = [Die([1, 2, 3, 4, 5, 6]), Die([1, 2, 3, 4, 5, 6])]
        self.game = Game(self.dice)

    def test_play_game_once(self):
        self.game.play(1)
        results = self.game.show_results()
        self.assertEqual(len(results), 1)


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.dice = [Die([1, 2, 3, 4, 5, 6]), Die([1, 2, 3, 4, 5, 6])]
        self.game = Game(self.dice)
        self.game.play(5)  
        self.analyzer = Analyzer(self.game)

    def test_analyze_jackpot(self):
        self.assertEqual(self.analyzer.jackpot(), 0) 

    def test_analyze_face_counts_per_roll(self):
        face_counts = self.analyzer.roll_face_counts()
        self.assertEqual(face_counts.loc[0, 1], 1) 

if __name__ == '__main__':
    unittest.main()
