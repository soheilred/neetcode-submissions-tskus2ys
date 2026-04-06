class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i, t in enumerate(temperatures):
            j = i + 1
            while j < n:
                if temperatures[j] > t:
                    res[i] = j - i
                    break
                j += 1
            if j == n: res[i] = 0
        
        return res

        