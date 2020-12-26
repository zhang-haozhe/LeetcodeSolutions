class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 0
        maximum = 1
        substr = ""
        while right < len(s):
            if s[right] not in substr:
                substr += s[right]
                right += 1
            else:
                left = s.index(s[right], left) + 1
                right += 1
                substr = s[left:right]
            maximum = max(maximum, len(substr))
        return maximum