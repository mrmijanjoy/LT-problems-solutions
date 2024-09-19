function lengthOfLongestSubstring(s) {
    const n = s.length;
    if (n === 0) return 0;

    let maxLength = 0;
    let start = 0;
    const seen = {};

    for (let end = 0; end < n; end++) {
        if (s[end] in seen && start <= seen[s[end]]) {
            start = seen[s[end]] + 1;
        } else {
            maxLength = Math.max(maxLength, end - start + 1);
        }
        seen[s[end]] = end;
    }

    return maxLength;
}

// Test cases
console.log(lengthOfLongestSubstring("abcabcbb")); // Output: 3
console.log(lengthOfLongestSubstring("bbbbb"));    // Output: 1
console.log(lengthOfLongestSubstring("pwwkew"));   // Output: 3
