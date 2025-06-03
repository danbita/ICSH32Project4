#project4movement.py

from project4classes import *

def faller_locked(board: Board) -> bool:
    'determines whether a faller is in a locked state'
    
    row = -1
    game_board = board.get_board()
    status_board = board.get_status_board()
    for c in range(board.cols()):
        for r in range(board.rows()+2, 2, -1):
            if status_board[r][c] == '|':
                row = r
                break
    if row != -1:
        return True
    return False

def rotate_board(board: Board) -> Board:
    'rotate a faller'
    col = 0
    row = 0
    game_board = board.get_board()
    status_board = board.get_status_board()
    for c in range(board.cols()):
        for r in range(board.rows()+2, 2, -1):
            if status_board[r][c] == '[' or status_board[r][c] == '|':
                row = r
                col = c
                break
                
    temp = game_board[row][col]
    game_board[row][col] = game_board[row-1][col]
    game_board[row-1][col] = game_board[row-2][col]
    game_board[row-2][col] = temp
    return Board(board.rows(), board.cols(), game_board, status_board)


def move_left(board: Board) -> Board:
    'moves a faller to the left'
    
    col = 0
    row = 0
    game_board = board.get_board()
    status_board = board.get_status_board()
    for c in range(board.cols()):
        for r in range(board.rows()+2, 2, -1):
            if status_board[r][c] == '[' or status_board[r][c] == '|':
                row = r
                col = c
                break

    if col == 0:
        return board
      
    if game_board[row][col-1] == ' ' and game_board[row-1][col-1] == ' ' and game_board[row-2][col-1] == ' ':
        game_board[row][col-1] = game_board[row][col]
        game_board[row-1][col-1] = game_board[row-1][col]
        game_board[row-2][col-1] = game_board[row-2][col]
        
        status_board[row][col-1] = '['
        status_board[row-1][col-1] = '['
        status_board[row-2][col-1] = '['

        game_board[row][col] = ' '
        game_board[row-1][col] = ' '
        game_board[row-2][col] = ' '
        
        status_board[row][col] = ' '
        status_board[row-1][col] = ' '
        status_board[row-2][col] = ' '
        
    return Board(board.rows(), board.cols(), game_board, status_board)

def move_right(board: Board) -> Board:
    'moves a faller to the right'
    
    col = 0
    row = 0
    game_board = board.get_board()
    status_board = board.get_status_board()
    for c in range(board.cols()):
        for r in range(board.rows()+2, 2, -1):
            if status_board[r][c] == '[' or status_board[r][c] == '|':
                row = r
                col = c
                break

    if col == board.cols()-1:
        return board
                
    if game_board[row][col+1] == ' ' and game_board[row-1][col+1] == ' ' and game_board[row-2][col+1] == ' ':
        game_board[row][col+1] = game_board[row][col]
        game_board[row-1][col+1] = game_board[row-1][col]
        game_board[row-2][col+1] = game_board[row-2][col]
        
        status_board[row][col+1] = '['
        status_board[row-1][col+1] = '['
        status_board[row-2][col+1] = '['

        game_board[row][col] = ' '
        game_board[row-1][col] = ' '
        game_board[row-2][col] = ' '
        
        status_board[row][col] = ' '
        status_board[row-1][col] = ' '
        status_board[row-2][col] = ' '
        
    return Board(board.rows(), board.cols(), game_board, status_board)

def has_landed(board: Board) -> Board:
    'determines whether a faller has fallen or not, and changes the status board accoadingly'
    col = 0
    row = 0
    game_board = board.get_board()
    status_board = board.get_status_board()
    for c in range(board.cols()):
        for r in range(board.rows()+2, 2, -1):
            if status_board[r][c] == '[':
                row = r
                col = c
                break

    status_board[row][col] = '|'
    status_board[row-1][col] = '|'
    status_board[row-2][col] = '|'
    return Board(board.rows(), board.cols(), game_board, status_board)
        
def tick(board: Board) -> Board:
    'ticks time as the game goes on'
    col = 0
    row = 0
    game_board = board.get_board()
    status_board = board.get_status_board()
    for c in range(board.cols()):
        for r in range(board.rows()+2, 2, -1):
            if status_board[r][c] == '[':
                row = r
                col = c
                break

    if row == board.rows() + 2:
        return has_landed(board)
    elif game_board[row+1][col] != ' ':
        return has_landed(board)
    
    game_board[row+1][col] = game_board[row][col]
    game_board[row][col] = game_board[row-1][col]
    game_board[row-1][col] = game_board[row-2][col]
    game_board[row-2][col] = ' '

    status_board[row+1][col] = '['
    status_board[row][col] = '['
    status_board[row-1][col] = '['
    status_board[row-2][col] = ' '

    if row+1 == board.rows() + 2:
        return has_landed(Board(board.rows(), board.cols(), game_board, status_board))

    if game_board[row+2][col] != ' ':
        return has_landed(Board(board.rows(), board.cols(), game_board, status_board))
    
    return Board(board.rows(), board.cols(), game_board, status_board)

def place_faller(board: Board, faller: Faller) -> Board:
    'places a faller'
    new_board = board.get_board()
    game_board = []
    col = faller.col() - 1
    status_board = board.get_status_board()
    if new_board[3][col] == ' ':
        new_board[1][col] = faller.tiles()[0]
        new_board[2][col] = faller.tiles()[1]
        new_board[3][col] = faller.tiles()[2]
        status_board[1][col] = '['
        status_board[2][col] = '['
        status_board[3][col] = '['
    else:
        new_board[0][col] = faller.tiles()[0]
        new_board[1][col] = faller.tiles()[1]
        new_board[2][col] = faller.tiles()[2]
        status_board[0][col] = '['
        status_board[1][col] = '['
        status_board[2][col] = '['
    return Board(board.rows(), board.cols(), new_board, status_board)

def handle_new_piece(line: str, board: Board, faller: Faller) -> Board:
    'handles new fallers'
    if line == 'F':
        if faller == None:
            return
        else:
            return place_faller(board, faller)
    else:
        print(line)
        print('error')

def is_fallen(board: list[list[str]]) -> bool:
    'determines whether a piece has fallen'
    
    for c in range(len(board[0])):
        last_found_tile = board[len(board)-1][c]
        for r in range(len(board)-2, 2, -1):
            if board[r][c] != ' ':
                if last_found_tile == ' ':
                    return False
            last_found_tile = board[r][c]
    return True

def drop_pieces(board: Board) -> Board:
    'drops each jewel as low as possible'
    
    game_board = board.get_board()
    new_board = []
    for r in range(len(game_board)):
        line = list(game_board[r])
        new_board.append(line)
    while not is_fallen(new_board):
        for c in range(len(new_board[0])):
            for r in range(len(new_board)-1, 2, -1):
                if new_board[r][c] == ' ':
                    new_board[r][c] = new_board[r-1][c]
                    new_board[r-1][c] = ' '
    return Board(board.rows(), board.cols(), new_board, board.get_status_board())
 
