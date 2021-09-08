# 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

# Result:

Runtime: 88 ms, faster than 48.68% of Python3 online submissions for Combination Sum II.
Memory Usage: 14.1 MB, less than 98.42% of Python3 online submissions for Combination Sum II.

# Solution:

Time complexity: O(n ** n!)
Space complexity: O(n ** n!)

Another variant of the permutation problem. Note that comparing to Combination Sum I, the key difference is that this problem introduces dupliates and we do not want duplicates in our return array. So here is how to solve it:

First, we want to avoid processing the duplicates, so we pass in the initial array sorted. Then in each loop, when i is at the starting position of the loop, which is denoted by "index", we can assume that value at this position is not duplicated as it has no previous value for it to compare with. If not, it compares with its previous value. If they are equal, it means that the current one is duplicated and needs to be skipped.

