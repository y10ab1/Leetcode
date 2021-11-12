class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        tickets = sorted(tickets)[::-1]
        for t in tickets:
            d[t[0]].append(t[1])
        ans = []
        def dfs(r):
            while d[r]:
                dfs(d[r].pop())
            ans.append(r)
        dfs("JFK")
        return ans[::-1]
        
