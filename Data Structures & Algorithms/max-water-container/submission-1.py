class Solution:
    # two pointers
    def maxArea(self, heights: List[int]) -> int:
        # fix a pointer to the start and the end
        l = 0
        r = len(heights) - 1
        waterMax = 0

        while l < r: 
            width = r - l
            height = min(heights[l], heights[r])
            currMax = width * height
            waterMax = max(waterMax, currMax)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return waterMax


        
