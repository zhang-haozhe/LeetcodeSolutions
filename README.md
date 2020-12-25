# 1. Find pair that sums up to k

Solve the problem [Python]
Given an array of integers arr and an integer k, create a boolean function that checks if there exist two elements in arr such that we get k when we add them together.

Example 1:

Input: arr = [4, 5, 1, -3, 6], k = 11

Output: true

Explanation: 5 + 6 is equal to 11

Example 2:

Input: arr = [4, 5, 1, -3, 6], k = -2

Output: true

Explanation: 1 + (-3) is equal to -2

Example 3:

Input: arr = [4, 5, 1, -3, 6], k = 8

Output: false

Explanation: there is no pair that sums up to 8

# Solution:

A typical way to solve this problem is to enumerate all possible combinations, which is a very bad practice. My solution improves the performance by adjusting the sum and making it closer to the desired value in each step. At the beginning, there are two iterators at the ends of the sorted array. Each time the sum of the values where the iterators are located is evaluated. If the sum is bigger than the desired value, the left pointer moves right by 1 to increase the sum. Similarly, the right pointer moves left to decrease the sum if it is too large. Thus, the time complexity is reduced to O(nlogn) for sorting the array and the space complexity is O(n) for storing the sorted array.
