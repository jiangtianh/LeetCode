class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sortedNums = sorted(nums)
        numToGroup = {}
        currentGroup = 0
        numToGroup[sortedNums[0]] = currentGroup
        groupToList = collections.defaultdict(collections.deque)
        groupToList[currentGroup].append(sortedNums[0])

        for i in range(1, n):
            if sortedNums[i] - sortedNums[i-1] > limit:
                currentGroup += 1
            
            numToGroup[sortedNums[i]] = currentGroup
            groupToList[currentGroup].append(sortedNums[i])
        
        res = []
        for n in nums:
            group = numToGroup[n]
            res.append(groupToList[group].popleft())
        return res