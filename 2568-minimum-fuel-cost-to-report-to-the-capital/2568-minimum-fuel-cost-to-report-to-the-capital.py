class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(list)

        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        self.total = 0
        def f(n):
            visited.add(n)
            numPeople = 1
            for neighbor in graph[n]:
                if neighbor not in visited:
                    numPeopleFromNeighbor = f(neighbor)
                    numPeople += numPeopleFromNeighbor
            self.total += math.ceil(numPeople / seats)
            return numPeople

        visited.add(0)
        for neighbor in graph[0]:
            f(neighbor)
        
        return self.total

