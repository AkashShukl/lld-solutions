import random


class DiceRollStrategy:
    def roll(self):
        pass


class SingleDiceRollStrategy:
    def roll(self) -> int:
        return random.randint(1, 6)


class ConsecutiveSixesDiceRollStrategy(DiceRollStrategy):
    def __init__(self, max_allowed_consecutive_sixes=3):
        self.consecutive_six_count = 0
        self.max_allowed_consecutive_sixes = max_allowed_consecutive_sixes

    def roll(self) -> int:
        moves = random.randint(1, 6)
        if moves != 6:
            total_moves = self.consecutive_six_count * 6 + moves
            self.consecutive_six_count = 0
            return total_moves
        else:
            self.consecutiveSixCount += 1
            if self.consecutive_six_count == self.max_allowed_consecutive_sixes:
                self.consecutive_six_count = 0
                return 0
            return self.roll()


class Dice:
    def __init__(self, count: int, strategy: DiceRollStrategy):
        self.diceCount = count
        self.strategy = strategy

    def roll(self) -> int:
        total_moves = 0
        for _ in range(self.diceCount):
            total_moves += self.strategy.roll()
        return total_moves
