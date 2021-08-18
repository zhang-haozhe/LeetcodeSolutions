# 1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

# Result:

Runtime: 268 ms, faster than 37.09% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 33.5 MB, less than 45.31% of Python3 online submissions for Count Good Nodes in Binary Tree.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

DFS. In each traversal, check if the current node value is bigger than the largest value that has appeared once the iterator passes to it, then update it if needed. Once checked, go to its child nodes.

Since we only traverse through the list at most twice, the time complexity is O(n). We do not create any extra data structure, so the space complexity is O(1). However, it is notable that this algo uses extra call stack due to recursion, the space complexity is actually not O(1).
