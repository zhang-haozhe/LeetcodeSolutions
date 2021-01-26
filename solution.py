from math import inf

def quickSort(arr):
    length = len(arr)
    if length < 2:
        return arr
    
    # in our case, we assume that the pivot is the first element. while in practice, the choice of the pivot position can greatly influence the performance.
    pivot = 0
    frontier = 1
    biggerNum = -inf

    # below is the partitioning step. each time, compare if the pivot element and the currently iterated element:
    # if the current is larger than the pivot, record its position.
    # if the current is smaller than or equal to the pivot, then the frontier moves right. if there is a larger element that has appeared, 
    # then swap this element and the current element.

    curr = frontier

    while curr < length:
        if arr[curr] <= arr[pivot]:
            if biggerNum != -inf:
                arr[biggerNum], arr[curr] = arr[curr], arr[biggerNum]
                biggerNum = -inf
                curr -= 1
            frontier += 1
        else:
            if biggerNum == -inf:
                biggerNum = curr
        curr += 1
    
    # each time the array is executed, swap the element to the left of the frontier and the pivot
    arr[pivot], arr[frontier - 1] = arr[frontier - 1], arr[pivot]

    # then we divide the array by the new pivot. respectively do quick sort for the two sub-arrays.
    leftArr = quickSort(arr[:frontier - 1])
    rightArr = quickSort(arr[frontier:])

    # at the end, join the sorted sub-arrays.
    return leftArr + [arr[frontier - 1]] + rightArr


print(quickSort([4,3,7,2,9,1,8]))