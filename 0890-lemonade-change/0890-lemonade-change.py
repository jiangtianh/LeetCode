class Solution:
    def lemonadeChange(self, nums: List[int]) -> bool:
        bills = {
            5: 0,
            10: 0,
            20: 0
        }

        def change(n):
            if n == 20:
                bills[20] += 1
                if bills[10] > 0 and bills[5] > 0:
                    bills[10] -= 1
                    bills[5] -= 1
                    return True
                elif bills[5] >= 3:
                    bills[5] -= 3
                    return True 
                else:
                    return False 

            elif n == 10:
                bills[10] += 1
                if bills[5] > 0:
                    bills[5] -= 1
                    return True
                return False
            elif n == 5:
                bills[5] += 1
                return True 

        for n in nums:
            if not change(n):
                return False 
        return True