class Solution:
    def numDecodings(self, s: str) -> int:
        # write your code here
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                ast = 1
                if s[i - 1] == '*':
                    ast = 9
                dp[i] += dp[i - 1] * ast
            if not i == 1:
                if s[i - 2] == '1':
                    if s[i - 1] == '*':
                        dp[i] += dp[i - 2] * 9
                    else:
                        dp[i] += dp[i - 2]
                if s[i - 2] == '2':
                    if s[i - 1] == '*':
                        dp[i] += dp[i - 2] * 6
                    elif s[i - 1] <= '6':
                        dp[i] += dp[i - 2]
                if s[i - 2] == '*':
                    if s[i - 1] == '*':
                        dp[i] += dp[i - 2] * 15
                    elif s[i - 1] <= '6':
                        dp[i] += dp[i - 2] * 2
                    else:
                        dp[i] += dp[i - 2]
            dp[i] %= (10 ** 9 + 7)

        return dp[-1] % (10 ** 9 + 7)