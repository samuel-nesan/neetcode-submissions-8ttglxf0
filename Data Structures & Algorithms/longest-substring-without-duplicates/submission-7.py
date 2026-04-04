class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        size = 0
        L = 0

        for R, char in enumerate(s):
            while char in window:
                window.remove(s[L])
                L += 1
            window.add(char)
            size = max(size, len(window))
        
        return size
