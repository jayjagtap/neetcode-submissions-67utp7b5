class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        delimiter = "#"
        for s in strs:
            encoded += str(len(s)) + delimiter + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        Time Complexity: O(n)
        Space Complexity: worst case O(m)
        """
        print(s)
        strs = []
        delimiter = "#"
        i = 0
        
        length = ""
        while i < len(s): 
            if s[i] == "#":
                length = int(length)
                # Read word
                word = ""
                for j in range(i+1, i+1+length):
                    word += s[j]
                strs.append(word)
                i = i+length+1
                length = ""
            else:
                length += s[i]
                i += 1
        
        return strs
            
