class Solution:
    def normalizePosition(self, newPos, l):
        if newPos >= l or newPos < 0:
            newPos = newPos % l
        return newPos
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        f = {}
        b = {}
        for i in range(len(nums)):
            d = nums[i]
            pos = self.normalizePosition(i + d, len(nums))
            if d < 0:
                b[i] = pos
            else: # d > = 0
                f[i] = pos
        while len(b):
            print(b)
            s = set()
            a = next(iter(b.keys()))
            while a in b:
                if a in s:
                    if b[a] in b and b[a] == b[b[a]]:
                        b = {x: y for x, y in b.items() if x not in s}
                        s.clear()
                        if len(b):
                            a = next(iter(b.keys()))
                        else:
                            break   
                    else:
                        return True
                else:
                    s.add(a)
                    if b[a] in b:
                        a = b[a]
                    else:
                        b = {x: y for x, y in b.items() if x not in s}
                        s.clear()
                        if len(b):
                            a = next(iter(b.keys()))
                        else:
                            break    
        while len(f):
            print(f)
            s = set()
            a = next(iter(f.keys()))
            while a in f:
                if a in s:
                    if f[a] in f and f[a] == f[f[a]]:
                        f = {x: y for x, y in f.items() if x not in s}
                        s.clear()
                        if len(f):
                            a = next(iter(f.keys()))
                        else:
                            break   
                    else:
                        return True
                else:
                    s.add(a)
                    if f[a] in f:
                        a = f[a]
                    else:
                        f = {x: y for x, y in f.items() if x not in s}
                        s.clear()
                        print("f: ", f)
                        if len(f):
                            a = next(iter(f.keys()))
                        else:
                            break             
                
        return False