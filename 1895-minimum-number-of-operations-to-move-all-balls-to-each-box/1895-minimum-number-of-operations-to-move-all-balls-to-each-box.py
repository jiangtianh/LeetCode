class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = [0] * n
        right = [0] * n
        res = [0] * n

        steps, count = 0, 0
        for i in range(n):
            box = boxes[i]
            steps += count
            left[i] = steps
            if box == "1":
                count += 1
        
        steps, count = 0, 0
        for i in range(n-1, -1, -1):
            box = boxes[i]
            steps += count
            right[i] = steps
            if box == "1":
                count += 1
        
        for i in range(n):
            res[i] = left[i] + right[i]
        return res