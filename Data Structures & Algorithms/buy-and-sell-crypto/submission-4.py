class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1

        # left = buy, right = sell

        maxProfit = 0

        # while right poitner not past the length of prices
        for r in range(len(prices)):
            # is transaction profitable?
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])

            else:
                l = r

        return maxProfit