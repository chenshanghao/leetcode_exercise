class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkSquare(board)
        
    def checkRows(self, board):
        for row in board:
            hashmap = {}
            for cell in row:
                if cell == ".":
                    continue
                elif cell in hashmap:
                    return False
                else:
                    hashmap[cell] = True
        return True
    
    def checkCols(self, board):
        for i in range(9):
            hashmap = {}
            for j in range(9):
                cell = board[j][i]
                if cell == ".":
                    continue
                elif cell in hashmap:
                    return False
                else:
                    hashmap[cell] = True
        return True
    
    def checkSquare(self, board):
        for i in range(3):
            for j in range(3):
                hashmap = {}
                for row in range(3):
                    for col in range(3):
                        cell = board[3 * i + row][3 * j + col]
                        if cell == ".":
                            continue
                        elif cell in hashmap:
                            return False
                        else:
                            hashmap[cell] = True
        return True