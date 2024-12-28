class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = []
        total = sum(nums[:k-1])
        l = 0
        for r in range(k-1, len(nums)):
            total += nums[r]
            sums.append(total)
            total -= nums[l]
            l += 1
        
        self.d = {}
        
        def f(i, selected):
            if (i, selected) in self.d:
                return self.d[(i, selected)]
            if selected == 3:
                return 0, [-1]
            elif i >= len(sums):
                return -math.inf, [-1]
            
            select, selectIdx = f(i + k, selected + 1)
            noSelect, noSelectIdx = f(i+1, selected)

            if select + sums[i] >= noSelect:
                self.d[(i, selected)] = select + sums[i], [i] + selectIdx
            else:
                self.d[(i, selected)] = noSelect, noSelectIdx
                
            
            return self.d[(i, selected)]
        res, idx = f(0, 0)
        idx.pop()
        return idx 


