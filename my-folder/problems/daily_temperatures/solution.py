class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            while len(s) > 0 and temperatures[i] > temperatures[s[-1]]:
                ans[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return ans
            