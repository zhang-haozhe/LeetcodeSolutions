# 120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
2
3 4
6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

# Result:

Runtime: 60 ms, faster than 66.24% of Python3 online submissions for Triangle.
Memory Usage: 14.9 MB, less than 95.70% of Python3 online submissions for Triangle.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

I regard this question as an entry-level but typical DP problem. I approached this problem by calculating the min steps to each cell and storing the results back to the triangle list. Each time, the value of a cell is decided by the one above it and the one to its top left, so min(triangle[i - 1][j], triangle[i - 1][j - 1]). There are certainly edge cases to handle because indeces go out of bound often. Once the calculation is done, calculate the min of the bottom level, which is the minimum steps required to reach the bottom.

The time comp is O(n) in my case because I traverse through all of the elements once, although I have two loops nested. The space comp can be taken as O(n) or O(1) either. In my case, I directly modify the original triangle 2-d array without creating any other data structure, so it is O(1). If a new list is created to store the numbers of steps taken, it should be O(n).
