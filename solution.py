from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while r > l:
            total = a + nums[l] + nums[r]
            if total == 0:
                res.append([a, nums[l], nums[r]])
                r -= 1
                while r > i and nums[r + 1] == nums[r]:
                    r -= 1
            elif total > 0:
                r -= 1
            else:
                l += 1

    return res

print(threeSum([-1,0,1,2,-1,-4]))