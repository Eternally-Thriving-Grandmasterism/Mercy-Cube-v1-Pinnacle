class RISCVCore:
    def __init__(self, freq_mhz=16):
        self.freq = freq_mhz * 1_000_000
        print(f"RISC-V core @ {freq_mhz} MHz — low power eternal")
