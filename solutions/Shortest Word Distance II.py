class WordDistance:    
    def __init__(self, words: List[str]):
        self.C = collections.defaultdict(list)
        for i in range(len(words)):
            self.C[words[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        WL = self.C[word1] 
        WR = self.C[word2]
        il = 0
        ir = 0
        R = []
        while il < len(WL) and ir < len(WR):
            if WL[il] < WR[ir]:
                R.append((WL[il], 'A'))
                il += 1
            else:
                R.append((WR[ir], 'B'))
                ir += 1
        
        R += [(x, 'A') for x in WL[il:]]
        R += [(x, 'B') for x in WR[ir:]]
        print(R)
        s = sys.maxsize
        D = {'A': sys.maxsize, 'B': sys.maxsize}
        for a in R:
            D[a[1]] = a[0]
            if s > abs(D['A'] - D['B']):
                s = abs(D['A'] - D['B'])
            
        return s

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)