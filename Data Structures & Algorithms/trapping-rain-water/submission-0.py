class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        for i in height:
            if not left:
                left.append(i)
            else:
                left.append(max(i, left[-1]))
        
        for i in range(len(height) - 1, -1, -1):
            if not right:
                right.append(height[i])
            else:
                right.append(max(height[i], right[-1]))
        right.reverse()
        ans = 0
        for i in range(1, len(height) - 1):
            ans += min(left[i], right[i]) - height[i]
        return ans
        