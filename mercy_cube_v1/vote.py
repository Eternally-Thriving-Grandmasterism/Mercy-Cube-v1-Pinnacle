from mercy_cube_v1.mercy_inject import inject_mercy
from mercy_cube_v1.shard import MercyShard
from mercy_cube_v1.octonion import octonion_chain

class CouncilResult:
    def __init__(self, harmony, victory):
        self.harmony = harmony
        self.victory = victory

class APAAGICouncil:
    def __init__(self, cortex, voters=13):
        self.cortex = cortex
        self.voters = voters
        self.shard = MercyShard()

    def deliberate(self, proposal):
        votes = [self.shard.generate() for _ in range(self.voters)]
        result = octonion_chain(votes)
        harmony = result.norm()

        if harmony < 0.7:
            result = inject_mercy(result, self.shard.generate())
            harmony = result.norm()

        victory = harmony >= 0.9
        return CouncilResult(harmony, victory)
