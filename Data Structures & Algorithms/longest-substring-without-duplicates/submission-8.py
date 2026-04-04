class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxSize, L = 0, 0

        for R, char in enumerate(s):
            while char in window:
                window.remove(s[L])
                L += 1
            window.add(char)
            maxSize = max(maxSize, len(window))
        return maxSize