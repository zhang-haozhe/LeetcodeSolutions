class ExamRoom:
    '''
    General idea is to insert intervals like (distance, start, end) to the heap and always pick the top interval from heap to get the biggest distance for seating.
    '''
    def dist(self, x, y):  # length of the interval (x, y)
        if x == -1:        # note here we negate the value to make it maxheap
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(abs(x-y)//2) 
        
    def __init__(self, N):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]  # initialize heap
        
    def seat(self):
        _, x, y = heapq.heappop(self.pq)  # current max interval 
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x+y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))  # push two intervals by breaking at seat
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat
        
    def leave(self, p):
        '''
        traverse the heap to get the intervals split by the leaving position and push a merged interval to the heap
        '''
        head = tail = None
        for interval in self.pq:  # interval is in the form of (d, x, y)
            if interval[1] == p:  
                tail = interval
            if interval[2] == p:  
                head = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)  # important! re-heapify after deletion
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)