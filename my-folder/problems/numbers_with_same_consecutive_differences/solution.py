class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        for i in range(1,10):
            nums = [str(i)]
            while nums and len(nums[0])<n:
                temp =set()
                for num in nums:
                    s = int(num[-1])
                    if s+k < 10:
                        temp.add(num+str(s+k))
                    if s-k >= 0:
                        temp.add(num+str(s-k))
                nums = list(temp)

            res += nums
        return res