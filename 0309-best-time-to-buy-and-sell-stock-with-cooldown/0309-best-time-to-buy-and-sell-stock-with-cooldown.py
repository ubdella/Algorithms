class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        # Initialize variables
        buy = float('inf')  # Minimum price seen so far
        sell = 0  # Maximum profit if we sell on the current day
        prev_sell = 0  # Maximum profit we had two days ago
        
        for price in prices:
            # The maximum profit if we don't sell on this day
            temp = sell
            
            # Update the maximum profit if we sell on this day
            sell = max(sell, price - buy)
            
            # Update the minimum buy price
            # We can either keep the previous buy price or buy on this day
            # If we buy on this day, we use the profit from two days ago
            buy = min(buy, price - prev_sell)
            
            # Update the profit from two days ago
            prev_sell = temp
        
        return sell