class Solution:
    def candy(self, ratings: List[int]) -> int:
        LR = [1] * len(ratings)
        RL = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                LR[i] += LR[i-1]
        for i in reversed(range(0, len(ratings)-1)):
            if ratings[i] > ratings[i+1]:
                RL[i] += RL[i+1]
        print(RL, LR)
                
        ans = []
        for i, j in zip(RL, LR):
            ans.append(max(i,j))
            
        return sum(ans)
            
            