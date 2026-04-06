class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = [False] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for c, pre in prerequisites:
            adj_list[c].append(pre)
        
        print(adj_list)
        res = []

        def dfs(cur, path):
            if cur in path:
                return False
            
            if seen[cur]:
                return True
            
            seen[cur] = True
            path.append(cur)

            for n in adj_list[cur]:
                if dfs(n, path) == False:
                    return False

            path.pop()
            res.append(cur)
            return True

        candid = []
        for i in range(numCourses):
            if dfs(i, []) == False:
                return []
                
        return res
        
        
        return candid
        