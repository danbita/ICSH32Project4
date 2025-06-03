#project4.py

from project4classes import *
from project4movement import *
from project4matching import *

def set_up_board() -> Board:
    'sets up the board'
    
    rows = int(input())
    cols = int(input())
    board_status = input()
    empty_row = []
    empty_list = []
    for i in range(cols):
        empty_row.append(' ')
        empty_list.append(' ')
    contents = [empty_row, empty_row, empty_row]
    status_board = [empty_list, empty_list, empty_list]
    if board_status == 'EMPTY':
        return Board(rows, cols, contents, status_board)
    elif board_status == 'CONTENTS':
        for i in range(rows):
            contents.append(input())
        return Board(rows, cols, contents, status_board)
    

def get_faller(info: list[str]) -> Faller:
    'identifies a faller from an input'
    
    col = int(info[0])
    chars = info[1:]
    return Faller(col, chars)

def is_col_empty(board: list[list[str]], col: int) -> bool:
    'determines whether a column is empty or not'
    
    for r in range(3, len(board)):
        if board[r][col] == ' ':
            return True
    return False


def run() -> None:
    'runs the program'
    
    board = set_up_board()
    board = drop_pieces(board)
    board = horizontal_matches(board)
    board = vertical_matches(board)
    board = diagonal_matches(board)
    board.remove_matches()
    board = reset_status_board(board)
    board = drop_pieces(board)
    board.print()
    count = 0
    faller = None
    while not board.game_over():
        line = input()
        if line == 'Q':
            break
        if line[0] == 'F':
            faller = get_faller(line.split()[1:])
        board = handle_new_piece(line[0], board, faller)
        board.print()
        end_game = False
        print_cleaned = False
        while True:
            command = input()
            need_to_print = True
            if faller_locked(board):
                if command == 'R':
                    board = rotate_board(board)
                elif command == '<':
                    board = move_left(board)
                elif command == '>':
                    board = move_right(board) 
                elif command == '':
                    board = freeze(board)
                    flag = False
                    if board.contains_matches():
                        board.print()
                        flag = True
                    board.remove_matches()
                    board = reset_status_board(board)
                    board = drop_pieces(board)
                    need_to_print = True
                    if flag == True and input() == '':
                        pass
                    break
            elif command == 'R':
                board = rotate_board(board)
            elif command == '<':
                board = move_left(board)
            elif command == '>':
                board = move_right(board)
            elif command == '':
                board = tick(board)
            elif command == 'Q':
                end_game = True
                break
            if need_to_print:
                board.print()
        board.print()
        if end_game:
            break
        if board.game_over():
            print('GAME OVER')
        

if __name__ == '__main__':
    run()
