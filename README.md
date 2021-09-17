# 1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.

# Result:

Runtime: 24 ms, faster than 96.40% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 14.1 MB, less than 92.17% of Python3 online submissions for Robot Bounded In Circle.

# Solution:

We store the directions in an array. Each time, if it goes, then the position moves per the direction given. If it turns, the index for the direction increases by 1. If it turns right, we only need to make the index point to the opposite direction given the result of turning left. 

Because of the nature of the 4 directions given in this game, at most it takes 4 cycles for the robot to return to the initial position. Otherwise, it won't. So, we only need to run the loop 4 times to check if at the end of each iteration the robot returns to the initial position. 

# Complexity analysis

Time Complexity: O(n)
Space Complexity: O(1)

The loop is iterated 4 * len(instructions) times, so the time complexity is O(n).
No extra space is used, so O(1) for the space complexity.