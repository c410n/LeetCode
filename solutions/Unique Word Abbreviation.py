class ValidWordAbbr:
    S = None
    D = None
    
    def getDicDefinition(self, word):
        if len(word) < 3:
            return word
        else:
            term = word[:1] + str(len(word[1:len(word)-1])) + word[len(word)-1:]
            return term
    
    def __init__(self, dictionary: List[str]):
        self.S = collections.defaultdict(int)
        self.D = set()
        for a in dictionary:
            term = self.getDicDefinition(a)
            if not a in self.D:
                self.D.add(a)
                self.S[term] += 1

    def isUnique(self, word: str) -> bool:
        term = self.getDicDefinition(word)
        if word not in self.D and term not in self.S:
            return True
        if term in self.S and word in self.D:
            if self.S[term] > 1:
                return False
            else:
                return True
        return False

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)