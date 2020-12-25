# Parameters:
#  arr: List[int]
#  k: int
# return type: bool

def findPair(arr, k):
    # your code here
    sortedArr = sorted(arr)
    left = 0
    right = len(sortedArr) - 1
    for i in range(len(sortedArr)):
        if sortedArr[left] + sortedArr[right] == k:
            return True
        elif sortedArr[left] + sortedArr[right] < k:
            left += 1
            if left == right:
                left += 1
        elif sortedArr[left] + sortedArr[right] > k:
            right -= 1
            if left == right:
                right -= 1
    return False