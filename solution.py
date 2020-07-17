class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for n in range(0, len(haystack) - len(needle) + 1):
            if haystack[n:n+len(needle)] == needle:
                return n
        else:
            return -1
