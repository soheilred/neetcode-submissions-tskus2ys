class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        res = ["JFK"]
        for f, t in tickets:
            graph[f].append(t)


        def dfs(city):
            if len(res) == len(tickets) + 1:
                return True

            if city not in graph: # len(graph[city]) == 0
                return False
            
            # while graph[city]:
            targets = list(graph[city])
            for i, target in enumerate(targets):
                # cur = graph[city].pop()
                graph[city].pop(i)
                res.append(target)
                if dfs(target):
                    return True
                res.pop()
                graph[city].insert(i, target)

            return False
        
        dfs("JFK")
            
        return res
        
            # targets = list(graph[city])

            # for target in targets:
            #     if dfs(target, seen):
            #         return True
            #     heapq.heappush(minH, target)
            #     graph[city].remove(target)