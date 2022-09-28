class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        return [[x,y] for _,x,y in sorted([((x**2+y**2)**(0.5),x,y) for x,y in points])[:k]]
