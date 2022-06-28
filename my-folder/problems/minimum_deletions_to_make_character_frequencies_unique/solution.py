class Solution:
    def minDeletions(self, s: str) -> int:
        num_cnt = defaultdict(int)
        alp_cnt = defaultdict(int)
        ans = 0
        for c in s:
            alp_cnt[c] +=1

        for v in sorted(alp_cnt.values()):
            i = 0
            while num_cnt[v-i] != 0 and i < v:
                i+=1
            num_cnt[v-i] += 1
            ans+=i
        return ans
            