class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = collections.Counter()

        for i in range(1, n+1):
            digitSum = sum(int(c) for c in str(i))
            counter[digitSum] += 1
    
        res = 0
        largest = 0
        for digitSum in counter:
            if counter[digitSum] > largest:
                largest = counter[digitSum]
                res = 1
            elif counter[digitSum] == largest:
                res += 1
        
        return res