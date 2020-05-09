class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occList = []
        numList = []
        for element in arr:
            if element not in numList:
                numList.append(element)
                occList.append(1)
            else:
                x = numList.index(element)
                occList[x] += 1
        # print(numList)
        # print(occList)
        for times in occList:
            # print(times)
            # print(occList[1:])
            if(times in occList[1:]):
                return False
            occList = occList[1:]
        
        return True