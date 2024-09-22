class Solution:
    def subsets(self, nums):
        def backtrack(start, current_subset):
            # Add the current subset to the result
            result.append(current_subset[:])
            
            # Iterate over all numbers starting from `start`
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                # Recursively call backtrack with the next starting point
                backtrack(i + 1, current_subset)
                # Backtrack by removing the last added number
                current_subset.pop()

        result = []
        backtrack(0, [])
        return result
