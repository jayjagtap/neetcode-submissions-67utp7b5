from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(k) k<26 chars
        """

        s = "".join(s.split())
        t = "".join(t.split())

        # Space Complexity: O(k)
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1

        return all(v == 0 for v in freq.values())

# from collections import Counter
# return Counter(s) == Counter(t)

        
        



