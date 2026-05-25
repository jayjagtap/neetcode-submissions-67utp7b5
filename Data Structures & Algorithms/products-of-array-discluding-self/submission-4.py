class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        O/P: [48, 24, 12, 8]

        [-1, 0, 1, 2, 3]
        O/P: [0, -6, 0, 0]

        Prefix product: [1, 1, 2, 8] 
        Post product: [48,24,6,1]
        """
        size = len(nums)
        pre, post = [1]*size , [1]*size

        # Compute pre-prod
        for i in range(1,size):
            pre[i] = pre[i-1]*nums[i-1]

        """
        Comments: Post array can be skipped, and we can reduce the 
        space complexity from O(n) to O(1)
        for i in range(size-2, -1, -1):
            post[i] = post[i+1]*nums[i+1]

        return [x*y for x, y in zip(pre, post)]
        """

        right = 1
        for i in range(size-2, -1, -1):
            right*=nums[i+1]
            pre[i]*=right

        return pre
    



        