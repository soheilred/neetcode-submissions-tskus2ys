class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict.sort()
        memo = {}

        def bt(i):
            if i in memo:
                return memo[i]

            if i >= n:
                memo[i] = True
                return True
            
            for word in wordDict:
                m = len(word)
                if m <= n - i:
                    if s[i:i+m] == word and bt(i+m):
                        memo[i] = True
                        return True
                # else:
                    # memo[i] = False
                    # return False

            memo[i] = False
            return False
        
        return bt(0)

        