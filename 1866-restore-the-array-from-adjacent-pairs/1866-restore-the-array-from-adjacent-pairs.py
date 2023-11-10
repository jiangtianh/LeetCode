class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res = [math.inf] * (len(adjacentPairs) + 1)

        graph = collections.defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        start = math.inf
        for key in graph:
            if len(graph[key]) == 1:    
                start = key
                break 
        print(graph)
        seen = {start}
        res[0] = start
        prev = start
        for i in range(1, len(res)):
            newNum = -math.inf
            for val in graph[prev]:
                if val not in seen:
                    newNum = val
                    break

            seen.add(newNum)
            res[i] = newNum
            prev = newNum
        
        return res




            
