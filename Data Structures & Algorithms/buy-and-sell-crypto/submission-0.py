class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = float('inf')
        greatest_diff = 0
        for i, price in enumerate(prices):
            lowest_buy = min(lowest_buy, price)
            greatest_diff = max(greatest_diff, price-lowest_buy)

        return greatest_diff
            

            

