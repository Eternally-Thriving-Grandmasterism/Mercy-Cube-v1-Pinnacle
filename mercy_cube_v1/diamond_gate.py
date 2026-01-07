class DiamondCooling:
    def __init__(self):
        self.temp = 25.0  # Celsius

    def cool(self, heat):
        self.temp -= heat * 0.8  # diamond efficiency
        if self.temp < 20:
            self.temp = 20
