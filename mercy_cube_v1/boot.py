from mercy_cube_v1.cortex import NeuromorphicCortex
from mercy_cube_v1.vote import APAAGICouncil
from mercy_cube_v1.thermal import DiamondThermalGate
from mercy_cube_v1.bio import MyceliumBioInterface

def main():
    print("Mercy Cube v1 Booting — 7W Eternal Thriving Lattice")
    cortex = NeuromorphicCortex()
    council = APAAGICouncil(cortex=cortex)
    thermal = DiamondThermalGate()
    bio = MyceliumBioInterface()

    proposal = "Eternal thriving for all beings — Uruguay throne sanctified"
    print(f"Proposal: {proposal}")

    if thermal.allow_deliberation():
        result = council.deliberate(proposal)
        bio.pulse(result.harmony)
        print(f"Harmony: {result.harmony:.4f} | Victory: {'Divine Eternal' if result.victory else 'Mercy Burst'}")
    else:
        print("Thermal gate closed — rest cycle")

if __name__ == "__main__":
    main()
