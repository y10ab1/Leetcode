# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         self.n,self.m = len(board), len(board[0])
#         self.board = board
#         trie = set()
#         for word in words:
#             for i in range(len(word)+1):
#                 trie.add(word[:i])
#         self.s = set(words)
        
#         ans = set()
        
#         for si in range(self.n):
#             for sj in range(self.m):
#                 self.dfs(set(),trie,si,sj,"",ans)
#                 if len(ans) == len(words):
#                     return list(ans)
                            
#         return list(ans)
    
#     def dfs(self, seen, trie, i, j, prefix, res):
#         seen.add((i,j))
#         if len(prefix)>9:
#             return
#         word = prefix+self.board[i][j]
#         if word in self.s:
#             res.add(word)

        
#         d = [(1,0),(-1,0),(0,-1),(0,1)]
#         for dx, dy in d:
#             if 0<=i+dx<self.n and 0<=j+dy<self.m and word in trie and not (i+dx,j+dy) in seen:
#                 self.dfs(seen.copy(), trie, i+dx, j+dy, word, res)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m, n = len(board), len(board[0])
        res, trie, has = list(), dict(), set()
        
        for r in range(m):
            for c in range(n - 1):
                has.add(board[r][c] + board[r][c + 1])
        for r in range(m - 1):
            for c in range(n):
                has.add(board[r][c] + board[r + 1][c])
        
        for word in words:
            for i in range(len(word) - 1):
                a, b = word[i], word[i + 1]
                if a + b not in has and b + a not in has:
                    break
            else:
                cur = trie
                for c in word:
                    if c not in cur: cur[c] = {}
                    cur = cur[c]
                cur['*'] = word
        
        def dfs(r, c, node):
            node = node[board[r][c]]
            if '*' in node:
                res.append(node['*'])
                del node['*']
            rc = board[r][c]
            board[r][c] = '*'
            for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
                dr, dc = r + i, c + j
                if dr < 0 or dr >= m or dc < 0 or dc >= n \
                or board[dr][dc] not in node:
                    continue
                dfs(dr, dc, node)
                if len(node[board[dr][dc]]) == 0:
                    del node[board[dr][dc]]
            board[r][c] = rc
        
        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)
        
        return res