class Solution:
    def LCS(self , str1 , str2 ):
        # write code here
        dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if str2[i - 1] == str1[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
        maximum = 0
        longest = ""
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if dp[i][j] > maximum:
                    maximum = dp[i][j]
                    longest = str1[j - maximum:j]
        return longest