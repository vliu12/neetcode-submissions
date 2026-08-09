class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        maxEnd = nums[0]
        minEnd = nums[0]

        best = nums[0]

        for i in range(1, n):   
            x = nums[i]

            prev_max = maxEnd
            prev_min = minEnd

            maxEnd = max(x, x * prev_max, x * prev_min)
            minEnd = min(x, x * prev_max, x * prev_min)

            best = max(best, maxEnd)
        
        return best

