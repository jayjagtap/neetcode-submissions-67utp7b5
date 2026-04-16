class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        odd
        [1,4,5,10,12], target = 4
        mid = size//2 = 5//2 = 2, left = 0, right = 4
        left = 0, right = mid - 1 , 1

        even
        [1,4,5,10,12,18], target = 12
        left=0, right= 6, mid = 3
        mid < target, left = mid+1

        if not found return -1
        """

        size = len(nums)
        left, right = 0, size-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return -1


        