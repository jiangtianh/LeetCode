class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        count = 0
        temp = []
        li = []

        for num in nums:
            c = bin(num).count('1')
            if c != count:
                li.append(temp)
                temp = []
                count = c
            temp.append(num)
        li.append(temp)

        for i in range(2, len(li)):
            prevMax = max(li[i-1])
            curMin = min(li[i])
            if prevMax > curMin:
                return False

        return True
        
