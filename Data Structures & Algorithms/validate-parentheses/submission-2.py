class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {
            "{": "}", 
            "[": "]", 
            "(": ")", 
        }

        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if len(stack) == 0 or c != mapping[stack.pop()]:
                    return False
        return len(stack) == 0

        