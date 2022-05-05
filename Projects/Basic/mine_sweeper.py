import random
import re

# consider making the board
# 0 - conider size of board and number of bombs
# 1 - create the empty space 2d arrasy
# 2 - assign the bomb areas
# 3 - assign the number values around the bombs


class Board:
    # need to know how big the board and now many bombs
    def __init__(self, board_size, num_bomb):
        self.board_size = board_size
        self.num_bomb = num_bomb

        self.board = self.make_new_board()
        self.assign_board_values()

        # Need to also keep track of where we dig, so a set can be used
        self.dug = set()

    # create board instance empty
    def make_new_board(self):
        board = [[None for _ in range(self.board_size)]
                 for I in range(self.board_size)]

        # now place bombs
        # keep track of bombs placed
        bombs_planted = 0

        while bombs_planted < self.num_bomb:
            loc = random.randint(0, self.board_size**2 - 1)
            row = loc // self.board_size
            col = loc % self.board_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_board_values(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_adjacent_check(r, c)

    def get_adjacent_check(self, row, col):
        num_adjacent_bombs = 0
        for r in range(max(0, row - 1), min(self.board_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.board_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_adjacent_bombs += 1

        return num_adjacent_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.board_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.board_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue  # don't dig where you've already dug
                self.dig(r, c)

        return True

# Create a visual board
    def __str__(self):
        visible_board = [[None for _ in range(
            self.board_size)] for _ in range(self.board_size)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        string_rep = ''
        width = []
        for idx in range(self.board_size):
            columns = map(lambda x: x[idx], visible_board)
            width.append(
                len(
                    max(columns, key=len)
                )
            )

        indices = [i for i in range(self.board_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(width[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]

            if i < 10:
                string_rep += f' {i} |'
            else:
                string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(width[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.board_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


def play():
    board_size = 0
    num_bombs = 0
    while board_size < 5 or board_size > 20:
        board_size = int(
            input('What do you want the number of bombs to be [Between 5 and 20]: '))

    while num_bombs < 5 or num_bombs > 20:
        num_bombs = int(
            input('What do you want the number of bombs to be [Between 5 and 20]: '))

    board = Board(board_size, num_bombs)
    safe = True

    while len(board.dug) < board.board_size ** 2 - num_bombs:
        print(board)

        user = re.split(
            ',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user[0]), int(user[-1])
        if row < 0 or row >= board.board_size or col < 0 or col >= board.board_size:
            print("Wrong placement")
            continue
        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print('You win')
    else:
        print('Game over')
        board.dug = [(r, c) for r in range(board.board_size)
                     for c in range(board.board_size)]
        print(board)


play()
