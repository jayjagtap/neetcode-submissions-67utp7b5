class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        positive case:
        racecar carrace
        traverse racecar and update hashmap
        {
        'r': 2,
        'a': 2,
        'c': 2,
        'e': 1
        }
        Now while testing anagram:
        1. Check if char is present in set, if not return False
        2. If yes, decrement by 1, if the count reaches 0, remove the char

        At the end check if map is empty, is yes, return true

        Corner cases
        empty string, long string "" , "csdcdscdscds" Handle it at start, if only 1 string is empty
        both strings empty, still return False

        """

        freq = defaultdict(int)

        for char in s:
            freq[char]+=1
        
        for char in t:
            freq[char]-=1
            if freq[char] == 0:
                freq.pop(char)
        
        return not freq




