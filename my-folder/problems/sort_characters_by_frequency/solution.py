class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        sd = sorted([(v,k) for (k,v) in d.items()], reverse = True)
        sd = dict((k,v) for (v,k) in sd)
        ans = ''
        for c in sd:
            ans+=c*d[c]
        return ans