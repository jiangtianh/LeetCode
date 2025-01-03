class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = collections.defaultdict(list)

        for i in range(len(pid)):
            ID = pid[i]
            parent = ppid[i]
            graph[parent].append(ID)
            if ID not in graph:
                graph[ID] = []
        res = []

        def f(node):
            res.append(node)
            for child in graph[node]:
                f(child)
        
        f(kill)
        return res
                