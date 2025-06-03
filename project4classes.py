#gamestate.py


class Faller:
    def __init__(self, col: int, tiles: list[str]):
        self._col = col
        self._tiles = tiles

    def tiles(self) -> list[str]:
        'returns the tiles'
        return self._tiles

    def col(self) -> int:
        'returns the col the tiles repreenting the jewels are to be placed in'
        return self._col

class Board:
    def __init__(self, rows: int, cols: int, game_board: list[str], status_board: list[list[str]]):
        self._rows = rows
        self._cols = cols
        self._game_board = game_board
        self._status_board = status_board
        if len(game_board) == 3:
            for r in range(self._rows):
                game_row = []
                status_row = []
                for c in range(self._cols):
                    game_row.append(' ')
                    status_row.append(' ')
                self._game_board.append(game_row)
                self._status_board.append(status_row)
        else:
            if len(self._status_board) != len(self._game_board):
                for r in range(self._rows):
                    status_row = []
                    for c in range(self._cols):
                        status_row.append(' ')
                    self._status_board.append(status_row)
        
    def rows(self) -> int:
        'returns rows of board'
        return self._rows

    def cols(self) -> int:
        'returns columns of board'
        return self._cols

    def game_over(self) -> bool:
        'determines if the game is over'
        for c in range(self._cols):
            for r in range(0, 3):
                if self._game_board[r][c] != ' ':
                    return True
        return False

    def get_board(self) -> list[str]:
        'returns the game board'
        return self._game_board

    def get_status_board(self) -> list[str]:
        'returns the status board'
        return self._status_board

    def remove_matches(self) -> None:
        'cleans up any matches after being deleted'
        for r in range(self._rows + 3):
            for c in range(self._cols):
                if self._status_board[r][c] == '*':
                    self._game_board[r][c] = ' '

    def contains_matches(self) -> bool:
        'determines whether there are any matches on the board at an instant'
        for r in range(self._rows + 3):
            for c in range(self._cols):
                if self._status_board[r][c] == '*':
                    return True
        return False
                    
    def print(self) -> None:
        'prints the board'
        
        endline = ' '
        for r in range(0, self._rows + 3):
            line = '|'
            for c in range(self._cols):
                if self._status_board[r][c] == '[':
                    line += '[' + self._game_board[r][c] + ']'
                else:
                    line += self._status_board[r][c] + self._game_board[r][c] + self._status_board[r][c]
            line += '|'
            print(line)
        for c in range(self._cols):
            endline += '---'
        print(endline + ' ')


class InvalidInput(Exception):
    def __init__(self):
        pass
