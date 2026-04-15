class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [1, 3, 2, 4] target = 7 ans = [1,3]
        map{
        1 : 0,
        3 : 1,
        2 : 2,
        4: 3
        }

        traverse the array and check (target - num) present or not.
        If present, make a list of indices and return it

        Corner cases:
        [1,2,4,5], target = 39 not possible
        [1,1] target = 2 , return [0,1] not [0,0]
        """

        index_map = {}

        for i, num in enumerate(nums):
            search = target - num
            if search in index_map:
                return [index_map[search], i]
            else:
                index_map[num] = i
        
        return []


        