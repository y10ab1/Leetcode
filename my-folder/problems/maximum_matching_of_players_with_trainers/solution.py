class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        hp = [-p for p in players]
        ht = [-t for t in trainers]
        heapq.heapify(hp)
        heapq.heapify(ht)      
        ans = 0
        while hp and ht:
            top = -heapq.heappop(hp)
            
            if top <= -ht[0]:
                heapq.heappop(ht)    
                ans+=1
                
        return ans