class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def f(i):
            if i == len(books):
                return 0
            curWidth = 0
            maxHeight = 0
            res = math.inf
            while i < len(books):
                thickness, height = books[i]
                if curWidth + thickness > shelfWidth:
                    break
                else:
                    maxHeight = max(maxHeight, height)
                    curWidth += thickness
                    res = min(res, f(i+1) + maxHeight)
                i += 1
            return res

        return f(0)