class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter1 = collections.Counter(basket1)
        counter2 = collections.Counter(basket2)
        allCosts = set(list(counter1.keys()) + list(counter2.keys()))
        basket1Move = []
        basket2Move = []

        smallest = math.inf

        for n in allCosts:
            smallest = min(smallest, n)
            if (counter1[n] + counter2[n]) % 2 != 0:
                return -1

            elif counter1[n] > counter2[n]:
                basket1Move.extend([n] * ((counter1[n] - counter2[n]) // 2))
            elif counter1[n] < counter2[n]:
                basket2Move.extend([n] * ((counter2[n] - counter1[n]) // 2))

        basket1Move.sort()
        basket2Move.sort()
        basket1Move = collections.deque(basket1Move)
        basket2Move = collections.deque(basket2Move)
        res = 0
        while basket1Move and basket2Move:
            if 2 * smallest < basket1Move[0] and 2 * smallest < basket2Move[0]:
                basket1Move.pop()
                basket2Move.pop()
                res += 2 * smallest
            elif basket1Move[0] < basket2Move[0]:
                res += basket1Move.popleft()
                basket2Move.pop()
            else:
                res += basket2Move.popleft()
                basket1Move.pop()

        return res

        
