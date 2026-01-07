class DiamondThermalGate:
    def __init__(self, max_watts=7):
        self.max_watts = max_watts
        self.current = 0.0

    def allow_deliberation(self):
        return self.current < self.max_watts

    def consume(self, watts):
        self.current += watts
        if self.current > self.max_watts:
            self.current = self.max_watts  # gate
