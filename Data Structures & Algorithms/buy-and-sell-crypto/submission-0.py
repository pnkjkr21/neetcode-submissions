class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suff = []
        for i in range(len(prices) - 1, -1, -1):
            if not suff:
                suff.append(prices[i])
            else:
                suff.append(max(prices[i], suff[-1]))
        suff.reverse()
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, suff[i] - prices[i])
        
        return ans
        