class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        left = [0,0]  right = [n-1, n-1]
        mid = [(r1+r2)//2, (c1+c2)//2]
        if target < nums[midr][midc]:
            right = [midr-1][midc]
        else:
            left = [midr+1][midc]
        """

        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return self.binary_search(row, target)
        
        return False
                
    def binary_search(self, search_space: List, target: int) -> bool:

        n = len(search_space)
        left, right = 0, n-1

        while left <= right:

            mid = (left+right)//2

            if target == search_space[mid]:
                return True
            elif target < search_space[mid]:
                right = mid-1
            else:
                left = mid + 1
        
        return False

        