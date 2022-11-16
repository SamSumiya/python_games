import random
import math

class Player: 
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass
    


class HumanPlayer: 
    def __init__(self, letter): 
        super().__init__(letter)

        def get_move(self, game):
            valid_square = False
            val = None
            while not valid_square: 
                square = input(self.letter + ' \'s turn. Input move 0 - 8: ')
                try:
                    val = int(square)
                    if val not in game.valid_move(): 
                        raise ValueError()
                    valid_square = True
                except ValueError:
                    print('Invalid square. Try again.')
            return val

class ComputerPlayer: 
    def __init__(self, letter): 
        super().__init__(letter)

        def get_move(self, game):
            square = random.choice(game.valid_move())
            return square




