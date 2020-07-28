class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        length = len(str(x))
        for n in range(length // 2):
            if x // 10 ** n % 10 != x // 10 ** (length - n - 1) % 10:
                return False
        return True
