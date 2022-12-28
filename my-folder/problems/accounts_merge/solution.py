class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def union(self, child, parent):
        self.parent[self.find(child)] = self.find(parent)
    def find(self, child):
        if child != self.parent[child]:
            self.parent[child] = self.find(self.parent[child])
        return self.parent[child]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        ans = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        ret = []
        for owner, emails in ans.items():
            ret.append([accounts[owner][0]]+sorted(emails))
        return ret
