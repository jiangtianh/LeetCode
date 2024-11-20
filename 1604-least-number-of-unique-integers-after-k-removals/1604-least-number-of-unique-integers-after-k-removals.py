class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        totalInt = len(counter)

        countToInt = collections.defaultdict(list)
        for n in counter:
            countToInt[counter[n]].append(n)

        
        for count in sorted(countToInt.keys()):
            for n in countToInt[count]:
                if k >= count:
                    k -= count
                    totalInt -= 1
                else:
                    break

        return totalInt