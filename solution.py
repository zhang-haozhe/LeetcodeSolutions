class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dek = collections.deque()
        min_dek = collections.deque()

        length = 0
        left = 0
        for i in range(len(nums)):
            while max_dek and nums[max_dek[-1]] < nums[i]:
                max_dek.pop()
            while min_dek and nums[min_dek[-1]] > nums[i]:
                min_dek.pop()
            max_dek.append(i)
            min_dek.append(i)
            
            res = nums[max_dek[0]] - nums[min_dek[0]]
            while res > limit:
                left += 1
                while max_dek and left > max_dek[0]:
                    max_dek.popleft()
                while min_dek and left > min_dek[0]:
                    min_dek.popleft()
                res = nums[max_dek[0]] - nums[min_dek[0]]
            
            length = max(length, i - left + 1)
        return length