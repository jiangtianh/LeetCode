class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(start,path):
            if start==len(num): return len(path)>2
            for end in range(start+1,len(num)+1):
                curr=num[start:end]
                if len(curr)>1 and curr[0]=='0': break
                curr=int(curr)
                if (len(path)<2 or curr==path[-1]+path[-2]) and backtrack(end,path+[curr]): 
                    return True
            return False
        return backtrack(0,[])