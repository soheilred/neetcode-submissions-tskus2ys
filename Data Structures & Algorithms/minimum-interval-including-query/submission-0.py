class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q = sorted([(queries[i], i) for i in range(len(queries))])
        n = len(intervals)
        minH = []
        intervals.sort(key=lambda x: x[0])
        i = 0
        res = []

        # for j in range(len(q)):
            # query = q[j][0]
        for query, j in q:
            print(j, query)

            while i < n and intervals[i][0] <= query:
                heapq.heappush(minH, (intervals[i][1] - intervals[i][0] + 1, intervals[i]))
                i += 1
            
            while minH and minH[0][1][1] < query:
                heapq.heappop(minH)
            if minH:
                res.append((j, minH[0][0]))
            else:
                res.append((j, -1))
        
        # print(res)
        res.sort()
        return [res[i][1] for i in range(len(res))]
        