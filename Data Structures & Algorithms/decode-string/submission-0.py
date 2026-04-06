class Solution:
    def decodeString(self, s: str) -> str:
        val = 0
        stack = []

        for c in s:
            if c.isdigit():
                val = val * 10 + int(c)

            elif c == '[':
                stack.append(val)
                val = 0
            
            elif c == ']':
                cur = ''
                print(stack)
                while isinstance(stack[-1], str):
                    # print(stack)
                    cur = stack.pop() + cur
                mult = stack.pop()
                # print(mult, cur)
                res = ''.join([cur for _ in range(mult)])
                stack.append(res)
            
            else:
                stack.append(c)
        
        return ''.join(stack)
        

'''
s = "2[a3[b]]c"
val = 0
stack = [2, a, 3, b]
for c in s:
    if c.isdigit():
        val = val * 10 + int(c)
    
    if c == '[':
        stack.append(val)
        val = 0
    
    if c == ']':
        while stack.string:
            cur = stack.pop() + cur -> b
        mul = stack.pop() -> 3
        res = cur * mul
        stack.push(res)

stack = [2, a, bbb]


'''