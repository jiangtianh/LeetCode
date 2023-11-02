class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = "abcdefghijklmnopqrstuvwxyz"
        st = set()
        for c in s:
            st.add(c)

        for c in sentence:
            if c in st:
                st.remove(c)
        
        return len(st) == 0