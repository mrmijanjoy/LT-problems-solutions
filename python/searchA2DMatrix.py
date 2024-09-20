class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Number of rows and columns
        m = len(matrix)
        n = len(matrix[0])
        
        # Binary search initialization
        low = 0
        high = m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Convert mid to row and column indices
            row = mid // n
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
