class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        n = len(s1)
        s2_count = Counter(s2[:n])
        if s1_count == s2_count: return True

        for i in range(n, len(s2)):
            s2_count[s2[i]] += 1
            s2_count[s2[i - n]] -= 1
        
            if s1_count == s2_count:
                return True

        return False
            

        