class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for _ in range(len(word2)+1): dp.append([0]*(len(word1)+1))
        for i in range(len(word1)+1): dp[0][i] = i
        for i in range(len(word2)+1): dp[i][0] = i
        
        for x in range(1, len(dp)):
            for y in range(1, len(dp[0])):
                if word1[y-1] == word2[x-1]:
                    dp[x][y] = dp[x-1][y-1]
                else:
                    dp[x][y] = 1 + min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1])
        
        return dp[-1][-1]