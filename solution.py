class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        mapping = collections.defaultdict(set)
        
        for index in range(len(routes)):
            for stop in routes[index]:
                # add bus number to each stop
                mapping[stop].add(index)
        
        queue = collections.deque([(source, 0)])
        seen_stops = set()
        seen_buses = set()
        
        while queue:
            curr_stop, num_step = queue.popleft()
            if curr_stop == target:
                return num_step
            
            for bus in mapping[curr_stop]:
                if bus in seen_buses:
                    continue
                seen_buses.add(bus)
                
                for neighbor_stop in routes[bus]:
                    if neighbor_stop in seen_stops:
                        continue
                    seen_stops.add(neighbor_stop)
                    queue.append((neighbor_stop, num_step + 1))
        return -1