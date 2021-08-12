# 338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:

0 <= n <= 105

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like \_\_builtin_popcount in C++)?

# Result:

Runtime: 76 ms, faster than 90.34% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 70.98% of Python3 online submissions for Counting Bits.

# Solution:

Time complexity: O(n)
Space complexity: O(n)

The gist of this solution is based on the following equation:

dp[i] = dp[i >> 1] + (i % 2)

E.g.

(170)10 = (10101010)2
(85)10 = (1010101)2

where by dividing 170 by 2, its binary form gets shifted right by one. 170's 1 bits can be converted to 170's last digit plus 85's 1 bits.

Since an array with size of s is used, the space complexity is O(n). Time is O(n) because it iterates through the string by each character.
