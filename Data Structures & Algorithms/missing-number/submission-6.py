class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0

        nums.sort()
        for num in nums:

            if (start != num): return start

            start += 1
        
        return len(nums)