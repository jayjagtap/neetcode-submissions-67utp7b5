class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = defaultdict(int)

        for char in s:
            freq[char]+=1
        
        for char in t:
            freq[char]-=1
            if freq[char] == 0:
                freq.pop(char)
        
        return not freq




