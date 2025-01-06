class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                graph[c] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
                

        if not graph:
            return words[0]
        res = []
        visited = set()
        path = set()

        def f(c):
            if c in visited:
                return 0 
            visited.add(c)
            if c not in graph:
                res.append(c)
                return 0
            path.add(c)
            for nei in graph[c]:
                if nei in path:
                    return -1
                if f(nei) == -1:
                    return -1                
            path.remove(c)
            res.append(c)
        
        for c in graph:
            if c not in visited:
                if f(c) == -1:
                    return ""
        
        res.reverse()
        return "".join(res)
                
                