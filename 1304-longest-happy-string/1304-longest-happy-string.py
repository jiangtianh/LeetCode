class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        li = []
        if a != 0:
            li.append([-a, 'a'])
        if b != 0:
            li.append([-b, 'b'])
        if c != 0:
            li.append([-c, 'c'])


        heapq.heapify(li)
        prev = None
        res = ''

        while li:
            count, c = heapq.heappop(li)
            count = -count

            if len(res) >= 2 and res[-1] == c and res[-2] == c:
                if not li:
                    break

                nextCount, nextC = heapq.heappop(li)
                res += nextC
                if nextCount + 1 < 0:
                    heapq.heappush(li, [nextCount+1, nextC])
                heapq.heappush(li, [-count, c])
            
            else:
                count -= 1
                res += c
                if count > 0:
                    heapq.heappush(li, [-count, c])
            
        return res