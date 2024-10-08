class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i, j):
            # Base cases
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            # If characters are the same, move to next characters
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            # Try all three operations and take the minimum
            insert = 1 + dfs(i, j + 1)    # Insert operation
            delete = 1 + dfs(i + 1, j)    # Delete operation
            replace = 1 + dfs(i + 1, j + 1)  # Replace operation
            
            return min(insert, delete, replace)
        
        return dfs(0, 0)
            
            