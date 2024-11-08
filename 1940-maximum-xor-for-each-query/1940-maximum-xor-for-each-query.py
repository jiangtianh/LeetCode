class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        totalXor = 0
        for num in nums:
            totalXor ^= num


        n = len(nums)

        result = []
        for ithQuery in range(n):
            bit = ["0"] * (maximumBit)

            if ithQuery != 0:
                totalXor ^= nums[n-ithQuery]

            binary = list(bin(totalXor)[2:])
            binary.reverse()
            
            for i in range(len(bit)):
                if i >= len(binary) or binary[i] == "0":
                    bit[i] = "1"
            
            bit.reverse()

            res = int("".join(bit), 2)
            result.append(res)

        return result
            