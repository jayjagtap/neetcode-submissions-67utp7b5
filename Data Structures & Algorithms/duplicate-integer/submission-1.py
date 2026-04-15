class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        [1,3,4,5,1] , ans 1
        Use hashmap/set. Time Complexity O(N)

        Corner Cases
        empty array [] , in this case return false since no element repeats
        single num [1], return false since no element repeats 
        """

        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        
        return False

        