class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        testBoard = {}

        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    if board[x][y] in testBoard:
                        return False
                        testBoard[board[x][y]] = 1
            testBoard = {}
        
        
        for x in range(9):
            for y in range(9):
                if board[y][x] != '.':
                    if board[y][x] in testBoard:
                        return False
                    testBoard[board[y][x]] = 1
            testBoard = {}
        
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                for _x in range(x, x + 3):
                    for _y in range(y, y + 3):
                        if board[_y][_x] != '.':
                            if board[_y][_x] in testBoard:
                                return False
                            testBoard[board[_y][_x]] = 1
                testBoard = {}
        return True