
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    res = [1] * length
    right = 1
    
    for i in range(1, length):
        res[i] = res[i - 1] * nums[i - 1]
    
    for i in range(1, length + 1):
        res[-i] *= right
        right *= nums[-i]
    return res
    
print(productExceptSelf([-1,1,0,-3,3]))