class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = defaultdict(int)
        edgeTo = defaultdict(list)
        leaves = []
        ans = 0
        for i, j in relations:
            edgeTo[i].append(j)
            indegree[j] += 1
        
        for i in range(1,n+1):
            if indegree[i] == 0:
                leaves.append(i)
                
        if len(leaves) == 0:
            return -1
        
        while leaves:
            ans += 1
            newLeaves = []
            for i in leaves:
                for j in edgeTo[i]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        newLeaves.append(j)
                        
            leaves = newLeaves
            
        for i in indegree:
            if indegree[i] != 0:
                return -1
            
        return ans