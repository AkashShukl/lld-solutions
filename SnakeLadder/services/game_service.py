
# game_service.py

from model.models import Board, Dice

class SnakeAndLadder:

    def __init__(self, blockCount, snakes, ladders, players) -> None:
        self.blockCount = blockCount
        self.snakes = snakes
        self.ladders = ladders
        self.players = players
        self.board = Board( blockCount, ladders, snakes )
        self.dice = Dice(1)
        self.winner = None



    def announceWinner(self):
        print("Winner ::: ", self.winner.name, self.winner.id)

    def startGame(self):

        while self.winner is None:

            for player in self.players:

                moves = self.dice.rollDice()

                prev = player.position.number

                if prev + moves <= self.blockCount:

                    player.position = self.board.blocks[prev + moves]

                    if player.position.ladder:
                        player.position = self.board.blocks[player.position.ladder.toBlock]

                    if player.position.snake:
                        player.position = self.board.blocks[player.position.snake.tail]

                    print(str(player.name) + " rolled a " + str(moves) + " and moved from " + str(prev) + " to " + str(player.position.number))

                    if player.position.number == self.blockCount:
                        self.winner = player
                        break
        self.announceWinner()





