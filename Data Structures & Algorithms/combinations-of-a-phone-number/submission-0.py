class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0: return []
        res = []
        digit_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def bt(ind, combo):
            if ind == n:
                res.append(''.join(combo))
                return
            
            for i in range(len(digit_dict[digits[ind]])):
                c = digit_dict[digits[ind]][i]
                combo.append(c)
                bt(ind+1, combo)
                combo.pop()
        
        bt(0, [])
        return res
        