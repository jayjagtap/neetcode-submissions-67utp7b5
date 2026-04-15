from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        [act, pots, tops, cat, stop]

        Traverse the list, make a hashmap
        Element 1  act
        {
        act: [act]
        }
        ele 2 pots, does not match with current entries in hashmap
        {
        act: [act],
        pots: [pots]
        }
        ele 3, tops. check against current entries in hashmap, matches with pots
        {
        act: [act],
        pots: [pots, tops]
        }
        Similary:
        {
        acts: [act,cat]
        pots: [pots, tops]
        hat: [stop]
        }
    
        If anagram is matched, add to the list, if not add new key

        time Complexity: O(N*KlogK)
        """ 

        ana_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            ana_map[sorted_word].append(word)
        
        return [x for x in ana_map.values()]

# s =  Solution()
# print(s.is_anagram("act", "cat"))