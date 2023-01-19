class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = ""
        for s in strs:
            ret += f'{len(s)}'+'#'+s

        return ret
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """        
        strs = []
        offset = 0
        while s:
            for i in range(len(s)):
                if s[i] == '#':
                    offset = int(s[:i])
                    s = s[i+1:]
                    break
            strs.append(s[:offset])
            s = s[offset:]


        
        return strs
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))