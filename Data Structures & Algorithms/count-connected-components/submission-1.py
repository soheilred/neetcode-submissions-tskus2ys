class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj_list = [[] for _ in range(n)]
        count = 0

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        print(adj_list)

        def dfs(cur, path):
            if cur in seen:
                return 
            
            seen.add(cur)
            path.append(cur)
            for n in adj_list[cur]:
                dfs(n, path)
            path.pop()
        

        for i in range(n):
            if i not in seen:
                dfs(i, [])
                count += 1
        
        return count
                
