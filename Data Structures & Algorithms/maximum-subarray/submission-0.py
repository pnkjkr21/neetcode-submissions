class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rs = 0
        ans = float('-inf')

        for num in nums:
            rs += num
            if rs <= num:
                rs = num
            ans = max(ans, rs)
        
        return ans
        