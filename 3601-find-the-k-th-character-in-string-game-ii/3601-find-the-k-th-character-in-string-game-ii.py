class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shift = 0
        length = 1

        for op in operations:
            length *= 2

        for op in reversed(operations):
            length //= 2
            if k > length:
                k -= length
                if op == 1:
                    shift += 1
        
        return chr((shift % 26) + ord('a'))