# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heightAtLevel = collections.defaultdict(list)
        levelOfNode = collections.defaultdict(int)
        heightOfNode = collections.defaultdict(int)

        def f(node, level):
            if not node:
                return 0
            
            currentNodeHeight = max(f(node.left, level+1), f(node.right, level+1))

            levelOfNode[node.val] = level
            heightOfNode[node.val] = currentNodeHeight
            if len(heightAtLevel[level]) <= 1:
                heightAtLevel[level].append(currentNodeHeight)
                heightAtLevel[level].sort(reverse=True)
            else:
                if currentNodeHeight > heightAtLevel[level][0]:
                    heightAtLevel[level][1] = heightAtLevel[level][0]
                    heightAtLevel[level][0] = currentNodeHeight
                elif currentNodeHeight > heightAtLevel[level][1]:
                    heightAtLevel[level][1] = currentNodeHeight
            return currentNodeHeight + 1
        f(root, 0)

        res = []
        for q in queries:
            level = levelOfNode[q]
            height = heightOfNode[q]
            if heightAtLevel[level][0] == height:
                if len(heightAtLevel[level]) == 1:
                    res.append(level - 1)
                else:
                    res.append(level + heightAtLevel[level][1])
            else:
                res.append(level + heightAtLevel[level][0])
        return res