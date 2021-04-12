# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

# Result:

Runtime: 88 ms, faster than 95.50% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.4 MB, less than 27.91% of Python3 online submissions for Group Anagrams.

# Solution:

Time complexity: O(n^2) (but actually O(n) in practice)
Space complexity: O(n)

First make a new list of sorted strings. Then, map the sorted strings to their original positions in the list. Once done, put the strings with the same sorted string together in one array and then return the list of such arrays.

There are indeed two nested loops, but in total they only execute n times rather than n^2, where n is the length of the list.
