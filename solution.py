class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]: return '0'
        num1 = list(num1[::-1])
        num2 = list(num2[::-1])
        overflow = 0
        
        dp = [0] * (len(num1) + len(num2))
        
        for i in range(len(num2)):
            for j in range(len(num1)):
                res = int(num1[j]) * int(num2[i]) + overflow
                dp[-i - j - 1] += res
                overflow = dp[-i - j - 1] // 10
                dp[-i - j - 1] %= 10
            else:
                dp[-i - j - 2] += overflow
                overflow = 0
        dp[0] += overflow
        final = list(map(str, dp))
        final = ''.join(final)
        final = final.lstrip('0')
        return final