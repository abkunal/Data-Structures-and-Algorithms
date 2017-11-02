"""

    Given an 2D board, count how many battleships are in it. The battleships 
    are represented with 'X's, empty slots are represented with '.'s. 
    You may assume the following rules:

    You receive a valid board, made of only battleships or empty slots.
    Battleships can only be placed horizontally or vertically. 
    In other words, they can only be made of the shape 1xN (1 row, N columns) 
    or Nx1 (N rows, 1 column), where N can be of any size.
    At least one horizontal or vertical cell separates between two 
    battleships - there are no adjacent battleships.
    
    Example:
    
    X..X
    ...X
    ...X
    
    In the above board there are 2 battleships.
    
    Invalid Example:
    
    ...X
    XXXX
    ...X
    
    This is an invalid board that you will not receive - as battleships 
    will always have a cell separating between them.
    
    Follow up:
    Could you do it in one-pass, using only O(1) extra memory and 
    without modifying the value of the board?
"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def contains_up(sea, i, j):
            if i == 0:
                return False
            elif sea[i-1][j] == 'X':
                return True
            return False

        def contains_right(sea, i, j):
            if j == len(sea[i]) - 1:
                return False
            elif sea[i][j+1] == 'X':
                return True
            return False

        ships = 0

        for i in range(len(board)):
            j = 0
            while j < len(board[i]):
                if board[i][j] == 'X':
                    if (not contains_up(board, i, j)) and (not contains_right(board, i, j)):
                        ships += 1
                    elif (not contains_up(board, i, j)) and contains_right(board, i, j):
                        ships += 1
                        while j < len(board[i]) and board[i][j] == 'X':
                            j += 1
                j += 1
        return ships


# a = Solution()
# print(a.countBattleships([["X","X","X","X"],[".",".",".","."],["X","X",".","X"]]))