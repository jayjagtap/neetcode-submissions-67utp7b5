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
        res = [1 for x in range(size)]

        # Compute left product
        for i in range(1, size):
            res[i] = res[i-1]*nums[i-1]
    
        # Compute right product
        right = 1
        for i in range(size-2, -1, -1):
            right *= nums[i+1]
            res[i] *= right

        return res






        