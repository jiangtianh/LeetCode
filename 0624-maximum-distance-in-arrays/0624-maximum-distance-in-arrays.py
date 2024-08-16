class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = []
        largest = []

        for arr in arrays:
            smallest.append(arr[0])
            largest.append(arr[-1])
        res = 0
        
        s = smallest[0]
        l = largest[0]

        for i in range(1, len(arrays)):
            sm, lg = smallest[i], largest[i]

            takeLg = lg - s
            takeSm = l - sm

            if takeLg >= takeSm and takeLg > res:
                res = takeLg
                
            elif takeLg < takeSm and takeSm > res:
                res = takeSm
            s = min(s, sm)
            l = max(l, lg)



        return res
