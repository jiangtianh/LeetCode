class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(force):
            i = 0
            count = 1
            prev = position[0]
            for _ in range(m-1):
                while i < len(position) and position[i] < prev + force:
                    i += 1
                if i < len(position):
                    count += 1
                    prev = position[i]
                else:
                    return False
            return True 

        l = 1
        r = position[-1] - position[0]
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res
