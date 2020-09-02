class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        if words == None or word1 == None or word2 == None:
            return None
        if len(words) < 2:
            return None
        i = 0
        m = sys.maxsize
        if word1 == word2:
            a = collections.deque([sys.maxsize,sys.maxsize])
            while i < len(words):
                if words[i] == word1:
                    a.append(i)
                    a.popleft()
                    if m > abs(a[0] - a[1]):
                        m = abs(a[0] - a[1])
                i += 1
        else:
            w1h = hash(word1)
            w2h = hash(word2)
            a = {w1h: sys.maxsize, w2h: sys.maxsize}
            while i < len(words):
                if words[i] == word1:
                    a[w1h] = i
                    if m > abs(a[w1h] - a[w2h]):
                        m = abs(a[w1h] - a[w2h])
                elif words[i] == word2:
                    a[w2h] = i
                    if m > abs(a[w1h] - a[w2h]):
                        m = abs(a[w1h] - a[w2h])
                i += 1
        return m