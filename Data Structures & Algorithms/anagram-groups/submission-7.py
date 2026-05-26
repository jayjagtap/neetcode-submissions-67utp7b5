from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity:
        Sort a work with avg size k, O(klogk)
        Traverse through a list of words O(n)
        Time Complexity: O(n*klogk)

        Space Compexity: O(n*k)
        """

        anagrams = defaultdict(list)

        # Time Complexity is O(n*k)
        for word in strs:
            count = [0]*26
            for char in word:   
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        return list(anagrams.values())

"""
Follow-up worth knowing — there's an O(n·k) time solution (no sorting) using a character frequency tuple as the key instead:

for word in strs:
    count = [0] * 26
    for c in word:
        count[ord(c) - ord('a')] += 1
    anagrams[tuple(count)].append(word)
"""