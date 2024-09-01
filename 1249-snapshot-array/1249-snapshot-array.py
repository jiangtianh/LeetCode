class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.li = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.li[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        l = 0
        r = len(self.li[index]) - 1

        while l <= r:
            m = (l + r) // 2
            if self.li[index][m][0] <= snap_id:
                l = m + 1
            else:
                r = m - 1
        
        return self.li[index][r][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)