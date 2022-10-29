class Solution:
    def oddString(self, words: List[str]) -> str:
        s = defaultdict(list)
        for word in words:
            temp = []
            for i in range(1,len(word)):
                temp.append(ord(word[i])-ord(word[i-1]))
            s[tuple(temp)].append(word)
            
        for k,v in s.items():
            if len(v) == 1:
                return v[0]
                