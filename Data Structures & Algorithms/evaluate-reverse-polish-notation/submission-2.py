class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))

            elif tokens[i] == "-":
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(y - x)

            elif tokens[i] == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))

            elif tokens[i] == "/":
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(y / x)
            
            else:
                stack.append(tokens[i])
        
        # while stack:
        # return sum(stack)
        print(stack)
        return int(stack.pop())



        