class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        buy = float('inf')
        sell = 0
        prev_sell = 0
        
        for price in prices:
            temp = sell
            sell = max(sell, price - buy)
            buy = min(buy, price - prev_sell)
            prev_sell = temp
        
        return sell