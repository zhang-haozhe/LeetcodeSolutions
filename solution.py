# Parameters:
#  arr: List[int]
# return type: bool

from functools import reduce
def recurr(map, string, length, index = 0):
    if index in map:
        return map[index]
    if index == length - 1:
        map[index] = 0
        return 0
    if index >= length or string[index] == 0:
        map[index] = 1
        return 1
    
    tempList = []
    for i in range(string[index]):
        tempList.append(recurr(map, string, length, index + i + 1))

    product = reduce(lambda x, y: x*y, tempList)
    # map[index] = product
    return product

def canJump(arr):
    # your code here
    map = {}
    ans = recurr(map, arr, len(arr))
    print(map)
    return False if  ans == 1 else True
# [3,0,2,0,2,1,4,3]
# [5,3,2,0,1,0,4]
# [1,1,1,1,1,0]
print(canJump([3,0,2,0,2,1,4,3]))