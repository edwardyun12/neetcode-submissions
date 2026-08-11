class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxNum = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxNum = max(maxNum, profit)
                r += 1
            else:
                l = r
        return maxNum
        