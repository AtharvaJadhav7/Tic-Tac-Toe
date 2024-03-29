import math
import random


class player:
    def __init__(self,letter):
        self.letter = letter


    def get_move(self, game):
        pass

class ComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # return super().get_move(game)
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # return super().get_move(game)
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +"'s turn. Input move (0-9): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except:
                print('Invalid square. Try again.')

        return val
