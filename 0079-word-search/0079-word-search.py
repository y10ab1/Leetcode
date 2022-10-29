class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def dfs(i:int,j:int,idx:int):
            if board[i][j] != word[idx]:
                return False
            elif idx == len(word)-1:
                return True
            
            board[i][j] += board[i][j]
            d = [(0,1),(0,-1),(1,0),(-1,0)]
            for x,y in d:
                if 0 <= x+i < n and 0 <= y+j < m and len(board[x+i][y+j])==1 and idx+1 <len(word):
                    if dfs(x+i,y+j,idx+1):
                        return True
            board[i][j] = board[i][j][0]
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False