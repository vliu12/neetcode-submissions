class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] * prefix[-1])

        suffix = []
        reversed = nums.copy()
        reversed.reverse()
        for i in range(len(nums)):
            if i == 0:
                suffix.append(reversed[i])
            else:
                suffix.append(reversed[i] * suffix[-1])
        suffix.reverse()
        res = []
        for i in range(len(nums)):
            pre = prefix[i-1] if i - 1 >= 0 else 1
            suff = suffix[i + 1] if i + 1 < len(nums) else 1
            res.append(pre * suff)

        return res
        