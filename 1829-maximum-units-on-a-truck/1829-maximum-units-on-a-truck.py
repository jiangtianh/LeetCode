class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        print(boxTypes)
        res = 0
        for i, [numOfBox, unit] in enumerate(boxTypes): 
             
            if truckSize >= numOfBox:
                res += numOfBox * unit
                truckSize -= numOfBox
            else:
                while truckSize > 0:
                    res += unit
                    truckSize -= 1
                break
        return res