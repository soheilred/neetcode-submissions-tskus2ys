class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i: set() for i in range(n)}
        seen = set()

        for n1, n2 in edges:
            if n1 == n2:
                return False
            adj_list[n1].add(n2)
            adj_list[n2].add(n1)
        
        print(adj_list)

        def dfs(parent, cur, path):
            print(cur, path, seen)
            if cur in path:
                return False
            
            if cur in seen:
                return True
            
            seen.add(cur)
        
            path.append(cur)
            for n in adj_list[cur]:
                if n == parent:
                    continue

                if dfs(cur, n, path) == False:
                    return False
            
            path.pop()
            return True
        if dfs(0, 0, []) == False:
            return False
        # for i in range(n):
            # if i not in seen and dfs(i, i, []) == False:
                # return False

        for i in range(n):
            if i not in seen:
                return False
        return True

        