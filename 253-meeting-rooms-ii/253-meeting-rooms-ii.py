class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startheap = [i for i in intervals]
        endheap = []
        cnt=1
        
        heapq.heapify(startheap)
            
        while startheap:
            ss,se = heapq.heappop(startheap)
            if endheap:
                ee,es = endheap[0]
                if ss>=ee:
                    heapq.heappop(endheap)
                else:
                    cnt+=1
            heapq.heappush(endheap, (se,ss))
                

        return cnt
                