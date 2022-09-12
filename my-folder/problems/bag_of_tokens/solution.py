class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l,r = 0,len(tokens)-1
        ans,tmp = 0,0
        tokens.sort()
        while l<=r:
            if tokens[l] <= power:
                power -= tokens[l]
                tmp += 1
                l+=1
            elif tmp:
                power += tokens[r]
                r-=1
                tmp-=1
            else:
                break
            ans = max(ans,tmp)
        return ans