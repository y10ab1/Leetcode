class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start:int,last:str,last_cnt:int,left:int):
            if left < 0:
                return 101
            if start >= len(s):
                return 0
            if s[start] == last:
                increase = 1 if last_cnt == 1 or last_cnt == 9 or last_cnt == 99 else 0
                return increase + counter(start+1,s[start],last_cnt+1,left)
                
            else:
                # accept
                acc = 1 + counter(start+1,s[start],1,left)
                # deny
                deny = counter(start+1,last,last_cnt,left-1)
                return min(acc,deny)
        
        return counter(0,"",0,k)
                