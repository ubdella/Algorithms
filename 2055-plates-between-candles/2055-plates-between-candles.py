class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Preprocess the string
        candle_positions = []
        prefix_sum = [0] * (n + 1)
        nearest_left_candle = [-1] * n
        nearest_right_candle = [-1] * n
        
        # Build preprocessing arrays
        last_candle = -1
        for i in range(n):
            if s[i] == '|':
                candle_positions.append(i)
                last_candle = i
            nearest_left_candle[i] = last_candle
            prefix_sum[i + 1] = prefix_sum[i] + (s[i] == '*')
        
        last_candle = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last_candle = i
            nearest_right_candle[i] = last_candle
        
        def count_plates(left: int, right: int) -> int:
            # Find the positions of the leftmost and rightmost candles within the query range
            left_candle = nearest_right_candle[left]
            right_candle = nearest_left_candle[right]
            
            # If there are fewer than 2 candles in the range, or if they're in the wrong order, return 0
            if left_candle == -1 or right_candle == -1 or left_candle >= right_candle:
                return 0
            
            # Calculate the number of plates between the candles
            return prefix_sum[right_candle] - prefix_sum[left_candle]
        
        # Process each query
        return [count_plates(left, right) for left, right in queries]