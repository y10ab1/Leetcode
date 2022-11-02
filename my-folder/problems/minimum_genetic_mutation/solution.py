class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        
        s = set()
        q = deque([(start,0)])
        while q:
            cur,step = q.popleft()
            s.add(cur)
            for gene in bank:
                differ = 0
                for c,g in zip(cur,gene):
                    if c!=g:
                        differ+=1
                    if differ>1:
                        break
                        
                if gene == end and differ < 2:
                    return step+1
                
                if differ < 2 and not gene in s:
                    q.append((gene,step+1))
        return -1