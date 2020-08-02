class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        temp = x
        result = 0
        if x < 0:
            negative = True
            temp = -x
        length = len(str(temp))
        for n in range(length-1, -1, -1):
            result += temp // 10 ** n % 10 * 10 ** (length - 1 - n)
        if negative:
            if -result < -2 ** 31:
                return 0
            return -result
        if result > 2 ** 31 - 1:
            return 0
        return result
