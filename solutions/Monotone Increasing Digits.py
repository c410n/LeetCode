class Solution:         
    def convertNumIntoListOfNum(self, num):
        return [int(x) for x in str(num)]
    
    def convertListOfNumToNum(self, lnum):
        return int("".join([str(x) for x in lnum]))
    
    def reduce(self, seq):
        condition_detected = False
        i = 0
        while i < len(seq):
            if i-1 >= 0:
                if seq[i] < seq[i-1]:
                    seq[i-1] -= 1
                    condition_detected = True
                    break
            i += 1
            
        while i < len(seq):
            seq[i] = 9
            i += 1
            
        return condition_detected
    
    def monotoneIncreasingDigits(self, N):
        if N < 10: # 1. border case
            return N

        seq = self.convertNumIntoListOfNum(N) # constructing the monotone sequence

        while self.reduce(seq) == True:
            pass
        
        print(seq)
        return self.convertListOfNumToNum(seq)