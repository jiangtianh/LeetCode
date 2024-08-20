class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        d = collections.defaultdict(int)
        for s, e, c in segments:
            d[s] += c
            d[e] -= c
        
        start = None
        color = 0
        res = []

        for i in sorted(d.keys()):    
            if color and start:
                res.append([start, i, color])
            color += d[i]
            start = i
        return res