import pandas as pd

import numpy as np


class Die:
    def __init__(self, faces):
        if not isinstance(faces, np.ndarray):
            try:
                faces = np.array(faces)
            except Exception as e:
                raise TypeError("Failed to convert faces to a numpy array.") from e

        if faces.dtype.kind not in 'SUiu':
            raise TypeError("Invalid dtype for faces; must be string or numeric.")

        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must have distinct values.")

        self._faces = faces
        self._weights = np.ones_like(faces, dtype=float)

    def alter_weight(self, face, new_weight):
        """

        """
        if face not in self._faces:
            raise IndexError(f"Face {face} not valid")

        if not isinstance(new_weight, (int, float)):
            raise TypeError("Not a numeric value")

        index = np.where(self._faces == face)[0][0]
        self._weights[index] = new_weight

    def roll(self, times=1):
        """

        """
        die_outcomes = np.random.choice(self._faces, size=times, p=self._weights / np.sum(self._weights))
        return die_outcomes.tolist()

    def display_state(self):
        """

        """
        current_state = {
            'faces': self._faces.tolist(),
            'weights': self._weights.tolist()
        }
        return current_state


class Game:
    def __init__(self, dice):
        """

        """
        self._dice = dice
        self._results = {}

    def play(self, num_rolls):
        """

        """
        cumulative_results = {}
        for i in range(num_rolls):
            roll_results = []
            for die in self._dice:
                roll_results.append(die.roll())
            cumulative_results[i + 1] = roll_results
        self._results = cumulative_results

    def show_results(self, format='wide'):
        """

        """
        if format == 'wide':
            return self._results
        elif format == 'narrow':
            df = pd.DataFrame(self._results).stack().reset_index()
            df.columns = ['Roll No.', 'Die No.', 'Outcome']
            return df
        else:
            raise ValueError("Invalid format")


class Analyzer:
    def __init__(self, game):
        """

        """
        if not isinstance(game, Game):
            raise ValueError("Not a Game object")
        self._game = game

    def jackpot(self):
        """

        """
        results = self._game.show_results(format='wide')
        jackpots = 0
        for roll in results.values():
            if len(set(roll)) == 1:
                jackpots += 1
        return jackpots

    def roll_face_counts(self):
        """

        """
        results = self._game.show_results(format='wide')
        face_counts = {}
        for roll_num, roll in results.items():
            face_counts[roll_num] = {face: roll.count(face) for face in set(roll)}
        return pd.DataFrame(face_counts).fillna(0)

    def combo_count(self):
        """

        """
        results = self._game.show_results(format='wide')
        combo_counts = {}
        for roll in results.values():
            combo = tuple(sorted(roll))
            if combo not in combo_counts:
                combo_counts[combo] = 0
            combo_counts[combo] += 1
        return pd.DataFrame.from_dict(combo_counts, orient='index', columns=['Count'])

    def permutation_count(self):
        """

        """
        results = self._game.show_results(format='wide')
        perm_counts = {}
        for roll in results.values():
            perm = tuple(roll)
            if perm not in perm_counts:
                perm_counts[perm] = 0
            perm_counts[perm] += 1
        return pd.DataFrame.from_dict(perm_counts, orient='index', columns=['Count'])
