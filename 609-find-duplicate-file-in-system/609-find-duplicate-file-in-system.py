class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup = defaultdict(list) # key->content/ values->path
        for path in paths:
            path = path.split(" ")
            for i in range(1,len(path)):
                file, content = path[i].split('(')
                
                dup[content].append("/".join([path[0],file]))
        ans = []
        for v in dup.values():
            if len(v) >1:
                ans.append(v)
        return ans
                    
        