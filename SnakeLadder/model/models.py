import random

class Dice:
    def __init__(self, count: int):
        self.diceCount = count
        self.consecutiveSixCount = 0
        self.maxAllowedConsecutiveSixes = 3

    def rollDice(self) -> int:
        return random.randint(1, 6)

    def resetConsecutiveSixesCount(self):
        self.consecutiveSixCount = 0

    def rollWithLimit(self) -> int:
        moves = self.rollDice()
        if moves != 6:
            total_moves = self.consecutiveSixCount * 6 + moves
            self.resetConsecutiveSixesCount()
            return total_moves
        else:
            self.consecutiveSixCount += 1
            if self.consecutiveSixCount == self.maxAllowedConsecutiveSixes:
                self.resetConsecutiveSixesCount()
                return 0
            return self.rollWithLimit()

    def multiDiceRoll(self):
        total_moves = 0
        for n in range(self.diceCount):
            total_moves += self.rollDice()
        return total_moves




class Player:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.position = Block(0)

    def move(self, pos: int):
        self.position = pos

class Snake:
    def __init__(self, head: int, tail: int):
        self.head = head
        self.tail = tail


class Ladder:
    def __init__(self, fromBlock : int, toBlock: int):
        self.fromBlock = fromBlock
        self.toBlock = toBlock


class Block:
    def __init__(self, number):
        self.number = number
        self.snake = None
        self.ladder = None

    def place_ladder(self, ladder):
        self.ladder = ladder

    def place_snake(self, snake):
        self.snake = snake


class Board:
    def __init__(self, blocksCount: int, ladders, snakes):
        self.blocks = [Block(count) for count in range(blocksCount+1)]

        for ladder in ladders:
            self.blocks[ladder.fromBlock].place_ladder(ladder)

        for snake in snakes:
            self.blocks[snake.head].place_snake(snake)






