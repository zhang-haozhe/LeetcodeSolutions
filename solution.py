class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        chars = list(s)
        while right > left:
            while right > -1 and not chars[right].isalpha():
                right -= 1
            while left < len(s) and not chars[left].isalpha():
                left += 1
            if right > left and right > -1 and left < len(s):
                chars[right], chars[left] = chars[left], chars[right]
                right -= 1
                left += 1
        return ''.join(chars)