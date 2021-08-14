# 73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

# Result:

Runtime: 202 ms, faster than 5.01% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 15 MB, less than 74.78% of Python3 online submissions for Set Matrix Zeroes.

# Solution:

Time complexity: O(mn)
Space complexity: O(1)

This solution follows the following steps:

1. once a row is found to contain a zero, mark the row.
2. once the row is marked, iterate through it and change all non-zero values to '%'.
3. repeat the same process for columns.
4. replace all cells whose values are '%' with 0.

This solution traverses through each cell in the matrix once (in each iteration) and in total we repeat it 3 times. Therefore, the time complexity of this solution is O(mn), where mn is the dimension of the matrix.

Since we do not use any additional space and all values are changed in-place, the space complexity is O(1).
