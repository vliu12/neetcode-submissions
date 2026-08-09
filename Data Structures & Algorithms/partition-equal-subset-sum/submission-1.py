class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        n = len(nums)

        def dfs(i, target):
            if i == 0 and target == 0:
                a = True
            elif i == 0 and target > 0:
                a = False
            elif target < nums[i - 1]:
                a = dfs (i - 1, target)
            else:
                a = dfs (i - 1, target) or dfs (i - 1, target - nums[i - 1])

            return a

        return dfs (n, sum(nums) // 2)