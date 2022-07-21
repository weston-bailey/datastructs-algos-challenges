# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_found = float('inf')
        max_profit = 0

        # loop over prices
        for price in prices:
            min_found = min(min_found, price)
            max_profit = max(max_profit, price - min_found)

        return max_profit
