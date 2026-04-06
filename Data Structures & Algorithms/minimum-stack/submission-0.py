class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_elem = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_so_far = self.min_elem[-1] if len(self.min_elem) > 0 else float('inf')
        self.min_elem.append(min(val, min_so_far))
        

    def pop(self) -> None:
        self.min_elem.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_elem[-1]
        
