from player import HumanPlayer, ComputerPlayer 


class TicTacToe: 
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self): 
        for i in range(3): 
            for row in [self.board[i*3: (i+1)*3]]:
                print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_position():
        number_board = []
        for i in range(3):
            temp = [] 
            for j in range(i*3, (i+1)*3): 
                temp.append(str(j))
            number_board.append(temp)
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def valid_move(self): 
        moves = [] 
        for (idx, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(idx)
        return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def number_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.is_winner(square, letter): 
                self.current_winner = letter
            return True
        return False
    
    def is_winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index* 3: ((row_index + 1) * 3)]
        if all([spot == letter for spot in row]): 
            return True
        
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]): 
            return True
        
        if square % 2 == 0: 
            diagnal_1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagnal_1]):
                return True
            diagnal_2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagnal_2]):
                return True

        return False


def play(game, human_player, computer_player, print_game=True):
    if print_game: 
        game.print_board_position() 
        print(' ')
        game.print_board()
    
    letter = 'O'

    while game.empty_squares():
        if letter == 'O':
            square = human_player.get_move(game)
        else: 
            square = computer_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game: 
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

        if game.current_winner: 
            if print_game:
                print(letter + ' wins!')
            return letter
        
        letter = "X" if letter == 'O' else 'O'

    if print_game:
        print("It's a tie!") 
    

# ttt = TicTacToe()
# # board = ttt.print_board()
# print(board)
# print(TicTacToe.print_board_position())


if __name__ == '__main__': 
    human_player = HumanPlayer('O')
    computer_player = ComputerPlayer('X')
    t = TicTacToe()
    play(t, human_player, computer_player, print_game=True)