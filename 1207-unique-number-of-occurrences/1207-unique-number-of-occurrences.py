class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counter = collections.Counter(arr)
        
        s = set()
        for i in counter:
            if counter[i] not in s:
                s.add(counter[i])
            else:
                return False
        
        return True