# 233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0

Constraints:

0 <= n <= 109

# Result

Runtime: 28 ms, faster than 80.15% of Python3 online submissions for Number of Digit One.
Memory Usage: 14.4 MB, less than 12.31% of Python3 online submissions for Number of Digit One.

# Solution

In this question, we can split up the number into three parts:

a, curr, b

where curr is the current digit that we are evaluating, and a is the digts before curr, b being the digits after curr.

When evaluating the number, there can be three cases:

1. curr > 1
2. curr < 1
3. curr == 1

In case 1,
e.g.
325 6 197
a curr b
where 6 is the curr. In this case, a can range from (0, 325) so 326 choices, and b can range from (0, 999), so base, which is set to be 1000.
Therefore, case 1 yields (a + 1) \* base choices.

In case 2,
e.g.
325 0 197
a curr b
where 0 is the curr. In this case, since there is no chance that we count 1 in this arrangement, a can only range from (0, 324) so 325 choices and b ranging from (0, 999) so base.
Therefore, case 2 yields a \* base choices.

In case 3,
e.g.
325 1 197
a curr b
where 0 is the curr. In this case, a can range from (0, 324) so 325 choices, and b can range from (0, 999), so base, which is set to be 1000. Then, we still need to consider the case when a = 325. When a = 325, b ranges from (0, 197).
Therefore, case 2 yields a \* base + 1 \* (b + 1) choices.

# Complexity Analysis

Time complexity: O(K), where K is the number of digits of the input.
Space complexity: O(1)

The loop runs log10(n) times, which is equivalent to the number of n's digits. Therefore, the time complexity is O(K), where K = log10(n).
Since we dont create any extra data structure, the space complexity is maintained at O(1).
