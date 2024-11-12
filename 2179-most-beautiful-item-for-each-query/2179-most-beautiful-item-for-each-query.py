class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key= lambda x: (x[0], -x[1]))
        prices = [item[0] for item in items]

        curMaxBeauty = 0
        for i in range(len(items)):
            price, beauty = items[i][0], items[i][1]
            curMaxBeauty = max(curMaxBeauty, beauty)
            items[i][1] = curMaxBeauty

        res = []
        for q in queries:
            idx = bisect_left(prices, q)

            if idx == 0:
                if items[idx][0] > q:
                    res.append(0)
                else:
                    res.append(items[idx][1])
            elif idx != len(items) and items[idx][0] == q:
                res.append(items[idx][1])
            else:
                res.append(items[idx-1][1])
                
        return res