class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        def remove():        
            for _ in range(k):
                stack.pop()
        
        count = 1
        for c in s:
            if stack and stack[-1][0] == c:
                count = stack[-1][1] + 1
            else:
                count = 1
            
            stack.append((c, count))
            while stack and stack[-1][0] == c and stack[-1][1] == k:
      
                remove()
                count = 1
            
            



        
        return ''.join([s for s, c in stack])
            