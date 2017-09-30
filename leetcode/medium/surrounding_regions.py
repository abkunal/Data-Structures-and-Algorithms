""" Surrounded Regions - https://leetcode.com/problems/surrounded-regions

    Given a 2D board containing 'X' and 'O' (the letter O), capture all 
    regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    For example,
    X X X X
    X O O X
    X X O X
    X O X X
    After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # This is the code of a fellow coder. Couldn't get through this problem
        # so checked his code, understood it and tried it myself

        # split rows of string into list
        for i in range(len(board)):
            board[i] = list(board[i])
        
        # find the "O" at the corner of the board and converge inwards where
        # "O" can be reached from the corner.
        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0,k), (m-1,k), (k,0), (k,n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "S"
                save += (i,j-1), (i,j+1),(i-1,j),(i+1,j)

        # replace "S" with "O" and all the other characters with "X"
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]


# a = Solution()
# b = ["XXXX","XOOX","XXOX","XOXX"]
# c = ["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]
# a.solve(["XOXX","OXOX","XOXO","OXOX"])
# a.solve(["OXXOX","XOOXO","XOXOX","OXOOO","XXOXO"])