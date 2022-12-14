class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        
        h = sorted([((x**2+y**2)**(0.5),x,y) for x,y in points])
        
        return [[x,y] for _,x,y in h[:k]]
