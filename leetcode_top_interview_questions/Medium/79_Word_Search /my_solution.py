class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(board, m, n, i, j, word):
            if board[i][j] != word[0]:
                return False
            elif board[i][j] == word[0] and len(word) == 1:
                return True
            else:
                tmp = board[i][j]
                board[i][j] = "#"
                word = word[1:]
                
                if i-1>=0 and helper(board, m, n, i-1, j, word):
                    return True
                
                if i+1 < m and helper(board, m, n, i+1, j, word):
                    return True
                
                if j-1>=0 and helper(board, m, n, i, j-1, word):
                    return True
                
                if j+1<n and helper(board, m, n, i, j+1, word):
                    return True
                board[i][j] = tmp 
            return False
            
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if helper(board, m, n, i, j, word):
                    return True
        return False