class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by slashes
        parts = path.split('/')
        stack = []
        
        # Iterate through each part of the path
        for part in parts:
            if part == '' or part == '.':
                # Skip empty parts or '.' (current directory)
                continue
            elif part == '..':
                # '..' means go back to the parent directory
                if stack:
                    stack.pop()
            else:
                # Valid directory names get added to the stack
                stack.append(part)
        
        # Join the stack into a single canonical path with slashes
        return '/' + '/'.join(stack)

# Example usage:
solution = Solution()

# Test cases
path1 = "/home/"
path2 = "/home//foo/"
path3 = "/home/user/Documents/../Pictures"
path4 = "/../"
path5 = "/.../a/../b/c/../d/./"

print(solution.simplifyPath(path1))  # Output: "/home"
print(solution.simplifyPath(path2))  # Output: "/home/foo"
print(solution.simplifyPath(path3))  # Output: "/home/user/Pictures"
print(solution.simplifyPath(path4))  # Output: "/"
print(solution.simplifyPath(path5))  # Output: "/.../b/d"
