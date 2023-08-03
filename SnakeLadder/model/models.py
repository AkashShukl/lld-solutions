import random




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






