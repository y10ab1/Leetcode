class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = dict([(w[::-1],idx) for idx,w in enumerate(words)])
        ans = []
        for idx,w in enumerate(words):
            for i in range(len(w)+1):
                pre,pos = w[:i], w[i:]
                
                if pre in d and idx!=d[pre] and pos == pos[::-1]:
                    ans.append([idx,d[pre]])
                if i>0 and pos in d and idx!=d[pos] and pre == pre[::-1]:
                    ans.append([d[pos],idx])
        return ans