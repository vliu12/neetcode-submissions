class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force solution
        out = set()
        nums.sort()

        length = len(nums)
        for i in range(length):
            for j in range(i+ 1, length):
                for k in range(j+ 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        new = [nums[i], nums[j], nums[k]]
                        out.add(tuple(new))

        return [list(i) for i in out]