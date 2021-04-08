class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x > 0, nums))
        
        if nums == [] or min(nums) != 1:
            return 1
        
        the_map = {}
        smallest = max(nums) + 1
        
        for num in nums:
            the_map[num] = num + 1
        
        for key in the_map.keys():
            if not the_map[key] in the_map:
                smallest = min(smallest, the_map[key])
        
        return smallest