from services.game_service import SnakeAndLadder
from model.models import Snake
from model.models import Ladder
from model.models import Player
from model.dice import SingleDiceRollStrategy
from constants import SNAKE_BODY
from constants import TOTAL_BLOCKS
from constants import SNAKES_COUNT
from constants import PLAYER_COUNT
from constants import PLAYER
from constants import LADDER_BODY
from constants import LADDER_COUNT


if __name__ == '__main__':
    snakes = []
    for i in range(SNAKES_COUNT):
        h, t = SNAKE_BODY[i]
        snakes.append(Snake(head=h, tail=t))

    ladders = []
    for i in range(LADDER_COUNT):
        h, t = LADDER_BODY[i]
        ladders.append(Ladder(h, t))

    players = []
    for i in range(PLAYER_COUNT):
        name, id = PLAYER[i]
        players.append(Player(name, id))

    diceRollStrategy = SingleDiceRollStrategy()

    snl = SnakeAndLadder.get_instance(TOTAL_BLOCKS, snakes, ladders,
                                      players, diceRollStrategy)
    snl.startGame()
