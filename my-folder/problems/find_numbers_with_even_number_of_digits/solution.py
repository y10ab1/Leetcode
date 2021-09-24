class Solution:
    
    
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            if compute_digit(nums[i])%2 == 0:
                cnt +=1 
        return cnt
    
def compute_digit(num):
        cnt=0
        while num!=0:
            num//=10
            cnt+=1
        return cnt
         
    