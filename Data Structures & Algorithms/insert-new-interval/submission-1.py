class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0
        n = len(intervals)
        res = []
        # new_s, new_e = float('inf'), -float('inf')
        new_s, new_e = newInterval[0], newInterval[1]
        j = 0

        # for start, end in intervals:
        while j < n:
            start, end = intervals[j]
            if start <= new_s <= end or start <= new_e <= end:
                new_s = min(new_s, start)
                new_e = max(new_e, end)
            
            if new_s > end:
                res.append([start, end])

            elif new_e < start:
                break

            j += 1
        
        res.append([new_s, new_e])
        while j < n:
            res.append(intervals[j])
            j += 1
        
        return res

        
        


