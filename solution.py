class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            for j, b in enumerate(nums[i + 1:], i + 1):
                if j > i + 1 and b == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1
                while r > l:
                    total = a + b + nums[l] + nums[r]
                    if total == target:
                        res.append([a, b, nums[l], nums[r]])
                        r -= 1
                        while r > j and nums[r + 1] == nums[r]:
                            r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1

        return res