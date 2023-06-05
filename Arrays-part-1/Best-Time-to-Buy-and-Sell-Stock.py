class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        prof = 0
        for i in range(1, len(prices)):
            prof = max(prof, prices[i] - mini)
            mini = min(mini, prices[i])

        return prof

        
