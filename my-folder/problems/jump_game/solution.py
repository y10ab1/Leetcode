class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums) == 1):
            return True
        
        dp = []
        for _ in range(len(nums)):
            dp.append(-1)
        
        for i in range(1, len(nums)):
            check_id = i-1
            while dp[i] == -1 and check_id >= 0:
                if check_id > 0 and dp[check_id] == -1:
                    return False 
                elif nums[check_id] >= i-check_id:
                    dp[i] = check_id
                else:
                    check_id = dp[check_id]
                    
        if dp[-1] == -1:
            return False
        else:
            return True
                
            