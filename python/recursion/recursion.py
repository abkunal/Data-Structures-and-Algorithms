""" Some Recursive problems """

from graphics import *
import time

# ==============================================================================
# Permutations
count = 0
def rec_permu(sofar, rest):
    """ Recursively finds all the permutations of rest """
    global count
    if rest == "":
        count += 1
        #print(sofar)
    else:
        for i in range(len(rest)):
            nex = sofar + rest[i]
            rem = rest[:i] + rest[i+1:]
            rec_permu(nex, rem)

def list_permutations(s):
    rec_permu('', s)
# ==============================================================================

# ==============================================================================
# Subsets
def rec_subsets(sofar, rest):
    if rest == '':
        print(sofar)
    else:
        rec_subsets(sofar + rest[0], rest[1:])
        rec_subsets(sofar, rest[1:])

def list_subsets(s):
    rec_subsets('', s)
# ==============================================================================

# ==============================================================================
# Sudoku Solver

grid = [[9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,0,4,3,2,1],
        [1,2,3,4,5,6,7,8,9],
        [9,0,7,0,5,4,3,0,1],
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,5,4,3,2,1]]

def is_row_ok(grid):
    """ Returns True if in each row a number 1-9 appears most once. """
    for row in grid:
        rcount = [0 for i in range(9)]
        for num in row:
            if num != 0:
                if rcount[num-1] == 1:
                    return False
                else:
                    rcount[num-1] += 1
    return True

def is_col_ok(grid):
    """ Returns True if in each column a number 1-9 appears most once. """
    for i in range(9):
        ccount = [0 for k in range(9)]
        for j in range(9):
            if grid[j][i] != 0:
                if ccount[grid[j][i]-1] == 1:
                    return False
                else:
                    ccount[grid[j][i]-1] += 1
    return True
            
def is_box_ok(grid):
    """ Returns True if in each box a number 1-9 appears most once. """
    boxes = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    for box in boxes:
        bcount = [0 for i in range(9)]
        for j in range(box[0], box[0]+3):
            for k in range(box[1], box[1]+3):
                if grid[j][k] != 0:
                    if bcount[grid[j][k]-1] == 1:
                        return False
                    else:
                        bcount[grid[j][k]-1] += 1
    return True

def find_unassigned_location(grid):
    """ Finds a position which is still unoccupied """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i,j)
    return False

def no_conflicts(grid, row, col, num):
    """ Returns True if insertion of num doesn't violate the sudoku property """
    grid[row][col] = num
    resp = is_row_ok(grid) and is_col_ok(grid) and is_box_ok(grid)
    if resp is True:
        return True
    else:
        grid[row][col] = 0
        return False

def solve_sudoku(grid):
    """ Solves sudoku using recursive backtracking approach """
    ans = find_unassigned_location(grid)
    #print(ans)
    if ans is False:
        return True
    row, col = ans
    #print(row, col)
    for num in range(1, 10):
        if no_conflicts(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False


easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]


# ==============================================================================

# ==============================================================================
# N Queens Problem

board = [[0 for i in range(8)] for j in range(8)]

'''def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()
'''
def is_board_row_ok(board):
    for i in range(len(board)):
        seen = False
        for j in range(len(board)):
            if board[i][j] != 0:
                if seen is True:
                    return False
                else:
                    seen = True
    return True

def is_board_col_ok(board):
    for i in range(len(board)):
        seen = False
        for j in range(len(board)):
            if board[j][i] != 0:
                if seen is True:
                    return False
                else:
                    seen = True


def forward_diagonal(board, x, y):
    """ Looks for all the forward diagonal entries """
    i,j = (x-1,y-1)

    while i >= 0 and j >= 0:
        if board[i][j] != 0:
            return False
        i -= 1
        j -= 1

    i,j = (x+1,y+1)
    l = len(board)
    while i < l and j < l:
        if board[i][j] != 0:
            return False
        i += 1
        j += 1

    return True


def backward_diagonal(board, x, y):
    """ Looks for all the backward diagonal entries """
    i,j = (x+1, y-1)
    l = len(board)
    while 0 <= i < l and 0 <= j < l:
        if board[i][j] != 0:
            return False
        i += 1
        j -= 1

    i,j = (x-1, y+1)

    while 0 <= i < l and 0 <= j < l:
        if board[i][j] != 0:
            return False
        i -= 1
        j += 1

    return True


def is_safe(board, row, col):
    """ Checks if placing a queen at given row and column will be safe. """
    board[row][col] = "Q"
    
    # check for rows and columns
    row_col = is_board_row_ok(board) and is_board_col_ok(board)
    
    if row_col == False:
        board[row][col] = 0
        return False
    
    # Check for diagonals
    for i in range(len(board)):
        for j in range(len(board)): 
            if board[i][j] != 0:
                resp = forward_diagonal(board, i, j) and backward_diagonal(board, i, j)

                if resp is False:
                    board[row][col] = 0
                    return False
    board[row][col] = 0
    return True

def visual_board(board, win):
    x,y = (100, 100)
    for i in range(len(board)):
        for j in range(len(board)):
                if board[i][j] == "Q":
                    label = Text(Point(x+j*50+25, y+25), "Q")
                    label.setSize(18)
                    label.setTextColor("purple")
                    label.draw(win)
                else:
                    rect = Rectangle(Point(x+j*50,y), Point(x+j*50+50, y+50))
                    rect.setFill("white")
                    rect.draw(win)
        y += 50
                

def solve_queens(board, col, win):
    """ Solves the N-Queens problem using Recursive backtracking technique """
    if col >= len(board):
        return True
    else:
        for row_to_try in range(len(board)):
            if is_safe(board, row_to_try, col):
                board[row_to_try][col] = "Q"
                visual_board(board, win)
                time.sleep(0.02)
                if solve_queens(board, col + 1, win):
                    return True
                board[row_to_try][col] = 0
                visual_board(board, win)
                time.sleep(0.02)
    return False

def solve_board(board):
    """ Initializes the chess board """
    l = len(board)
    width = height = l * 100 + 200
    win = GraphWin("N-Queens", width, height)
    win.setBackground("white")

    x,y = (100, 100)
    big_rect = Rectangle(Point(x, y), Point(x+l*50, y+l*50))
    big_rect.draw(win)

    x,y = (100, 100)

    for i in range(l):
        for j in range(l):
            rect = Rectangle(Point(x+j*50, y), Point(x+j*50+50, y+50))
            rect.draw(win)
        y += 50
    
    visual_board(board, win)
    solve_queens(board, 0, win)
            
# ==============================================================================
