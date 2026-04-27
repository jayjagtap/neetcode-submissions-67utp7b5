from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Sort and put it in a hash. O(n*klogk) where k is the average length of the word
        """

        anagrams = defaultdict(list)

        for word in  strs:
            anagrams["".join(sorted(word))].append(word)
        
        return [x for x in anagrams.values()]
