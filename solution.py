class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if int(s[i - 1]) != 0:
                dp[i] += dp[i - 1]
            if not i == 1 and not int(s[i - 2:i]) < 10 and not int(s[i - 2:i]) > 26:
                dp[i] += dp[i - 2]

        return dp[-1]