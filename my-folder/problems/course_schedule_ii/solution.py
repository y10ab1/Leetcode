class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        seen = defaultdict(bool)
        visited = defaultdict(bool)
        
        root = defaultdict(int)
        for i in range(numCourses):
            root[i] = True
        finished = []
        ans = []
        
        for child, parent in prerequisites:
            edges[parent].append(child)
            
            root[child] = False
        
        def dfs(node):
            seen[node] = True
            for child in edges[node]:
                if seen[child] and not visited[child]:
                    return False
                if not visited[child]:
                    if not dfs(child):
                        return False
            visited[node] = True
            finished.append(node)
            return True
            
        
        for i in range(numCourses):
            if not visited[i] and root[i]:
                if not dfs(i):
                    return []
        
        while finished:
            ans.append(finished.pop())
        if len(ans) != numCourses:
            return []
        return ans
                    
            