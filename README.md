# 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1); // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2); // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1); // return -1 (not found)
lRUCache.get(3); // return 3
lRUCache.get(4); // return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 \* 105 calls will be made to get and put.

# Result:

Runtime: 716 ms, faster than 99.32% of Python3 online submissions for LRU Cache.
Memory Usage: 75.3 MB, less than 17.55% of Python3 online submissions for LRU Cache.

# Solution:

We want a data structure to have the property of mapping so that a key and its value are associated. However, normal dict in Python is not ordered to represent the order of the items used. Therefore, an ordered dict is the perfect choice. When getting an element, if the key does not exist, return -1 and if it does, mark it as recently used and return the value.

When putting an element, we first check if it is in the dict. If it does, modify the value. If not, then check if the data structure has empty space. If there is, then reduce the capacity by one and add the value. If not, pop the first item in the ordered list. In any case, move the element to the last position of the ordered dictionary, indicating that it has just been recently used.

# Complexity analysis

Time complexity: O(1)
Space complexity: O(n)

For an ordered dictionary in Python, the time complexity to locate an item is O(1). It also takes O(1) time complexity to insert or delete an item. Also, since move_to_end is constant in time becasue it only adjusts pointers in a doubly linked list, the overal time complexity of this structure is O(1) for put and get.
The space complexity is O(n) because the function call stack is O(n) in the worst case.
