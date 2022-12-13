class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def find(s:int, index:int, comb:list):
            
            if s > target:
                return []
            
            if s == target:
                return [comb]
            
            ret = []
            for i in range(index, len(candidates)):
                ret+=find(s+candidates[i], i, comb+[candidates[i]])
            return ret
        return find(0,0,[])

