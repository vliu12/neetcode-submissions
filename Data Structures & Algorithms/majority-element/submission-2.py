class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maxCount = 0
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if maxCount < counts[num]:
                res = num
                maxCount = counts[num]
        
        return res