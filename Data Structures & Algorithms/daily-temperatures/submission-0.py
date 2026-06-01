class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Brute Force: O(n2)
        """

        count = 0
        n = len(temperatures)
        result = [0]*n

        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        
        return result



        
        