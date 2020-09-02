class Solution:
    def backtrackBoard(self, board, y, x, st, R, level, S):
        if (y,x) in S:
            return
        # print("START", st.letter, st.data.keys())
        if y >= len(board) or y < 0 or x >= len(board[0]) or x < 0:
            # print("EXIT")
            return
        
        l = board[y][x]
        st = st.stepRetrieve(l)
        # print(y,x, (st.letter, st.word) if st != None else "None") # Best log candidate
        
        if st != None:            
            if st.word != None:
                R.add(st.word)
            S.add((y,x))
            # print("EXEC", y, x, l, st.letter, st.word, level)
            # print("1")
            self.backtrackBoard(board, y+1, x, st, R, level + 1, S)
            # print("2")
            self.backtrackBoard(board, y-1, x, st, R, level + 1, S)
            # print("3")
            self.backtrackBoard(board, y, x+1, st, R, level + 1, S)
            # print("4")
            self.backtrackBoard(board, y, x-1, st, R, level + 1, S)
            S.remove((y,x))
        # else:
        #     print("TOTAL RETURN")
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) < 1 or len(board) < 1 or len(board[0]) < 1:
            return []
        class ST:
            def __init__(self):
                super(ST, self).__init__()
                self.data = dict()
                self.isWord = False
                self.letter = None
                self.word = None
            def feed(self, W):
                C = self
                for i in range(len(W)):
                    if W[i] not in C.data:
                        C.data[W[i]] = ST()
                    C = C.data[W[i]]
                    C.letter = W[i]
                    if i == len(W)-1:
                        C.isWord = True
                        C.word = W                        
            def describe(self, level = 0):
                B = self
                for el in B.data:
                    # print(el, B.data[el].isWord, B.data[el].word, level)
                    B.data[el].describe(level + 1)
            def stepRetrieve(self, letter):
                if letter in self.data:
                    return self.data[letter]
                else:
                    return None
        
        st = ST()
        for w in words:
            st.feed(w)
        
        R = set()
        
        # st.describe()
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                # print("INITIAL")
                S = set()
                self.backtrackBoard(board, y, x, st, R, 0, S)   
                # print(S)
        
        return R