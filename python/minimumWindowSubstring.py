from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary to keep track of the frequency of characters in t
        t_freq = Counter(t)
        required = len(t_freq)

        # Left and right pointer of our sliding window
        left, right = 0, 0
        # formed is how many unique characters in t are currently being satisfied in the window
        formed = 0

        # Dictionary to keep track of the frequency of characters in the current window
        window_freq = {}

        # (window length, left, right)
        ans = float("inf"), None, None

        while right < len(s):
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            # If the frequency of the current character added equals to the desired count in t_freq, increment formed
            if char in t_freq and window_freq[char] == t_freq[char]:
                formed += 1

            # Try and contract the window till the point where it ceases to be "desirable"
            while left <= right and formed == required:
                char = s[left]

                # Save the smallest window until now
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # The character at the position pointed by `left` is no longer a part of the window
                window_freq[char] -= 1
                if char in t_freq and window_freq[char] < t_freq[char]:
                    formed -= 1

                # Move the left pointer ahead
                left += 1    

            # Keep expanding the window by moving the right pointer
            right += 1

        # Return the smallest window or an empty string if no such window exists
        return "" if ans[1] is None else s[ans[1]:ans[2] + 1]
