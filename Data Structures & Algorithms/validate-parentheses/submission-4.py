class Solution:
    def isValid(self, s: str) -> bool:
        pars = {"(": ")", "[": "]", "{": "}"}
        q = deque()
        for c in s:
            if c in "({[":
                q.append(c)
            else:
                if not q:
                    return False
                last = q.pop()
                if pars[last] != c:
                    return False
        return True if not q else False
        