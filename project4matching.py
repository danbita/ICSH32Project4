#project4matching.py

from project4classes import *

def horizontal_matches(board: Board) -> Board:
    'marks any horizontal matches'
    
    game_board = board.get_board()
    status_board = board.get_status_board()
    for r in range(3, board.rows() + 3):
        for c in range(board.cols() - 2):
            if game_board[r][c] == game_board[r][c+1] and game_board[r][c+1] == game_board[r][c+2] and game_board[r][c] != ' ':
                status_board[r][c] = '*'
                status_board[r][c+1] = '*'
                status_board[r][c+2] = '*'
                for index in range(c+3, board.cols()):
                    if game_board[r][index] == game_board[r][c]:
                        status_board[r][index] = '*'
                    else:
                        break

    return Board(board.rows(), board.cols(), game_board, status_board)

def vertical_matches(board: Board) -> Board:
    'marks any vertical matches'
    
    game_board = board.get_board()
    status_board = board.get_status_board()
    for c in range(board.cols()):
        for r in range(board.rows() + 1):
            if game_board[r][c] == game_board[r+1][c] and game_board[r+1][c] == game_board[r+2][c] and game_board[r][c] != ' ':
                status_board[r][c] = '*'
                status_board[r+1][c] = '*'
                status_board[r+2][c] = '*'
                for index in range(r + 3, board.rows() + 3):
                    if game_board[index][c] == game_board[r][c]:
                        status_board[index][c] = '*'
                    else:
                        break

    return Board(board.rows(), board.cols(), game_board, status_board)

def diagonal_matches(board: Board) -> Board:
    'marks any diagonal matches'
    
    game_board = board.get_board()
    status_board = board.get_status_board()
    for r in range(3, board.rows()+1):
        for c in range(board.cols()-2):
            if game_board[r][c] == game_board[r+1][c+1] and game_board[r+1][c+1] == game_board[r+2][c+2] and game_board[r][c] != ' ':
                status_board[r][c] = '*'
                status_board[r+1][c+1] = '*'
                status_board[r+2][c+2] = '*'
                index = 3
                while(r + index <= board.rows() and c + index <= board.cols() - 3):
                    if game_board[r+index][c+index] == game_board[r][c]:
                        status_board[index][c] = '*'
                    else:
                        break

    for r in range(3, board.rows()+1):
        for c in range(board.cols()-1, 1, -1):
            if game_board[r][c] == game_board[r+1][c-1] and game_board[r+1][c-1] == game_board[r+2][c-2] and game_board[r][c] != ' ':
                status_board[r][c] = '*'
                status_board[r+1][c-1] = '*'
                status_board[r+2][c-2] = '*'
                index = 3
                while(r + index <= board.rows() and c + index <= board.cols() - 3):
                    if game_board[r+index][c-index] == game_board[r][c]:
                        status_board[index][c] = '*'
                    else:
                        break

    return Board(board.rows(), board.cols(), game_board, status_board)


def reset_status_board(board: Board) -> Board:
    'resets the status board to a clean state'
    
    status_board = board.get_status_board()
    for r in range(board.rows() + 3):
        for c in range(board.cols()):
            status_board[r][c] = ' '
    return Board(board.rows(), board.cols(), board.get_board(), status_board)

def freeze(board: Board) -> Board:
    'freezes any locked pieces'
    
    board = reset_status_board(board)
    board = horizontal_matches(board)
    board = vertical_matches(board)
    board = diagonal_matches(board)
    return board
