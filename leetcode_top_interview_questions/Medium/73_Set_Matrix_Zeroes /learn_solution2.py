class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        first_row_zero, first_col_zero = False, False
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                first_row_zero = True
                break
        
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                first_col_zero = True
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])
          
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        

        if first_row_zero:
            matrix[0] = [0] * len(matrix[0])
        
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        