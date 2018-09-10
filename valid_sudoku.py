"""
Problem:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if validate_row(board) and validate_sub(board) and validate_column(board):
            return True
        return False

def validate_row(board):
    for i in range(9):
        temp = []
        for j in range(9):
            if board[i][j].isdigit() and board[i][j] in temp:
                return False
            temp.append(board[i][j])
    return True

def validate_column(board):
    for i in range(9):
        temp = []
        for j in range(9):
            if board[j][i].isdigit() and board[j][i] in temp:
                return False
            temp.append(board[j][i])
    return True

def validate_sub(board):
    sub_mat = {1: [[0, 0], [0, 1], [0, 2],
                  [1, 0], [1, 1], [1, 2],
                  [2, 0], [2, 1], [2, 2]],
               2: [[0, 3], [0, 4], [0, 5],
                  [1, 3], [1, 4], [1, 5],
                  [2, 3], [2, 4], [2, 5]],
               3: [[0, 6], [0, 7], [0, 8],
                  [1, 6], [1, 7], [1, 8],
                  [2, 6], [2, 7], [2, 8]],

               4: [[3, 0], [3, 1], [3, 2],
                   [4, 0], [4, 1], [4, 2],
                   [5, 0], [5, 1], [5, 2]],
               5: [[3, 3], [3, 4], [3, 5],
                   [4, 3], [4, 4], [4, 5],
                   [5, 3], [5, 4], [5, 5]],
               6: [[3, 6], [3, 7], [3, 8],
                   [4, 6], [4, 7], [4, 8],
                   [5, 6], [5, 7], [5, 8]],

               7: [[6, 0], [6, 1], [6, 2],
                   [7, 0], [7, 1], [7, 2],
                   [8, 0], [8, 1], [8, 2]],
               8: [[6, 3], [6, 4], [6, 5],
                   [7, 3], [7, 4], [7, 5],
                   [8, 3], [8, 4], [8, 5]],
               9: [[6, 6], [6, 7], [6, 8],
                   [7, 6], [7, 7], [7, 8],
                   [8, 6], [8, 7], [8, 8]],
               }
    for i in range(1, 10):
        temp = []
        for j in sub_mat[i]:
            if board[j[0]][j[1]].isdigit() and board[j[0]][j[1]] in temp:
                return False
            temp.append(board[j[0]][j[1]])
    return True



if __name__ == "__main__":
    s = Solution()
    input = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9",".",".",".",".",".","6","."],
  [".",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(s.isValidSudoku(input))
