class Solution:
    R = None
    def retrieveAbbreviations(self, b, word):
        for i in range(1, len(word)) if (len(b) > 0 and b[len(b)-1].isnumeric()) else range(len(word)):
            for s in range(1, len(word)+1-i):
                self.R.append(b + word[:i] + str(len(word[i:i+s])) + word[i+s:])
                if len(word[i+s:]) > 0:
                    self.retrieveAbbreviations(b + word[:i] + str(len(word[i:i+s])), word[i+s:])
    
    def generateAbbreviations(self, word):
        self.R = [word]
        self.retrieveAbbreviations("", word)
        return self.R