class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Compexity: O(n)
        Space Complexity: O(1)

        Window resets, whenver profit becomes negative.
        """

        profit, maxProfit = 0, 0
        left, right , n = 0, 1, len(prices)
        while right < n:
            profit = prices[right] - prices[left]
            maxProfit = max(profit, maxProfit)
            if profit < 0:
                left , right = right, right+1
            else:
                right+=1
        
        return maxProfit
        