class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination: return 0 
        pointA = min(start, destination)
        pointB = max(start, destination)
        
        tempList = distance
        
        dis1 = sum(tempList[pointA:pointB])
        del tempList[pointA:pointB]
        dis2 = sum(tempList)
        
        return min(dis1, dis2)