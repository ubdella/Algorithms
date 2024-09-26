class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = [i for i in range(len(accounts))]
        def find(a):
            while par[a] != a:
                a = find(par[a])
            return par[a]
        def union(a, b):
            parA, parB = find(a), find(b)
            par[parB] = parA
        
        emailToIndices = defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                emailToIndices[account[j]].append(i)
        
        for indices in emailToIndices.values():
            parIndex = indices[0]
            for index in indices[1:]:
                union(parIndex, index)
                
        accToEmails = defaultdict(set)
        
        for i, account in enumerate(accounts):
            accToEmails[find(i)].update(account[1:])
            
        return [[accounts[i][0]] + sorted(list(emails)) for i, emails in accToEmails.items()]