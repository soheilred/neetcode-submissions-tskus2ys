class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N = min(len(word1), len(word2))
        res = ''
        
        for i in range(N):
            res += word1[i] + word2[i]
        
        if i < len(word1) - 1:
            res += word1[i+1:]

        elif i < len(word2) - 1:
            res += word2[i+1:]
        
        return res
        