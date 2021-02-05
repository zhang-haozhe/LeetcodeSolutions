# 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

# Result:

Runtime: 92 ms, faster than 91.90% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.6 MB, less than 82.71% of Python3 online submissions for Minimum Path Sum.

# Solution:

Time complexity: O(m _ n)
Space complexity: O(m _ n)

where m \* n is the size of the original matrix.

Quite similar to 62 and 63. This time it only calculates the minimum between the one from the left and the one from the top. Then the value of the cell is calculated by adding the result to the original value in the grid.
