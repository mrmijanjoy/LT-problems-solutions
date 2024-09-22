class Solution:
    def combine(self, n: int, k: int):
        def backtrack(start, path):
            # If the current combination is of the required length k
            if len(path) == k:
                result.append(path[:])  # Add a copy of the current path to the results
                return
            
            # Iterate through the numbers from `start` to `n`
            for i in range(start, n + 1):
                # Add i to the current combination
                path.append(i)
                # Move on to the next number, increasing `start` to avoid duplicates
                backtrack(i + 1, path)
                # Backtrack by removing the last number
                path.pop()

        result = []
        backtrack(1, [])
        return result
