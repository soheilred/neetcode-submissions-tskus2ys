class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        def bt(i, prev):
            if i == len(intervals):
                return 0
            
            res = bt(i+1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + bt(i+1, i))
            return res
        
        return len(intervals) - bt(0, -1)
        