# 217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

# Result:

Runtime: 124 ms, faster than 88.12% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20.2 MB, less than 15.85% of Python3 online submissions for Contains Duplicate.

# Solution:

The core of this solution is Hash, in that looking for pairs of mapped values is fairly easy and fast using dictionary in Python. Therefore, the program each time checks if a value exists in its dictionary; if so, it returns true and adds the value if not.
