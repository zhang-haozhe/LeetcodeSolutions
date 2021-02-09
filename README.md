# 72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

# Result:

Runtime: 168 ms, faster than 70.72% of Python3 online submissions for Edit Distance.
Memory Usage: 17.7 MB, less than 64.29% of Python3 online submissions for Edit Distance.

# Solution:

Time complexity: O(m \* n)
Space complexity: O(m \* n)

where m \* n is the size of the original matrix.

In this question, supposed that we are checking word 1 against word 2, where i and j represent the index of the characters iterated in word 1 and word 2, respectively, the three operations (insert, delete, replace) can be viewed as:

1. i jumps to the next position, leaving j unchanged
2. j jumps to the next position, leaving i unchanged
3. i and j both jump to the next positions.

At each step, find out the minimum of the three choices and fill the result into the dp matrix.

Note that there is a case that the characters being checked are identical, which means that no operations need to be performed. In this case, just paste the result from the last step (i-1 and j-1).
