import mmh3
import numpy as np

class CountSketch:
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.table = np.zeros((depth, width))

    def _hash(self, key, seed):
        return mmh3.hash(key, seed) % self.width

    def update(self, key, value):
        for i in range(self.depth):
            hash_val = self._hash(key, i)
            self.table[i][hash_val] += value

    def estimate(self, key):
        estimates = []
        for i in range(self.depth):
            hash_val = self._hash(key, i)
            estimates.append(self.table[i][hash_val])
        return min(estimates)
