import numpy as np
from mercy_cube_v1.octonion import Octonion

class MercyShard:
    def __init__(self, seed=13):
        np.random.seed(seed)
        self.vector = Octonion.random_normalized()

    def generate(self):
        return self.vector
