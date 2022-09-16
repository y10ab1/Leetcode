class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l,r=0,0
        maxlen=0
        char_set = defaultdict(int)
        while r<len(s):
            char_set[s[r]]+=1
            
            if len(char_set) <= 2:
                maxlen = max(maxlen,r-l+1)
            else:
                char_set[s[l]]-=1
                if char_set[s[l]] <= 0:
                    del char_set[s[l]]
                l+=1
            r+=1
        return maxlen