def lcs(str1, str2):
    # your code here
    dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(dp)
    return dp[-1][-1]

print(lcs("abdacbab", "acebfca"))
# print(lcs("ac", "gfecbfdedae"))