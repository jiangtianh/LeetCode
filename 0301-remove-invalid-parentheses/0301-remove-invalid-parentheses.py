class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        self.d = collections.defaultdict(set)

        def f(i, deleted, temp, left, right):
            if right > left:
                return 
            
            if i == len(s):
                if left == right:
                    self.d[deleted].add(temp)
                return 

            if s[i] == "(" or s[i] == ")":
                
                # delete the current 
                f(i+1, deleted + 1, temp, left, right)

                #dont delete the current
                if s[i] == "(":
                    left += 1
                else:
                    right += 1

                f(i+1, deleted, temp + s[i], left, right)


            else:
                f(i+1, deleted, temp + s[i], left, right)
        
        f(0, 0, "", 0, 0)
        return self.d[min(self.d.keys())]