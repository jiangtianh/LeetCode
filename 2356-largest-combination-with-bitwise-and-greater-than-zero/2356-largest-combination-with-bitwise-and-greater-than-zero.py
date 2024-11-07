class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit = [0] * 24

        for num in candidates:
            binary = bin(num)[2:]
            
            for i in range(-1, -len(binary) - 1, -1):
                if binary[i] == "1":
                    bit[i] += 1
        
        return max(bit)