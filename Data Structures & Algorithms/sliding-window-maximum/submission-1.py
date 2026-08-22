
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque([])
        ans = []
        i, j = 0, 0
        while j < len(nums):
            while stack and stack[-1] < nums[j]:
                stack.pop()
            stack.append(nums[j])
            if j - i + 1 == k:
                ans.append(stack[0])
                if stack[0] == nums[i]:
                    stack.popleft()
                i += 1
            j += 1
        return ans
            
        