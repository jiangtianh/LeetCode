class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = collections.Counter(num)
        if counter["0"] == len(num):
            return "0"

        print(counter)
        largestSingleDigit = None 
        res = []


        for n in "9876543210":
            if n not in counter:
                continue
            if counter[n] % 2 == 1:
                if not largestSingleDigit:
                    largestSingleDigit = n
            res.append(n * (counter[n] // 2))
                
        left = "".join(res)
        i = 0
        while i < len(left) and left[i] == "0":
            i += 1
        left = left[i:]
        right = left[::-1]
        if largestSingleDigit:
            res = left + largestSingleDigit + right
        else:
            res = left + right

        return res