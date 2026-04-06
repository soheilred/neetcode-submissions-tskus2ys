class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sign = +1

        for op in operations:
            print(stack)
            if op[0] == '-':
                op = op[1:]
                sign = -1

            if op.isdigit():
                stack.append(sign * int(op))
                sign = 1

            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            
            elif op == 'D':
                stack.append(stack[-1] * 2)
            
            elif op == 'C':
                stack.pop()
        
        return sum(stack)
        


'''
for op in ops:
    1. if op is digit, add it to stack
    2. if op is +, pop the stack twice and add the values
    3. if op is D, double the last element, append to the stack
    4. if op is C, pop the stack
'''