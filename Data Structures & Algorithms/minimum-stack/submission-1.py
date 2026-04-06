class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elem = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_so_far = self.min_elem[-1] if len(self.min_elem) > 0 else float('inf')
        self.min_elem.append(min(min_so_far, val))
        
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_elem.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_elem[-1]
        
