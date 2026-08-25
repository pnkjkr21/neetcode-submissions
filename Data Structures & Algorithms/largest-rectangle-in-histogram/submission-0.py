class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                right.append(len(heights))
            else:
                right.append(stack[-1])
            stack.append(i)
        right.reverse()
        
        stack = []
        left = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1])
            stack.append(i)
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, (right[i] - left[i] - 1) * heights[i])
        return ans
        
        