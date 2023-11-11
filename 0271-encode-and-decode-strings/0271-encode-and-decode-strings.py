class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "/"
            res += s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "/": 
                length += s[i]
                i += 1
            
            length = int(length)
            temp = ""
            while length:
                i += 1
                temp += s[i]
                length -= 1
            i += 1
            res.append(temp)
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))