class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for st in strs:
            d = {}
            for i in range(97,123):
                d[chr(i)] = 0
            for s in st:
                d[s]+=1
            A = ''
            for dk,dv in d.items():
                A += dk+f'{dv}'
            if not ans.get(A):
                ans[A] = [st]
            else:
                ans[A] += [st]
           
        return ans.values()
    '''
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
                    
    '''
                    
                    