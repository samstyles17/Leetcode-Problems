import collections
"""
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board:list[list[str]])->bool:
        # 1. We have to check for duplicates in the current column
        cols = collections.defaultdict(set) #Here Key will be col no. and value will be set of unique integers
        # 2. Check for duplicates in current row
        rows = collections.defaultdict(set) # here key will be row no. and value will be set of unique integers.
        # 3. Check for duplicates in each of 3x3 grid.
        # Logic- To represent the grids we use indexes. row&col (0,1,2) represent one grid, row&col(3,4,5) represent second grid , row&col(6,7,8) represent third grid.
        # first grid has to be represented through 0,0 second, 1,1 and third 2,2. for that we use integer division on actual coordinates with denominator 3. to get representative coordinates.
        squares = collections.defaultdict(set) # here key = (r//3, c//3) and value is hash set
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True