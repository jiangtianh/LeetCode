class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indices)
        li = [(indices[i], sources[i], targets[i]) for i in range(n)]
        li.sort(key=lambda x: x[0]) 
        
        j = 0
        i = 0
        res = []

        while i < len(s):
            found = False
            while j < len(li) and li[j][0] <= i:
                source, target = li[j][1], li[j][2]
                if li[j][0] == i and s[i:i+len(source)] == source:
                    res.append(target)
                    i += len(source)
                    found = True
                j += 1

            if not found:
                res.append(s[i])
                i += 1

        return "".join(res)