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

        # Handle empty string cases

        if s == "" or t == "":
            return False
        
        char_freq = {}

        # Traverse the char map in s and increment as chars found.
        for char in s:
            if char not in char_freq:
                char_freq[char] = 1
            else:
                char_freq[char] += 1
        
        # Now traverse for t and decrement
        for char in t:
            if char not in char_freq:
                return False
            else:
                char_freq[char] -=1
                if char_freq[char] == 0:
                    char_freq.pop(char)
        
        if char_freq != {}:
            return False
        
        return True





