class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights = heights + [0]

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                popped_height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                area = popped_height * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area

