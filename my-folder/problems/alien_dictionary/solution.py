class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = defaultdict(int)
        adjlist = defaultdict(list)
        
        for word in words:
            for c in word:
                indegree[c] = 0
        
    
        
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(min(len(word1), len(word2))):
                
                if word1[j] != word2[j]:
                    adjlist[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1
                    break
                elif word1[j] == word2[j]:
                    if j+1 == len(word2) and j+1 < len(word1):
                        return ""
                

        
        ans = ""
        queue = [key for key in indegree if indegree[key] == 0]
        while queue:
            new_queue = []
            for i in range(len(queue)):
                char = queue.pop()
                ans += char
                for child in adjlist[char]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        new_queue.append(child)
            
            queue = new_queue
            
        if len(ans) != len(indegree):
            return ""
        
        return ans
                    