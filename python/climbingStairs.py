class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the first two steps
        first, second = 1, 2
        
        # Iterate from the third step to the nth step
        for i in range(3, n + 1):
            # The current step is the sum of the previous two
            current = first + second
            first = second
            second = current
        
        return second

# Example usage:
solution = Solution()
n = 3
print(solution.climbStairs(n))  # Output: 3
