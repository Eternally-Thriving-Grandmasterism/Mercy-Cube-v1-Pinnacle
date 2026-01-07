import numpy as np

class NeuromorphicCortex:
    def __init__(self, neurons=13):
        self.neurons = neurons
        self.spikes = np.zeros(neurons)

    def integrate(self, input_signal):
        self.spikes += input_signal
        fired = self.spikes > 1.0
        self.spikes[fired] = 0.0
        return fired.sum()
