# 1207. Unique Number of Occurrences

Easy


Add to List

Share
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000


# Solution:

First set up the occurance list and the number list, which store the times that each number has shown up. 
Then, each time it iterates the given array, it modifies the two lists in the logic stated above.
At last, it finds if each occurance element has existed in the rest of the occurrance list and each time the occurance list removes its first element. If one is found, then return false. If one has never been found, then return true.
