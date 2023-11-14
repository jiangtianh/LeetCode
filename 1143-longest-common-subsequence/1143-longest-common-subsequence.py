class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def f(p1, p2):

            if p1 >= len(text1) or p2 >= len(text2):
                return 0
            
            option1 = f(p1+1, p2)

            if text1[p1] == text2[p2]:
                option2 = f(p1+1, p2+1) + 1
            else:
                option2 = f(p1 + 1, p2)

            option3 = f(p1, p2 + 1)

            return max(option1, option2, option3)

        return f(0, 0)

