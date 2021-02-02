# 63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:

1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
   Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

# Result:

Runtime: 60 ms, faster than 66.24% of Python3 online submissions for Triangle.
Memory Usage: 14.9 MB, less than 95.70% of Python3 online submissions for Triangle.

# Solution:

Time complexity: O(m _ n)
Space complexity: O(m _ n)

where m \* n is the size of the original matrix.

I solved this problem in 3 different approaches. The basic gist is that each cell is the sum of the cell above it and the cell to its left. Therefore, 3 methods can be derived out of this thought:

Brute force recursion:
Each time the function queries value of the right cell and the value of the cell under it. Once it gets to the desired spot, return 1. Then, it sum up all the possibilities. The drawback of this method is that it always re-vissts the queried cell, which significnatly reduces the performance.

Memoization:
The improved version of brute force. On the basis of it, create a map that keeps track of the value of each cell. However, because of the size of call stack, the performance is still very slow.

Dynamic programming:
The gist of this method is to consider the grid as a matrix, where each cell contains the number of possibilities to get to the cell. Each cell is determined by the one to its left and the one above it. To help process the data, I added 1 additional row and 1 additional column, because for the first row/column from the original grid, there is no cell to its left/above it for reference.
