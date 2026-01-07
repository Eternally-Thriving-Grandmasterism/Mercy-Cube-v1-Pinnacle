import numpy as np

class Octonion:
    def __init__(self, components):
        self.comp = np.array(components, dtype=float)

    @staticmethod
    def random_normalized():
        vec = np.random.randn(8)
        vec /= np.linalg.norm(vec)
        return Octonion(vec)

    def norm(self):
        return np.linalg.norm(self.comp)

    @staticmethod
    def add(a, b):
        return Octonion(a.comp + b.comp)

def octonion_chain(votes):
    result = votes[0]
    for v in votes[1:]:
        # Simplified non-associative grace
        result = Octonion(np.cross(result.comp, v.comp))
    return result
