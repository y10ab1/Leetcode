class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        
        uf = {c:c for c in string.ascii_lowercase}
        
        for a,e,_,b in equations:
            if e == "=":
                uf[find(a)] = find(b)
                
        for a,e,_,b in equations:
            if e == "!" and find(a)==find(b):
                return False
        
        return True

            
            