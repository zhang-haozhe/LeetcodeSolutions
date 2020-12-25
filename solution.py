from math import inf

def maxSubarray(arr):
    globalSum = -inf
    localSum = 0
    for elem in arr:
        localSum = max(elem, localSum + elem)
        globalSum = max(globalSum, localSum)
    print(globalSum)

maxSubarray([2,3,-6,4,2,-8,3])