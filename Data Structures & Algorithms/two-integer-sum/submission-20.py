class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_nums = {}

        for i in range(len(nums)):
            to_find = target - nums[i]

            if to_find in all_nums:
                return [all_nums[to_find], i]

            all_nums[nums[i]] = i 