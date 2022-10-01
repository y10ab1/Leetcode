class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter([c for c in word])
        for w in cnt:
            cnt[w]-=1
            if len(set([v for v in cnt.values() if v > 0]))==1:
                return True
            else:
                cnt[w]+=1
                
                
        return False