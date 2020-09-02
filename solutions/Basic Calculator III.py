import math, queue

class OPMeta(type):
    def __getitem__(self, key):
        if key == '+':
            return OP.ADD
        elif key == '-':
            return OP.REM
        elif key == '*':
            return OP.MUL
        elif key == '/':
            return OP.DIV

class OP(object, metaclass = OPMeta):   
    ADD = 'A'
    REM = 'R'
    MUL = 'M'
    DIV = 'D'    
            
# Shunting-yard algorithm
class Solution:
    def process(self, s: str, i: [int]) -> int:
        ops = collections.deque()
        args = collections.deque()
        is_definition_expected = True
        sign = True
        while i[0] < len(s):
            # print(i[0], s[i[0]], is_definition_expected)            
            if s[i[0]].isspace():
                i[0] += 1
                continue
            ncache = ""            
            if is_definition_expected == True and i[0] < len(s) and s[i[0]] == "-":
                # print("S")
                sign = False
                i[0] += 1
                continue                
            while i[0] < len(s) and s[i[0]].isdigit():                
                ncache += s[i[0]]
                i[0] += 1
            if len(ncache) > 0:
                if sign == False:
                    args.append(-int(ncache))
                else:
                    args.append(int(ncache))
                ncache = ""
                is_definition_expected = False
                sign = True
                continue
            if s[i[0]] in ['+', '-', '*', '/']:
                ops.append(OP[s[i[0]]])
                i[0] += 1
                is_definition_expected = True
                continue
            if s[i[0]] == '(':
                i[0] += 1
                is_definition_expected = False
                if sign == False:
                    args.append(-self.process(s, i))
                else:
                    args.append(self.process(s, i))
                sign = True
                i[0] += 1
                continue
            if s[i[0]] == ')':
                break
        # print(args, ops)
        holder = None
        args_n = collections.deque()
        ops_n = collections.deque()
        while len(args) and len(ops):
            op = ops.popleft()
            # print(op)
            if op == 'A':
                args_n.append(args.popleft())
                ops_n.append(op)
            elif op == 'R':
                args_n.append(args.popleft())
                ops_n.append(op)
            elif op == 'M':
                holder = math.floor(args.popleft() * args.popleft())
                args.insert(0, holder)
            elif op == 'D':
                l = args.popleft()
                r = args.popleft()
                holder = math.floor(l / r)
                args.insert(0, holder)
        if len(args):
            args_n.append(args.pop())
        # print(args, ops, args_n, ops_n)
        left = args_n.popleft()
        while len(args_n) and len(ops_n):
            op = ops_n.popleft()
            if op == 'A':
                left += args_n.popleft()
            elif op == 'R':
                left -= args_n.popleft()
        return left
            
    def calculate(self, s: str) -> int:
        i = dict()
        i[0] = 0
        return self.process(s, i)