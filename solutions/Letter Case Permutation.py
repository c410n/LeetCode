class Solution:
    def accumulate(self, S, l, ret):
        s = S[:l] + S[l].swapcase() + S[l+1:]
        ret.append(s)
        l += 1
        while l < len(s):
            if s[l].isalpha():
                self.accumulate(s, l, ret)
            l += 1
        
    def letterCasePermutation(self, S: str) -> List[str]:
        if S == None or len(S) < 1:
            return S
        
        ret = [S]
        l = 0
        while l < len(S):
            if S[l].isalpha():
                self.accumulate(S, l, ret)
            l += 1
        return ret