class Solution:
    def rewind(self, term):
        P = ord(term[0])
        R = []
        for i,e in enumerate(term[1:]):
            R.append((ord(e)-P) % 26)
            P = ord(e)
        return R
    
    def groupStrings(self, S: List[str]) -> List[List[str]]:
        D = collections.defaultdict(list)
        
        for i,e in enumerate(S):
            K = self.rewind(e)
            D[tuple(K)].append(e)
                    
        return D.values()
