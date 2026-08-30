class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        return self.solve(nums, 0, dp)

    def solve(self, nums, ind, dp):
        if ind >= len(nums) - 1:
            dp[ind] = 0
            return 0
        if nums[ind] + ind >= len(nums) - 1:
            return 1
        if ind in dp:
            return dp[ind]
        
        dp[ind] = float('inf')
        for k in range(ind + 1, nums[ind] + ind + 1):
            dp[ind] = min(1 + self.solve(nums, k, dp), dp[ind])
        return dp[ind]
        