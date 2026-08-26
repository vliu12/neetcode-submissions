class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        best_max = 0

        while l < r:
            left = heights[l]
            right = heights[r]

            area = (r - l) * min(left, right)

            best_max = max(area, best_max)

            if left > right:
                r -= 1
            else:
                l += 1

        return best_max