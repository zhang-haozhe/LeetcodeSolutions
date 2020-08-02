# 451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

# Result:

Runtime: 40 ms, faster than 83.74% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 15.1 MB, less than 58.78% of Python3 online submissions for Sort Characters By Frequency.

# Solution:

The dictionary stores the frequency of each character's presence. However, it needs to be sorted by its values. Hence, we use Python's built-in sorted function, where its three parameters being the items of the dict, specifying the function to sort by value and true for making the sorting to go in the descending order.
