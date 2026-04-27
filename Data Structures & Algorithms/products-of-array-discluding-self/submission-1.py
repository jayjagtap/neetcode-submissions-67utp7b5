class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        left_prod
        right_prod

        [1,4,-2,3,7]
        left_prod = [1,]. (for i in range(1, len(nums), 1st element is 1))
        right_prod = [].  (for i in range(len(nums)-1,0,-1)) last element is 1
        """
        size = len(nums)
        left_prod = [1 for x in range(size)]
        right_prod = [1 for x in range(size)]

        # Compute left product
        for i in range(1, size):
            left_prod[i] = left_prod[i-1]*nums[i-1]
    
        # Compute right product
        for i in range(size-2, -1, -1):
            right_prod[i] = right_prod[i+1]*nums[i+1]

        return [x*y for x, y in zip(left_prod, right_prod)]






        