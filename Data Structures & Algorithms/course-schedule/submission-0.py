class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = [[] for _ in range(numCourses)]
        seen = [False] * numCourses

        for c, pre in prerequisites:
            adj_list[c].append(pre)

        def dfs(cur, path):
            if cur in path:
                return False
            
            if seen[cur] == True:
                return True

            seen[cur] = True
            
            if len(adj_list[cur]) == 0:
                return True
            
            for n in adj_list[cur]:
                path.append(cur)
                if dfs(n, path) == False:
                    return False
                path.pop()

            return True

        print(adj_list)
        
        for i in range(numCourses):
            print(seen)
            if dfs(i, []) == False:
                print(seen)
                return False
        
        for i in range(numCourses):
            if seen[i] == False:
                return False
        return True
        


        