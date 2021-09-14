# 917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.

# Result:

Runtime: 52 ms, faster than 5.97% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 14.1 MB, less than 91.66% of Python3 online submissions for Reverse Only Letters.

# Solution:

Two pointers. Iterate until one pointer reaches a letter and then iterate the other one. This should make both on letters. Then, swap them and then move both of them one step closer. Note that this should only run when the right pointer is to the right of the left. 

# Complexity analysis

Time Complexity: O(n)
Space Complexity: O(n)

