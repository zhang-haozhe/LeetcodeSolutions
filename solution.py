def backpack(m, A):
    # write your code here
    n = len(A)
    if sum(A) <= m:
        return sum(A)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])
    return dp[n][m]

print(backpack(10, [3,4,8,5]))