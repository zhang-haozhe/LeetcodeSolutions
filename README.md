# Jump to Last Index

Given a non-empty array of non-negative integers arr, where each element represents the maximum jump that we can perform from that index, create a boolean function that checks if we can reach the last index starting from the first one.

Example 1:

Input: arr = [3, 0, 2, 0, 2, 1, 4, 3]

Output: true

Explanation: we can for example jump from arr[0] to arr[2], then from arr[2] to arr[4], then from arr[4] to arr[6], then from arr[6] to arr[7] (the last index)

Example 2:

Input: arr = [5, 3, 2, 0, 1, 0, 4]

Output: false

Explanation: we have no way to reach the last index

# Result:

# Solution:

I approached this by using memoization. First solve the problem by recursive brute force, but when a node has been queried, it immediately returns the answer for the given node. If not queried, it stores the answer for the current node.
