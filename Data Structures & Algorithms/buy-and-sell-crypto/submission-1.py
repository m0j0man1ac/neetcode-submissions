class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)

        buy = prices[0]
        maxProfit = -1

        for i in range(1, size):
            maxProfit = max(maxProfit, prices[i]-buy)
            buy = min(buy, prices[i])

        return max(0, maxProfit)

        