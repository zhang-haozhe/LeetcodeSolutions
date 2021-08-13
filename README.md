# 639. Decode Ways II

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '_' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1_" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1\*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s consisting of digits and '\*' characters, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: s = "_"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "_".
Example 2:

Input: s = "1*"
Output: 18
Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
Hence, there are a total of 9 * 2 = 18 ways to decode "1\*".
Example 3:

Input: s = "2*"
Output: 15
Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
"21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
Hence, there are a total of (6 * 2) + (3 _ 1) = 12 + 3 = 15 ways to decode "2_".

Constraints:

1 <= s.length <= 105
s[i] is a digit or '\*'.

# Result:

Runtime: 857 ms, faster than 25.82% of Python3 online submissions for Decode Ways II.
Memory Usage: 18.9 MB, less than 35.82% of Python3 online submissions for Decode Ways II.

# Solution:

Time complexity: O(n)
Space complexity: O(n)

The gist of this solution is based on the following equation:

dp[i] = dp[i-1] (if the last digit is not zero) + dp[i - 2] (if the last two digits combined are between 10 - 26)

The other issue to consider is that '_' introduces a significant level of complexity. To deal with it, we need to discuss it by case.
There are generally 4 cases: nn, n_, _n and ** where n represents a number. nn has already been discussed and solved in decode ways I.
For **, there are 11~19 + 21~26 so 15 cases.
For 1_, possible cases are 11~19 so 9 cases.
For 2*, possible cases are 21~26 so 6 cases.
For *n, if n <= 6, possbile cases are 1n and 2n so 2 cases. If n >6, the only possble case is 1n.

Note that this problem is strict with time and space. Make sure to take the modulo of the number computed each time, or the memory cannot hold.

Since an array with size of s is used, the space complexity is O(n). Time is O(n) because it iterates through the string by each character.
