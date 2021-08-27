# Tower of Hanoi

Description
Tower of Hanoi is a well-known problem.There are n plates of different sizes (radius 1-n) stacked on three pillars A, B and C.They are all stacked on A at first, your goal is moving all the plates from A to C in minimum legal steps.
The rules of moving are as follows:

You are allowed to move one plate once (from top of one pillar to top of another pillar)
Ensure that the smaller plates are on the top of the bigger one,and there is nothing under the biggest plate.

Example
Example 1:

Input:n = 2
Output: ["from A to B","from A to C","from B to C"]
Example 2:

Input:n = 3
Output:["from A to C","from A to B","from C to B","from A to C","from B to A","from B to C","from A to C"]

# Result

122 mstime cost
·
11.55 MBmemory cost
·
Your submission beats93.28 %Submissions

# Solution

Done using binary tree inorder traversal. Each time, it reduces the problem of moving n plates to moving n - 1 plates. Since 3 pillars are given, we can treat them as start, temp, and end, respectively. Then, to move the nth plate, it first moves all the plates above it to the temp pillar, then move it to end and then move the rest from temp to end. Once the upmost plate is being moved, it skips the temp pillar as it does not need it to move to the end pillar.

# Complexity Analysis
