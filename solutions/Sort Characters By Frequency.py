class Solution:
    def frequencySort(self, s: str) -> str:
        s = collections.Counter(s)
        a = collections.defaultdict(list)
        for i in s:
            a[s[i]].append(i)
        keys = sorted(a.keys())[::-1]
        r = ""
        for i in keys:
            for ii in a[i]:
                r += ii * i
        return r