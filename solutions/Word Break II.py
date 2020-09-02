class Solution:
    def wbreak(self, W, R, s):
        if not s:
            return [[]]
        if s in R:
            return R[s]
        
        for e in range(1, len(s)+1):
            c = s[:e]
            if c in W:
                for ic in self.wbreak(W, R, s[e:]):
                    R[s].append([c] + ic)
                
        return R[s]
                
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # D = dict()
        # for w in wordDict:
        #     R = D
        #     i = 0
        #     while i < len(w):
        #         if w[i] not in R:
        #             R[w[i]] = [dict(), 0]
        #         R[w[i]][1] += 1
        #         R = R[w[i]][0]
        #         i += 1
        # print(D)
        
        R = collections.defaultdict(list)
        W = set(wordDict)
        
        self.wbreak(W, R, s)
        
        print(R)
        return [" ".join(r) for r in R[s]]