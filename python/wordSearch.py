class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        def backtrack(r, c, index):
            # Base case: If the entire word is found
            if index == len(word):
                return True
            
            # Check if the current position is out of bounds or the character does not match
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False
            
            # Mark the current cell as visited by storing its value and replacing it with a special character
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore in all four directions: up, down, left, right
            found = (backtrack(r + 1, c, index + 1) or  # Down
                     backtrack(r - 1, c, index + 1) or  # Up
                     backtrack(r, c + 1, index + 1) or  # Right
                     backtrack(r, c - 1, index + 1))    # Left
            
            # Restore the original value of the cell (backtrack)
            board[r][c] = temp
            
            return found
        
        # Loop through the grid to find the starting point for the search
        for i in range(len(board)):
            for j in range(len(board[0])):
                # If the first letter matches, start backtracking from this position
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        
        return False
