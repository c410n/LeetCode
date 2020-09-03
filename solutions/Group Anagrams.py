class Solution:
    def groupAnagrams(self, S: List[str]) -> List[List[str]]:
        D = collections.defaultdict(list)
        
        for i,e in enumerate(S):
            K = sorted(e)
            D[tuple(K)].append(e)
            
        return D.values()