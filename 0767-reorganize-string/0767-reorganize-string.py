class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character
        # Time complexity: O(n), Space complexity: O(k), where k is the number of unique characters
        char_counts = Counter(s)

        # Create a max heap (using negatives since Python has min heap)
        # Time complexity: O(k log k), Space complexity: O(k)
        max_heap = [(-count, char) for char, count in char_counts.items()]
        heapq.heapify(max_heap)

        # If the most frequent character appears more than (n+1)/2 times,
        # it's impossible to reorganize the string
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""

        result = []

        # Rearrange the string
        # Time complexity: O(n log k), Space complexity: O(n) for the result
        while len(max_heap) >= 2:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)

            result.extend([char1, char2])

            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))

        # Handle the case when there's one character left
        if max_heap:
            result.append(max_heap[0][1])

        return ''.join(result)