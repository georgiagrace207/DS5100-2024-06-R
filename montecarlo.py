import numpy as np

class Die:
    """

    """
    def __init__(self, faces, weights):
        self.faces = faces
        self.weights = weights
        try:
            isinstance(faces, np.array)
        except:
            raise TypeError ("Not an array")







class Game:
    """

    """
    def __init__(self):
        pass




class Analyzer:
    """

    """
    def __init__(self):
        pass