class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        intervals = [item for items in intervals for item in items]
        l = bisect.bisect_left(intervals, newInterval[0])
        r = bisect.bisect_right(intervals, newInterval[1])
        ans+=intervals[:l]
        if l%2==0:
            ans.append(newInterval[0])
        if r%2==0:
            ans.append(newInterval[1])
        ans+=intervals[r:]

        ans = [[ans[i],ans[i+1]] for i in range(0,len(ans),2)]
        return ans
