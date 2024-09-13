class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: index for index, char in enumerate(s)}
        
        partitions = []
        start = end = 0
        
        for index, char in enumerate(s):
            end = max(end, last_occurrence[char])
            
            if index == end:
                partitions.append(end - start + 1)
                start = index + 1
        
        return partitions