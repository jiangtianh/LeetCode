class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        counter = {}
        k = len(nums)

        li = []

        for i in range(len(nums)):
            for num in nums[i]:
                li.append((num, i))
        heapq.heapify(li)
        
        temp = collections.deque()
        res = None
        while li:
            num, idx = heapq.heappop(li)
            if idx in counter:
                counter[idx] += 1
            else:
                counter[idx] = 1
            
            temp.append([num, idx])
        
                

            while len(counter) == k:
                if res == None:
                    res = [temp[0][0], temp[-1][0]]
                else:
                    if res[1]-res[0] > temp[-1][0] - temp[0][0]:
                        res = [temp[0][0], temp[-1][0]]
                num, idx = temp.popleft()
                counter[idx] -= 1
                if counter[idx] == 0:
                    counter.pop(idx)
        
        return res