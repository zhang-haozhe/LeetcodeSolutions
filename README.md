# 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

# Result:

Runtime: 134 ms, faster than 69.54% of Python3 online submissions for Course Schedule.
Memory Usage: 15.4 MB, less than 90.00% of Python3 online submissions for Course Schedule.

# Solution:

Use Topological Sort to solve the problem. First, count the number of dependencies of each node, and put all nodes that have no dependencies to the queue. Each time, we pop one, remove it from the graph, and thus decrease the number of dependencies of its next nodes by one. Once its neighbor nodes have an incoming degree of 0, we add it to the queue. If the queue gets empty, check if the number of popped nodes is equal to the total number of nodes. If not, it indicates there is a cycle in the graph and the program should return false. Otherwise, return true.

# Complexity analysis

Time Complexity: O(|E| + |V|)
Space Complexity: O(|E| + |V|)
