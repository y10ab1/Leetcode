class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [(sqrt(x**2+y**2),x,y) for x,y in points]
        dis = sorted(dis)
        ans = []
        for i in range(k):
            ans.append([dis[i][1], dis[i][2]])
        return ans