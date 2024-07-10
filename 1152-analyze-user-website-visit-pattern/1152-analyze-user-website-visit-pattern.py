class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        # Combine and sort the visits
        visits = sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1]))

        # Group visits by user
        user_history = defaultdict(list)
        for user, _, site in visits:
            user_history[user].append(site)

        def generate_patterns(sites):
            # Generate all 3-website patterns for a given list of sites
            patterns = set()
            n = len(sites)
            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        patterns.add((sites[i], sites[j], sites[k]))
            return patterns

        # Generate all 3-website patterns for each user
        pattern_count = defaultdict(int)
        for sites in user_history.values():
            # Use set to avoid counting duplicate patterns from the same user
            patterns = generate_patterns(sites)
            for pattern in patterns:
                pattern_count[pattern] += 1

        # Find the pattern(s) with the highest count
        max_count = max(pattern_count.values())

        # Get all patterns with the max count, sorted lexicographically
        top_patterns = sorted(
            [pattern for pattern, count in pattern_count.items() if count == max_count]
        )

        # Return the lexicographically smallest pattern
        return list(top_patterns[0])
        
