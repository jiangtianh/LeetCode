class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        res = [0] * n

        graph = collections.defaultdict(list)
        
        for i in range(1, n):
            graph[parents[i]].append(i)

        print(graph)

        def f(node):
            if len(graph[node]) == 0:
                res[node] = n - 1
                return 1
            
            left = f(graph[node][0])
            
            if len(graph[node]) == 1:
                top = (n - 1 - left)
                if top == 0:
                    top = 1
                res[node] = top * left
                return left + 1
            else:
                right = f(graph[node][1])
                top = (n-1-left-right) 
                if top == 0:
                    top = 1
                res[node] = left * right * top
                return left + right + 1
        f(0)
        print(res)
        return res.count(max(res))

