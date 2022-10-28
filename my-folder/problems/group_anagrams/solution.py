class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            d[tuple(sorted(Counter(s).items()))].append(s)
        return d.values()
    
        # O(len(strs)*100log(100))