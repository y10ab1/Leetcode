class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        dp = [set()]
        for word in arr:
            if len(set(word)) < len(word): continue
            a = set(word)
            for c in dp:
                if a & c: continue
                dp.append(a | c)
        return max([len(i) for i in dp])
            