# If cycle isn't reached within 4 steps it's never reached
class Solution:
    def rotate(self, D, M):
        if D == [0, 1]:
            if M == -1:
                D[0] = -1
                D[1] = 0
            elif M == 1:
                D[0] = 1
                D[1] = 0
        elif D == [0, -1]:
            if M == -1:
                D[0] = 1
                D[1] = 0
            elif M == 1:
                D[0] = -1
                D[1] = 0
        elif D == [1, 0]:
            if M == -1:
                D[0] =  0
                D[1] = 1
            elif M == 1:
                D[0] = 0
                D[1] = -1
        elif D == [-1, 0]:
            if M == -1:
                D[0] = 0
                D[1] = -1
            elif M == 1:
                D[0] = 0
                D[1] = 1
        # exception
    
    def performMove(self, D, P, c):
        # print(D, c)
        if c == 'G':
            P[0] += D[0]
            P[1] += D[1]
        elif c == 'R':
            self.rotate(D, 1)
        else: # 'L'
            self.rotate(D, -1)
        # print(D, P)
        
    def isRobotBounded(self, I: str) -> bool:
        P = [0,0]
        D = [0,1] # x,y / North
        
        for j,c in enumerate(I):
            self.performMove(D, P, c)
            
        
        if P == [0, 0] or D != [0,1]:
            return True                
        
        return False