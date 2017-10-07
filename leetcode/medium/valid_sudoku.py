""" Valid Sudoku - https://leetcode.com/problems/valid-sudoku

    Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

    The Sudoku board could be partially filled, where empty cells are 
    filled with the character '.'.


    A partially filled sudoku which is valid.

    Note:
    A valid Sudoku board (partially filled) is not necessarily solvable. 
    Only the filled cells need to be validated.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # validate rows
        for row in range(len(board)):
            nums = set()
            for col in range(len(board)):
                if board[row][col] != '.':
                    if board[row][col] in nums:
                        return False
                    else:
                        nums.add(board[row][col]) 

        for row in range(len(board)):
            nums = set()
            for col in range(len(board)):
                if board[col][row] != '.':
                    if board[col][row] in nums:
                        return False
                    else:
                        nums.add(board[col][row])

        boxes = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for box in boxes:
            nums = set()
            for j in range(box[0], box[0]+3):
                for k in range(box[1], box[1]+3):
                    if board[j][k] != '.':
                        if board[j][k] in nums:
                            return False
                        else:
                            nums.add(board[j][k])
        return True