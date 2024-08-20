class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        d = collections.defaultdict(int)
        MAX = 0
        for s, e, c in segments:
            d[s] += c
            d[e] -= c
            MAX = max(MAX, e)
        
        start = None
        color = 0
        res = []
        print(d)
        for i in range(1, MAX+1):
            if i in d:
                
                
                if color and start:
                    res.append([start, i, color])
                color += d[i]
                start = i
        return res