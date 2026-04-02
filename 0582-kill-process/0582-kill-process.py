class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = collections.defaultdict(list)

        for i in range(len(pid)):
            graph[ppid[i]].append(pid[i])

        self.res = []

        def f(node):
            self.res.append(node)
            for child in graph[node]:
                f(child)
        
        f(kill)

        return self.res