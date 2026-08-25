class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1] - i)
            stack.append(i)
        ans.reverse()
        return ans
        