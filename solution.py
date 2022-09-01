class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        
        courses = [0] * numCourses
        c_map = collections.defaultdict(set)
        q = collections.deque()
        
        for c, r in prerequisites:
            courses[c] += 1
            c_map[r].add(c)
        
        for i, val in enumerate(courses):
            if val == 0:
                q.append(i)
        
        output = []
        while q and courses[q[0]] == 0:
            c = q.popleft()
            output.append(c)
            for next_c in c_map[c]:
                courses[next_c] -= 1
                if courses[next_c] == 0:
                    q.append(next_c)
        
        return len(output) == numCourses