from typing import List
from math import inf

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    diff = inf
    sum_global = 0
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while r > l:
            total = a + nums[l] + nums[r]
            if total == target:
                return total
            else:
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                curr_diff = abs(target - total)
                if curr_diff < diff: 
                    sum_global = total
                    diff = curr_diff
                
    return sum_global

print(threeSumClosest([-1,2,1,-4],1))